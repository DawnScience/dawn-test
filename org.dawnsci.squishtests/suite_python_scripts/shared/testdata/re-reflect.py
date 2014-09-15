'''
Created on 28 May 2014

@author: Jonathan Rawle

****************************************************************

To run this script, click in this window then press Ctrl-Alt-Enter
Choose "Console for the currently active editor"
The script will then run in the terminal below

To process a data file, use:
rerefl(range(10000,10006))
which will stitch scans 10000 to 10005 (last number is non-inclusive)

Alternatively, you can do:
rerefl(10000,10001,10003,10004)
to stitch non-contiguous scans

Due to a bug in DAWN, you then need to draw regions of interest on the image and run
getrois()
You need to re-run this ***every time*** you change, add or delete ROIs

Finally run the same rerefl command again to do the processing

'''

import scisoftpy as dnp
import numpy as np
import reflectivity.nsplice as nsplice
import reflectivity.ErrorProp as ep
from scipy.stats import norm
import re
import os
import platform

# path to the input .dat files
if platform.system() == 'Windows':
    pathtofiles = r'\/dls-science\/science\/groups\/das\/dlshudson\/dawn_squish_data\/i07\/cm4957-3'
else:
    pathtofiles = r'/dls/science/groups/das/dlshudson/dawn_squish_data/i07/cm4957-3'
# path for the output data
outputpath = r'/scratch/workspace/suite_python_scripts/tst_i07_reflectivity/workspace/reflectivity'
# scale factor to divide the data by
scalar = 1e7
# beam height FWHM in microns
beamheight = 150
# footprint in mm
footprint = 8
# angular offset correction in degrees   
angularfudgefactor = 0
# wavelength in Angstrom
wl = 0.82657    
# image to display initially to enable ROIs to be drawn interactively (0=first image from scan)
imgdisp = 5    

###############################################################################################

print "\nType  rerefl(range(12345, 12351))  to process a range of .dat files"
print "Type  getrois()  each time you update the regions of interest due to a DAWN bug"

def replace_path(filename):
    # replace the pathname hard-coded in the dat file with the one we specified
    global pathtofiles
    # if we are running Windows, we also need to replace forward- with back-slashes
    if os.name == 'nt':
        sep = '\\\\'
    else :
        sep = '/'
    # if windows correctly modify the path to the image file
    if platform.system() == 'Windows':
        filename = re.sub(r'/dls/','//dls-science/', filename)
    newpath = re.sub(r'/dls/\w\d\d/data/\d\d\d\d/\w\w\d+-\d', pathtofiles, filename)
    result = re.sub(r'/', sep, newpath)
    return result
def getrois():
    global savedbean
    bean = dnp.plot.getbean(name='Plot 1')
    try:
        rois = dnp.plot.getrois(bean)
        norois = len(rois)
    except(KeyError, TypeError):
        print "Please define/edit the regions of interest then type getrois() again"
        norois = 0    
    if norois > 0:
        savedbean = bean
        print str(norois) + " ROIs detected"
        print "\nPlease remember to type getrois() every time you change the regions of interest."
        print "This is due to a bug in DAWN."
def showimage(number=imgdisp):
        global firstfiledata
        image = dnp.io.load(replace_path(firstfiledata['file'][number]), warn=False)
        dnp.plot.image(image[0], name='Plot 1', resetaxes=False)
