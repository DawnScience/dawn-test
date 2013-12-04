#!/usr/bin/env python 
import os,sys,re,time 

logpath= os.path.join(os.environ['WORKSPACE'],'log/')


listing = os.listdir(logpath)    
 
time= time.strftime('%d_%m_%y(%H:%M)',time.localtime())   

        
for infile in sorted(listing): 

    f = open(os.path.join(logpath,infile)) 
    strData = f.read() 
    f.close() 
    listLines = strData.split("\n") 
    total_error=False 
    error=False 
    log_error = "" 
    for line in listLines: 
        var_nb=0 
        nb_error_tst=0       
        test_error=0 
        if re.compile('START_TEST_CASE').search(line):          
            var =(re.findall('\(\w+\)', line)[0]) 
            tst=(re.findall('\w+', var)[0]) 
           
        if re.compile('Number of Errors:').search(line): 
            #logfile.write(infile) 
            #logfile.write("\n")                  
            nb_error_tst =int(re.findall('\d+', line)[0]) 
            if nb_error_tst>0:             
                log_error=log_error+"** "+tst+ " // number of error(s) = " + str(nb_error_tst)+"\n"   
                error=True 
        test_error=test_error+nb_error_tst 
 
        
if error == False: 
    print "************************" 
    print "** Squish Test passed **" 
    print "************************" 
    sys.exit(0) 
else: 
    print "************************" 
    print "** Squish Test failed **" 
    #print str(var_nb) + " Error(s)" 
    print log_error 
    print "************************" 
    sys.exit(1) 
 
 
