#!/usr/bin/python2.6
import os,re,sys
f = open(os.environ['WORKSPACE']  +'/squishlog')
strData = f.read()
f.close()
listLines = strData.split("\n")
for line in listLines:
	if re.compile('Number of Errors:').search(line):
		var_nb = re.findall('\d+', line)[0]
if int(var_nb) == 0:
	print "Test passed "
	sys.exit(0)
else:
	print "Test failed"
	print "Number of error ="+ var_nb
	sys.exit(1)
	