def rerefl(runfiles):
        global pathtofiles, savedbean, firstfiledata
        qq = []
        RR = []
        dR = []
        ii = -1
        for filename in runfiles:
            roi1sum = []
            roi1dr = []
            bg_sum = []
            bg_dr = []
            data = dnp.io.load(pathtofiles + "/" + str(filename) + ".dat")
            ii += 1
            if ii == 0:
                firstfiledata = data

            # define theta
            theta = data.alpha
            # define q
            qqtemp = 4 * dnp.pi * dnp.sin((theta + angularfudgefactor) * dnp.pi /180) / wl
            #qqtemp = data.qdcd
            
            qmin = qqtemp.min()
            qmax = qqtemp.max()

            # plot first image of first file
            if ii == 0:
                global image
                image = dnp.io.load(replace_path(data['file'][imgdisp]), warn=False)
                dnp.plot.image(image[0], name='Plot 1', resetaxes=False)

            # find ROIs from saved bean
            try:
                rois = dnp.plot.getrois(savedbean)
                norois = len(rois)
            # if we don't have any ROIs yet, ask the user to draw some
            except(KeyError, TypeError, NameError):
                if ii==0:
                    print "\nPlease define some regions of interest then type getrois()"
                    print "You must type getrois() after adding/changing any regions due to a bug in DAWN."
                norois = 0                
            
            # this section to be restored when ROIs are working again
            ## find ROIs from plot window
            #bean = dnp.plot.getbean('Plot 1')
            #try:
            #    rois = dnp.plot.getrois(bean)
            #    norois = len(rois)
            ## if we don't have any ROIs yet, ask the user to draw some
            #except(KeyError, TypeError):
            #    if ii==0:
            #        print "Please define some regions of interest"
            #    norois = 0
            
            if norois > 0:
                if ii == 0:
                    print str(norois) + " ROIs defined, " + str(norois-1) + " will be used for the background"
 
                for imgfile in data['file']:
                    imgdata = dnp.io.load(replace_path(imgfile), warn=False)
                    dnp.plot.image(imgdata[0], name="Plot 1", resetaxes=False)
                    image = imgdata[0].transpose() # Pilatus images load with axes transposed for some reason
                    bg_pt = 0
                    bgdr_pt = 0
                    for j in range(0,norois):
                        roi = image[int(rois[j].spt[0]):int(rois[j].spt[0]+rois[j].len[0]), int(rois[j].spt[1]):int(rois[j].spt[1]+rois[j].len[1])]
                        roisum_pt = dnp.float(roi.sum())
                        if j == 0:
                            roi1sum.append(roisum_pt)
                            roi1dr.append(dnp.sqrt(roisum_pt))
                        else:
                            (bg_pt, bgdr_pt) = ep.EPadd(bg_pt, bgdr_pt, roisum_pt, dnp.sqrt(roisum_pt))
                    bg_sum.append(bg_pt)
                    bg_dr.append(bgdr_pt)

                # convert lists to arrays
                (roi1sum, roi1dr, bg_sum, bg_dr) = (dnp.array(roi1sum), dnp.array(roi1dr), dnp.array(bg_sum), dnp.array(bg_dr))
                
                # normalise background
                if norois > 1:
                    bgsize = 0
                    for k in range(1, norois):
                        bgsize += rois[k].len[0]*rois[k].len[1]
                    (bg_sum, bg_dr) = ep.EPmulk(bg_sum, bg_dr, rois[0].len[0]*rois[0].len[1]/bgsize)

                # subtract background
                (RRtemp, drtemp) = ep.EPsub(roi1sum, roi1dr, bg_sum, bg_dr)

                # do a footprint correction.
                # assumes that the beam is gaussian in profile, with a FWHM of "beamheight".
                # footprint of sample is measured in mm.
                areamultiplier = 2*(norm.cdf(dnp.float(footprint) * dnp.sin((theta + dnp.float(angularfudgefactor)) / 180 * dnp.pi) / 2, 0, 1e-3 * dnp.float(beamheight)/ (2*dnp.sqrt(2*dnp.log(2)))) - 0.5)
                RRtemp /= areamultiplier
                drtemp /= areamultiplier


                # for the 2nd, 3rd, 4th q ranges have to splice the data on the end of the preexisting data
                if(ii > 0):
                    (scalingfactor, sferror) = nsplice.getScalingInOverlap(qq, RR, dR, qqtemp, RRtemp, drtemp)
                    RRtemp *= scalingfactor
                    drtemp *= scalingfactor
            
                # now concatenate the data.
                qq = dnp.concatenate((qq, qqtemp))
                RR = dnp.concatenate((RR, RRtemp))
                dR = dnp.concatenate((dR, drtemp))
        # end of per-file loop
        if norois > 0:
            RR /= dnp.float(scalar)
            dR /= dnp.float(scalar)
        
            RR = RR[np.argsort(qq)]
            dR = dR[np.argsort(qq)]
            qq = np.sort(qq)
       
            # write out the data.
            np.savetxt(outputpath+"/"+str(runfiles[0])+"_rerefl_bkg1.dat",dnp.concatenate((qq,RR,dR)).reshape(3,qq.shape[0]).transpose(), fmt="%.10f %.10e %.10e")
            print "Output saved to " + outputpath+"/"+str(runfiles[0])+"_rerefl_bkg1.dat"

            # plot the resulting
            dnp.plot.line(qq,dnp.log10(RR),name='Plot 2')
