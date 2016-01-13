source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_global_python_setup.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))
source(findFile("scripts", "plotting_test.py"))
    
def main():
    
    #Start using clean workspace, open Python perspective with 
    #space for the console and setup python; switch on py4j automatically
    startOrAttachToDAWN(vmArgs='-DPREF_PY4J_ACTIVE=true')
    openPerspective("Data Browsing (default)")
    setupPython()
    
    #Open a python console
    openPyDevConsole()
    
    # Press the record macro button
    mouseClick(waitForFirstSwtToolItem('Record Macro'), 6, 12, 0, Button.Button1)
    
    # Open a data file
    openExample("metalmix.mca")
    
    #Need to give time for the macro to run through
    snooze(30)
    # Check that macro commands are there
    got = waitForObject(":PyDev Console").text
    test.verify("import numpy" in got, "Unable to find numpy command in macro recorded!")
    test.verify('ps = dnp.plot.getPlottingSystem("metalmix.mca")' in got, "The correct plotting system was not in the macro")
    closeOrDetachFromDAWN()
