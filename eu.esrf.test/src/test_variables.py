#!/usr/bin/python2.6 
import os,shutil 
queue = {'suite_workflows_general': {'tst_case':'tst_open_examples'}} 
#only one queue allowed for one suite_test_case 
#queue = {'suite_workflows_general': {'tst_case2':'tst_open_examples'}} 
#queue.update({'suite_usecases_general':{'tst_case':'tst_hdf5_large_tree'}}) 
#queue.update({'suite_workflows_bignexus':{'tst_case':'tst_slicedata_dbrowsing'}}) 
#queue['suite_workflows_bignexus'] = {'tst_case':'tst_slicedata_dexplore'} 
   
    
def check_variable(testSuiteName): 
    path_global_script=os.path.join(os.environ['WORKSPACE'],'org.dawnsci.squishtests',testSuiteName,'shared/scripts') 
    if os.path.exists(path_global_script)== True: 
        shutil.rmtree(path_global_script)          
    shutil.copytree(os.path.join(os.environ['WORKSPACE']  +'/eu.esrf.test/global_script_esrf') ,path_global_script) 
            
def setup_log(): 
    path_log=os.path.join(os.environ['WORKSPACE']  +'/log/') 
    if os.path.exists(path_log)== True: 
        shutil.rmtree(path_log) 
    os.mkdir(path_log) 
 
setup_log() 
#launch all the tests
for testSuiteName in queue.keys(): 
    check_variable(testSuiteName) 
    for tst in queue[testSuiteName]: 
        os.chdir(os.path.join(os.environ['WORKSPACE'],'eu.esrf.test/src')) 
        os.popen("./script_jenkins "+testSuiteName+" "+queue[testSuiteName][tst], "r").read()
