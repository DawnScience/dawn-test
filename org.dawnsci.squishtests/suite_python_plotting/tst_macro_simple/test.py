source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_global_python_setup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))
source(findFile("scripts", "plotting_test.py"))

    
def main():
    
    #Start using clean workspace, open Python perspective with 
    #space for the console and setup python; switch on py4j automatically
    startOrAttachToDAWN(vmArgs='-DPREF_PY4J_ACTIVE=true')
    openPerspective("Data Browsing (default)")
    createConsoleSpace(perspective="Data Browsing (default)")
    setupPython()
    
    #Open a python console
    openPydevConsole(perspective="Data Browsing (default)")
    #As of 1.8, console slow to start on ws131
    snooze(30)
    
    # Press the record macro button
    mouseClick(waitForObject(":Record Macro_ToolItem_2"), 6, 12, 0, Button.Button1)
    
    # Open a data file
    openExample("metalmix.mca")
    
    # Check that macro commands are there
    got = waitForObject(":PyDev Console").text
    test.verify("import numpy" in got, "Unable to find numpy command in macro recorded!")
    test.verify('ps = dnp.plot.getPlottingSystem("metalmix.mca")' in got, "The correct plotting system was not in the macro")
    closeOrDetachFromDAWN()
