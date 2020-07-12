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
# This bash script is designed to take the output from data reduced from a development version of #
# DAWN and compare it to data obtained from a stable version of DAWN to deduce whether the        #
# processing pipeline (and therefore autoprocessing) has been killed accidentally.                #
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
# h5FileComparer.sh fileOne fileTwo
#
# Script inputs are:
#
# fileOne - First file for comparing
# fileTwo - Second file for comparing 
#
# Script exit codes are:
#
# 0 - Success! The files were the same!
# 1 - Failure! The files weren't the same...
# 2 - Failure! The first and second files couldn't be opened!
# 3 - Failure! The first file couldn't be opened!
# 4 - Failure! The second file couldn't be opened!
# 255 - Failure! You broke the script. Well done?


# First do our 'imports' or module loadings...
module load dawn > /dev/null 2>&1

# This script will take two arguments, which are files, and compare them. 
# If it will inform the user either way as to what happened.

# Get the file inputs from the console
fileOne="$1"
fileTwo="$2"

# Run h5ls to see if the file exists
fileOneCheck="$(h5ls "$fileOne" 2>&1)"
fileTwoCheck="$(h5ls "$fileTwo" 2>&1)"

# Do the check
if [ "$fileOneCheck" == "$fileOne: unable to open file" ] && [ "$fileTwoCheck" == "$fileTwo: unable to open file" ]
then
	echo "Can't open either of the files given in the two arguments"
	exit 2

elif [ "$fileOneCheck" == "$fileOne: unable to open file" ]
then
	echo "Can't open the file given in the first argument"
	exit 3

elif [ "$fileTwoCheck" == "$fileTwo: unable to open file" ]
then
	echo "Can't open the file given in the second argument"
	exit 4
fi

# Then set up some strings so that the comparison responses are uniform
successString="Success"
failureString="Failure"

# Compare the files, getting back the standard string
fileCompare=$(cmp --silent <(h5ls -d "$fileOne"/entry/result/data) <(h5ls -d "$fileTwo"/entry/result/data) && echo "$successString" || echo "$failureString")

# Do the appropriate action if the files are or are not equal and handling for crazy results too
if [ "$fileCompare" == "$successString" ]
then
	echo "Success! The files are the same!"
	exit 0
elif [ "$fileCompare" == "$failureString" ]
then
	echo "Failure! The files are not the same!"
	exit 1
else
	echo "Failure! Somehow you've broken this script"
	exit 255
fi
