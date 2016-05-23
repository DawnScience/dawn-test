'''
Created on 14 Sep 2011
Revised 10 Oct 2012 by Thomas Connolley

@author: ssg37927
'''

#
# JYTHON Script
#

import scisoftpy as dnp
from uk.ac.diamond.scisoft.analysis.plotserver import GuiParameters as _guiparam


class EDXDCalibrator(object):
    '''
    classdocs
    '''
    
    spectrun_window = "Plot 1"
    calibration_window = "Plot 2"
    ## Comment or uncomment these lines to select the calibration material you wish to use
    ## Silicon
    ##standard_peaks = [2.0036, 3.2719, 3.8366, 4.6271, 5.0423, 5.6671, 6.0108, 6.5438, 6.8436]
    ## Lab6 (check before using)
    ##standard_peaks = [1.5115, 2.1376, 2.6180, 3.0230, 3.3798, 3.7024, 4.2752, 4.5345, 4.7798, 5.0131, 5.2360, 5.4498, 5.6555, 6.0460, 6.2321, 6.4128, 6.5885, 6.9266, 7.0896, 7.4048, 7.5575, 7.7072, 7.8540]
    ##CeO2(764b)
    standard_peaks = [2.010944, 2.322096, 3.28394, 3.850761, 4.021988, 4.644192, 5.060891, 5.192364, 5.68795, 6.032982, 6.567879, 6.868852, 6.966288]
    ##
    #standard_peaks = []


    def __init__(self, filename):
        '''
        Constructor
        '''
        self.data = dnp.io.load(filename)
        self.results = {}
        
    
    def load_data_element(self, element_number):
        identifier = "/entry1/EDXD_Element_%02i/data" % element_number
        element = self.data[identifier][:]
        #energy = self.data.getLazyDataset("/entry1/EDXD_Element_%02i/edxd_energy_approx" % element_number).getSlice(None,None)
        counts = element.sum(0)
        energy = dnp.arange(counts.shape[0])
        return (counts, energy)
    
    def plot_element(self, element_number):
        (element, energy) = self.load_data_element(element_number)
        dnp.plot.updateline(energy, element,self.spectrun_window)
    
    def get_peak_list_from_view(self):
        fp = _guiparam.FITTEDPEAKS
        bean = dnp.plot.getbean(self.spectrun_window)
        print bean
        peaks = bean[fp]
        return peaks
    
    def calc_bins_vrs_q(self):
        peaklist = self.get_peak_list_from_view()
        peakpos = []
        for peak in peaklist :
            peakpos.append(peak.getPosition())
        peakpos.sort()
        x = dnp.array(self.standard_peaks)
        y = dnp.array(peakpos)
        max_size = min(x.shape[0], y.shape[0])
        x = x[0:max_size]
        y = y[0:max_size]
        x.name = "Calibration Values"
        y.name = "Peak positions"
        fr = dnp.fit.polyfit(y, x, 2, full=True)
        return (x,y,fr[1])
    
    def calibrate_elements(self, start, stop):
        for i in range(start, stop):
            self.plot_element(i)
            print "Select Peaks in Plot 1 for element %i" % i
            void = raw_input("Press enter here when finished selecting peaks")
            (x,y,fr) = calib.calc_bins_vrs_q()
            self.results[i] = (x,y,fr)
        print "********************"
        print "Calibration Complete"
        print "********************"
    
    def report(self):
        print "==========================="
        print "Calibration Function report"
        print "==========================="
        keys = self.results.keys()
        keys.sort()
        for key in keys:
            result = self.results[key][2]
            print "Element %i, has f(x) = %f*x^2 + %f*x + %f with residual %f" % (key, result[0], result[1], result[2], result.residual )
    
    def full_report(self):
        print "============================="
        print "Calibration Per Peak Analysis"
        print "============================="
        keys = self.results.keys()
        keys.sort()
        string = "Element  "
        for peak in self.standard_peaks:
            string += "%1.4f  " % peak
        string += "|  Residual  "
        print string
        length = len(string)
        string = ""
        for i in range(length):
            string += "-"
        print string
        for key in keys:
            result = self.results[key][2]
            string = "  %02i     " % key
            i = 0;
            for point in self.results[key][1] :
                value = result[0]*point*point + result[1]*point + result[2]
                string += "%1.4f  " % abs(self.standard_peaks[i] - value)
                i += 1
            string += "|  %1.6f" % result.residual
            print string
    
    def display_parameters(self, parameter_number):
        keys = self.results.keys()
        keys.sort()
        data = []
        for key in keys:
            result = self.results[key][2]
            data.append(result[parameter_number])
        y = dnp.array(data)
        x = dnp.array(keys)
        dnp.plot.line(x,y,name=self.calibration_window);
    
    def print_report(self, filename):
        file = open(filename, 'w')
        keys = self.results.keys()
        keys.sort()
        for key in keys:
            result = self.results[key][2]
            file.write("%02i, %1.10e, %1.10e, %1.10e\n" % (key, result[0], result[1], result[2]))
        file.close()
        
print "Calibrating EDXD Q axis"
calib = EDXDCalibrator("/scratch/workspace/suite_python_scripts/tst_i12_auto_peakfitting/workspace/data/examples/i12/36153.nxs")
calib.calibrate_elements(1, 24)
calib.report()
calib.full_report()
calib.print_report("/scratch/workspace/suite_python_scripts/tst_i12_auto_peakfitting/workspace/data/examples/i12/36153_TESTING_2014-04-23_calib_CeO2.txt")
# finally display the curve shown by the second parameter(could be useful)   
calib.display_parameters(1)
