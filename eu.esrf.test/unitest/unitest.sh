 #! /usr/bin/env sh
echo $WORKSPACE/eu.esrf.test/src/scriptFunction
### unitTest.sh ###

#source /scisoft/jenkins/ub1204_opid23_test/dawn-test/eu.esrf.test/src/scriptFunction
source $WORKSPACE/eu.esrf.test/src/scriptFunction
#test the function findDisplayNumber with a temp file belonged to the user
function testWithTmp () {
	mkdir 'tmpFile'
	chmod -R 775 tmpFile
	cd tmpFile
	touch .X2-lock
	cd ..
	ssh opid29@ub1204 "touch $WORKSPACE/eu.esrf.test/unitest/tmpFile/.X0-lock;touch $WORKSPACE/eu.esrf.test/unitest/tmpFile/.X1-lock;touch $WORKSPACE/eu.esrf.test/unitest/tmpFile/.X4-lock;"
	val=$(findDisplayNumber tmpFile/)
	rm -rf tmpFile
	assertEquals '2' $val
}

#test the function findDisplayNumber with no temp file belonged to the user
function testwithNoTmpUser () {
	mkdir 'tmpFile'
	chmod -R 775 tmpFile
	cd tmpFile
	cd ..
	ssh opid29@ub1204 "touch $WORKSPACE/eu.esrf.test/unitest/tmpFile/.X0-lock;touch $WORKSPACE/eu.esrf.test/unitest/tmpFile/.X1-lock;touch $WORKSPACE/eu.esrf.test/unitest/tmpFile/.X2-lock;touch $WORKSPACE/eu.esrf.test/unitest/tmpFile/.X4-lock"
	val1=$(findDisplayNumber tmpFile/)
	rm -rf tmpFile
	assertEquals '3' $val1
}

function testwithOneTmpbelongRoot () {
	mkdir 'tmpFile'
	chmod -R 775 tmpFile
	cd tmpFile
	cd ..
	ssh opid29@ub1204 "touch $WORKSPACE/eu.esrf.test/unitest/tmpFile/.X0-lock"
	val1=$(findDisplayNumber tmpFile/)
	rm -rf tmpFile
	assertEquals '1' $val1
}

function testwithEmptyFolder () {
	mkdir 'tmpFile'
	chmod -R 775 tmpFile
	cd tmpFile
	cd ..
	val1=$(findDisplayNumber tmpFile/)
	rm -rf tmpFile
	assertEquals '0' $val1
}


. "$WORKSPACE/eu.esrf.test/src/shunit2-2.1.6/src/shunit2"



