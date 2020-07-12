###################################################################################################
#                                                                                                 #
# Copyright (c) 2017 Diamond Light Source Ltd.                                                    #
#                                                                                                 #
# All rights reserved. This program and the accompanying materials are made available under the   #
# terms of the Eclipse Public License v1.0 which accompanies this distribution, and is available  #
# at http://www.eclipse.org/legal/epl-v10.html                                                    #
#                                                                                                 #
###################################################################################################
#                                                                                                 #
# This Python script is designed to copy and modify a DAWN pipeline file to contain the correct   #
# calibration and mask locations as well as generating the accompanying JSON file for the         #
# headless DAWN client to reduce an input diffraction image for comparison against a 'model'      #
# reduction file.                                                                                 #
#                                                                                                 #
###################################################################################################
#                                                                                                 #
# Last updated 2017-03-30                                                                         #
#                                                                                                 #
# Author: Tim Snow (tim.snow@diamond.ac.uk)                                                       #
#                                                                                                 #
###################################################################################################


# Script usage:
#
# pipelineEditor.py workingDirectory inputPipelineFilePath pathToCalibrationFile pathToMaskFile
#
# Script inputs are:
#
# workingDirectory - Full path to the current working directory, must have write access!
# inputPipelineFilePath - Full path to the model pipeline path
# pathToCalibrationFile - Full path to the diffraction image calibration file
# pathToMaskFile - Full path to the diffraction image mask file
# 
# Script exit codes are:
#
# 0 - Success!
# 1 - Wrong number of inputs
# 2 - The working directory doesn't exist
# 3 - The given pipeline file path doesn't work
# 4 - The given calibration file path doesn't work
# 5 - The given mask file path doesn't work
# 6 - No tmp directory in the working directory and couldn't make one either
# 7 - Couldn't copy the model pipeline file to tmp
# 8 - Couldn't edit the copied pipeline file


# Starting with some imports!
import h5py
from shutil import copy
from os import mkdir, sep
from sys import argv, exit
from os.path import exists, isdir

# Check our inputs, if they match assign them and if not send out a warning!
if (len(argv) == 5):
	workingDirectory = str(argv[1])
	inputPipelineFilePath = str(argv[2])
	pathToCalibrationFile = str(argv[3])
	pathToMaskFile = str(argv[4])
else:
	print "\nThis script will only run is given four arguments which should be:\n\n- The working directory\n- A full path to some data\n- A full path to a NeXus calibration file\n- A full path to a NeXus mask file\n\nPlease try again.\n"
	exit(1)

# Now exhaustively check the given arguments
if (isdir(workingDirectory) == False):
	print "The given path to the working directory leads nowhere!"
	exit(2)

if (exists(inputPipelineFilePath) == False):
	print "The given path to the pipeline file leads nowhere!"
	exit(3)

if (exists(pathToCalibrationFile) == False):
	print "The given path to the calibration file leads nowhere!"
	exit(4)

if (exists(pathToMaskFile) == False):
	print "The given path to the mask file leads nowhere!"
	exit(5)

# Check, and if neccessary setup, that we have a tmp directory
tmpDirectory = workingDirectory + "/tmp"

if (isdir(tmpDirectory) == False):
	try:
		mkdir(tmpDirectory)
	except:
		print "There wasn't a tmp directory in the working directory and one couldn't be created"
		exit(6)

# Copy the pipeline file so that we can customise it
pipelineFilePath = inputPipelineFilePath.split(sep)
outputPipelineFilePath = tmpDirectory + "/validationPipeline.nxs"

try:
	copy(inputPipelineFilePath, outputPipelineFilePath)
except:
	print "There was a problem copying the pipeline file"
	exit(7)

# Then try to edit the variables in the pipeline so that they work with our current setup
try:
	neXusFileReference = h5py.File(outputPipelineFilePath)

	# The hard coded, internal, NeXus paths
	neXusCalibrationPath = "/entry/process/4/data"
	neXusMaskPath = "/entry/process/5/data"

	# Making room
	del(neXusFileReference[neXusCalibrationPath])
	del(neXusFileReference[neXusMaskPath])


	# For our new variables!
	neXusFileReference[neXusCalibrationPath] = u'{"filePath":"' + pathToCalibrationFile + '"}'
	neXusFileReference[neXusMaskPath] = u'{"filePath":"' + pathToMaskFile + '"}'

	neXusFileReference.close()
except:
	print "There was a problem opening the copied pipeline file"
	exit(8)

# A bit of user feedback
print "\nSuccessfully copied the pipeline to tmp and edited to the internal filepaths to:\n"
print "    Calibration file: " + pathToCalibrationFile
print "    Mask file: " + pathToCalibrationFile + "\n"

# Success!
exit(0)
