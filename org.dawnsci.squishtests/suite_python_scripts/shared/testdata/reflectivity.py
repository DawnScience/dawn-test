'''
Created on 18 Sep 2012

@author: Jonathan Rawle

To run this script, click in this window then press Ctrl-Alt-Enter
Choose "Console for the currently active editor"
The script will then run in the terminal below

'''

import scisoftpy as dnp
import numpy as np
import reflectivity.nsplice as nsplice
import reflectivity.ErrorProp as ep
from scipy.stats import norm

# refl(range(116047,116050), "/dls/i07/data/2012/si7618-1", "/dls/i07/data/2012/si7618-1/processing/test", 7e11, 400, 150, 0.000, 0.99188, back=())
# remember that python ranges need to be max+1 !!! can also specify individually, e.g. (115822,115823.115829) 
def refl(runfiles, pathtofiles, outputpath, scalar, beamheight, footprint, angularfudgefactor, wl, back=()):
        # scalar - scale factor to divide the data by
        # beamheight FWHM in microns
        # footprint in mm
        # angular offset correction in degrees
        #  wavelength in wl
        #  back is an optional variable to subtract a background, set back=1 to do a background subtraction
 
        qq = []
        RR = []
        dR = []
        ii = -1
        for filename in runfiles:
            data = dnp.io.load(pathtofiles + "/" + str(filename) + ".dat")
            ii += 1

            theta = data.alpha
            # work out the q vector
            qqtemp = 4 * dnp.pi * dnp.sin((theta + angularfudgefactor) * dnp.pi /180) / wl
            #qqtemp = data.qdcd
            
            # this section is to allow users to set limits on the q range used from each file
            if not 'qmin' + str(ii) in refl.__dict__:
                qmin = qqtemp.min()
            else:
                print "USER SET",
                qmin = refl.__getattribute__('qmin' + str(ii))
            print 'refl.qmin' + str(ii) + " = " + str(qmin) + " ;",
            if not 'qmax' + str(ii) in refl.__dict__:
                qmax = qqtemp.max()
            else:
                print "USER SET",
                qmax = refl.__getattribute__('qmax' + str(ii))
            print 'refl.qmax' + str(ii) + " = " + str(qmax) + " ;",            
            
            roi1_sum = data.roi1_sum
            roi1_sum = roi1_sum[dnp.where((qqtemp >= qmin) & (qqtemp <= qmax))]
            roi1dr = dnp.sqrt(roi1_sum)
            theta = theta[dnp.where((qqtemp >= qmin) & (qqtemp <= qmax))]
            qqtemp = qqtemp[dnp.where((qqtemp >= qmin) & (qqtemp <= qmax))]
 
            bg_sum = dnp.zeros(len(roi1_sum))
            bg_dr = dnp.zeros(len(roi1dr))
 
            # if background ROI number given as int, convert to a single-item tuple
            if type(back) == int:
                back = (back,)
            
            # subtract any background ROIs from the data
            if len(back) > 0 and back[0] > 0:
                if ii==0:
                    print "Using background from " + str(len(back)) + " ROIs: " + str(back)
                for bg in back:
                    if ('roi' + str(bg) + '_sum' in data.keys()):
                        bg_cur = data[data.keys().index('roi' +str(bg) + '_sum')]
                        dr_cur = dnp.sqrt(bg_cur)
                        (bg_sum, bg_dr) = ep.EPadd(bg_sum, bg_dr, bg_cur, dr_cur)
                (bg_sum, bg_dr) = ep.EPmulk(bg_sum, bg_dr, 1.0/len(back))
            else:
                if ii==0:
                    print "Not subtracting a background"                
            (RRtemp, drtemp) = ep.EPsub(roi1_sum, roi1dr, bg_sum, bg_dr)
 
            # do a footprint correction.
            # assumes that the beam is gaussian in profile, with a FWHM of "beamheight".
            # footprint of sample is measured in mm.
            areamultiplier = 2*(norm.cdf(footprint * dnp.sin((theta + angularfudgefactor) / 180 * dnp.pi) / 2, 0, 1e-3 * beamheight/ (2*dnp.sqrt(2*dnp.log(2)))) - 0.5)
            RRtemp /= areamultiplier
            drtemp /= areamultiplier


            # for the 2nd, 3rd, 4th q ranges have to splice the data on the end of the preexisting data
            if(ii > 0):
                # splice
                (scalingfactor, sferror) = nsplice.getScalingInOverlap(qq, RR, dR, qqtemp, RRtemp, drtemp)
                RRtemp *= scalingfactor
                drtemp *= scalingfactor
                print "Error in scaling factor: %2.3f %%" % (sferror/scalingfactor*100)
            
            # now concatenate the data.
            qq = dnp.concatenate((qq, qqtemp))
            RR = dnp.concatenate((RR, RRtemp))
            dR = dnp.concatenate((dR, drtemp))
        # end of per-file loop

        RR /= scalar
        dR /= scalar
        
        RR = RR[np.argsort(qq)]
        dR = dR[np.argsort(qq)]
        qq = np.sort(qq)
        
        # write out the data.
        np.savetxt(outputpath+"/"+str(runfiles[0])+"_refl.dat",dnp.concatenate((qq,RR,dR)).reshape(3,qq.shape[0]).transpose())

        # plot the resulting
        #dnp.plot.line(qq,RR,name='Plot 2')
