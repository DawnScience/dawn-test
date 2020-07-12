#!/bin/bash


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
# This bash script is designed to create pipeline and json file for the DAWN headless processing, #
# modified to either their current, or some input defined, locations. DAWN is then invoked and    #
# the pipeline is run. The result from this reduction is then compared against a known working    #
# state to see if the processing in DAWN has been broken.                                         #
#                                                                                                 #
###################################################################################################
#                                                                                                 #
# Last updated 2017-04-24                                                                         #
#                                                                                                 #
# Author: Tim Snow (tim.snow@diamond.ac.uk)                                                       #
#                                                                                                 #
###################################################################################################

# Script usage:
#
# validator.sh
# (Defaults to internal values)
#
# validator.sh workingDirectory neXusDataFile neXusPipelineFile jsonFile neXusCalibrationFile neXusMaskFile neXusResultsFile
# (Overrides internal values)
#
# Script inputs are:
#
# workingDirectory - The directory that the script shall work from, must be writable to the script
# neXusDataFile - The raw diffraction data for reducing
# neXusPipelineFile - The model pipeline that will be modified and used for the reduction
# jsonFile - The JSON file that accompanies the pipeline file
# neXusCalibrationFile - The calibration file for the diffraction data
# neXusMaskFile - The mask file for the diffraction data
# neXusResultsFile - The model result file, which the freshly reduced data will be compared against
#
# Script exit codes are:
#
# 0 - Success! The files were the same!
# 1 - Failure! Couldn't make the tmp folder in the working directory
# 2 - Failure! Couldn't set up the processing pipeline in the tmp directory
# 3 - Failure! Couldn't set up the JSON file in the tmp directory
# 4 - Failure! Couldn't perform the data reduction in DAWN
# 5 - Failure! File comparison failed
# 6 - Failure! Couldn't delete tmp from working directory


# We have to fetch the current script location BEFORE loading the modules or we lose the path!
workingDirectory="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Next we do our 'imports' or module loadings...
module load dawn/nightly > /dev/null 2>&1
module load python/ana > /dev/null 2>&1

# Then a bit of space
echo ""

# If we've been given enough variables, let's listen to the invoker and override our default locations
if [ $# -eq 7 ]
then
	workingDirectory="$1"
	tmpDirectory="$workingDirectory/tmp"
	jsonFile="$4"
	neXusCalibrationFile="$5"
	neXusDataFile="$2"
	neXusMaskFile="$6"
	neXusPipelineFile="$3"
	neXusResultsFile="$7"
	cd $workingDirectory
	echo "Hard coded default locations overriden"
else
	# If not let's be a bit smart, as the folder might have moved, but overall use our defaults
	tmpDirectory="$workingDirectory/tmp"
	jsonFile="$workingDirectory/tmp/validation.json"
	neXusCalibrationFile="$workingDirectory/default_dataset/i22-363061_calibration.nxs"
	neXusDataFile="$workingDirectory/default_dataset/i22-363061.nxs"
	neXusMaskFile="$workingDirectory/default_dataset/i22-363061_mask.nxs"
	neXusPipelineFile="$workingDirectory/default_dataset/i22-363061_pipeline.nxs"
	neXusResultsFile="$workingDirectory/default_dataset/i22-363061_processed.nxs"
	echo "Using default locations as not enough arguments given"
fi

# First, try to set up a temporary directory
if [ ! -d "$tmpDirectory" ]
then
	mkdir "$tmpDirectory" > /dev/null 2>&1
	exitCode="$?"

	if [ $exitCode -ne 0 ]
	then
		echo ""
		echo "Couldn't create a tmp directory in the working directory, exit code: $exitCode, see mkdir manpage. Exiting here."
		echo ""
		exit 1
	fi
fi

# Next, try to make our new NeXus pipeline file, complete with customised paths for the calibration and mask files
python $workingDirectory/pipelineEditor.py $workingDirectory $neXusPipelineFile $neXusCalibrationFile $neXusMaskFile
exitCode="$?"

if [ $exitCode -ne 0 ]
then
	echo ""
	echo "Couldn't set up the processing pipeline in the tmp directory, exit code: $exitCode, see pipelineEditor.py for details. Exiting here."
	echo ""
	exit 2
fi

# Try to set up the processing JSON file, as required, and stick it in our tmp directory
echo '{"runDirectory": "'"$workingDirectory"'/tmp", "name": "Validation Test", "filePath": "'"$neXusDataFile"'", "dataDimensions": [-1, -2], "processingPath": "'"$tmpDirectory"'/validationPipeline.nxs", "outputFilePath": "'"$workingDirectory"'/tmp/validationResults.nxs", "deleteProcessingFile": false, "datasetPath": "/entry1/detector", "numberOfCores" : 1, "xmx" : 1024}' > $jsonFile
exitCode="$?"

if [ $exitCode -ne 0 ]
then
	echo ""
	echo "Couldn't set up the processing JSON in the tmp directory, exit code: $exitCode, see echo manpage for details. Exiting here."
	echo ""
	exit 3
fi

# Then perform the data reduction using DAWN
/dls_sw/apps/DawnDiamond/2.4/builds/release-linux64/dawn -noSplash -configuration $workingDirectory/tmp/.eclipse -application org.dawnsci.commandserver.processing.processing -data @none -path $jsonFile > $workingDirectory/tmp/log.txt 2>&1
exitCode="$?"

if [ $? -ne 0 ]
then
	echo ""
	echo "Couldn't perform the data reduction using DAWN, exit code: $exitCode, see the DAWN manual for details. Exiting here."
	echo ""
	exit 4
fi

$workingDirectory/h5FileComparer.sh "$neXusResultsFile" "$workingDirectory/tmp/validationResults.nxs"
exitCode="$?"

if [ $exitCode -ne 0 ]
then
	echo ""
	echo "The file comparison failed, exit code: $exitCode, see h5FileComparer.sh for details. Exiting here."
	echo ""
	exit 5
fi

rm -R $tmpDirectory
exitCode="$?"

if [ $exitCode -ne 0 ]
then
	echo ""
	echo "Couldn't delete the tmp directory in the working directory, exit code: $exitCode, see rm manpage for details. Exiting here."
	echo ""
	exit 6
fi

# If we've gotten this far, success! Give some space then exit.
echo ""
exit 0
