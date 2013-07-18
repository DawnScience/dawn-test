#!/usr/bin/python2.6
import os,shutil,subprocess
queue = {'tst_suite': 'suite_workflows_general','tst_case':'tst_loop_example'}

print '/scisoft/jenkins/ub1004_jonathan/workspace/Dawn_squish_tests/org.dawnsci.squishtests/'+queue["tst_suite"]+'/shared/'
def check_variable():
    path_global_script='/scisoft/jenkins/ub1004_jonathan/workspace/Dawn_squish_tests/org.dawnsci.squishtests/'+queue["tst_suite"]+'/shared/scripts'
    if os.path.exists(path_global_script)== True:
        shutil.rmtree(path_global_script)         
    shutil.copytree('/scisoft/jenkins/ub1004_jonathan/workspace/Dawn_squish_tests/eu.esrf.test/global_script_esrf',path_global_script)
        
        
check_variable()

os.system('sh script_jenkins.sh')

#if test -z "$1" 
#then

#else 
    
 #   fi
