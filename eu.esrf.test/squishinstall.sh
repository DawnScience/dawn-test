#!/bin/bash
set -o posix # posix mode so that error setting inherit to subshells
set -eux # error, unset and echo


# Options
export AUT_NAME=dawn
export AUT_DIR=/scisoft/jenkins/dawn/master_nightly/linux_x64/dawn
echo "WORKSPACE", ${WORKSPACE:="./WORKSPACE"}
echo "AUT_NAME=${AUT_NAME}"
echo "DISPLAY", ${DISPLAY:=":0.0"}\

export JREDIR=/sware/isdd/soft/java/v7u40/linux_x64/jdk1.7.0_40/jre


# Install squish in the Guest, $1 should be guest's JRE directory, $2 the aut name, $3 aut directory
# Sets SQUISHDIR (essentially as return)
function install_squish()
{
  echo "`date +"%a %d/%b/%Y %H:%M:%S"` install_squish start"
  local jredir=$1
  local aut_name=$2
  local aut_dir=$3
  local java="${jredir}/bin/java"

  unzip -q -d $WORKSPACE/tempsquish /scisoft/jenkins/Squish_SourceFiles/squish.zip
  : Remove version from folder name
  mv $WORKSPACE/tempsquish/* $WORKSPACE/squish
  rmdir $WORKSPACE/tempsquish

  ## Setup squish
  # This is essentially the command that is run by the UI setup in Squish to create the magic squishrt.jar
  SQUISHDIR="$WORKSPACE/squish"
  local squishserver="$SQUISHDIR/bin/squishserver"
  java_version=`"$java" -version 2>&1 | grep 'java version' | sed '-es,[^"]*"\([^"]*\)",\1,'`
  echo "`date +"%a %d/%b/%Y %H:%M:%S"` install_squish FixMethod"
  "$java" \
    -classpath "${SQUISHDIR}/lib/squishjava.jar:${SQUISHDIR}/lib/bcel.jar" \
    com.froglogic.squish.awt.FixMethod \
    "${jredir}/lib/rt.jar:${SQUISHDIR}/lib/squishjava.jar" \
    "${SQUISHDIR}/lib/squishrt.jar"

  cp "/scisoft/sware_isdd/src/squish/.squish-3-license" ~/.squish-3-license
  $squishserver --config setJavaVM "$java" 
  $squishserver --config setJavaVersion "$java_version"
  $squishserver --config setJavaHookMethod "jvm"
  $squishserver --config setLibJVM "`find $jredir -name libjvm.so | head -1`"
  $squishserver --config addAUT "$aut_name" "$aut_dir"
  $squishserver --config setAUTTimeout 120
  echo "`date +"%a %d/%b/%Y %H:%M:%S"` install_squish end"
}

: Setup Squish
if !([ -d "$WORKSPACE/squish" ]); 
  then
  install_squish $JREDIR $AUT_NAME $AUT_DIR
  else
  echo "*****************************"
  echo "************ALREADY EXIST*****************"
  echo "*****************************"
fi



