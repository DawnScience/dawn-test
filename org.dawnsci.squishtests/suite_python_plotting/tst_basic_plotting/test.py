source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_global_python_setup.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))
source(findFile("scripts", "plotting_test.py"))
    
def main():
    
    #Start using clean workspace, open Python perspective with 
    #space for the console and setup python
    startOrAttachToDAWN()
    openPerspective("Python")
    setupPython()
    
    #Get the plotting system and open a Jython console
    system = getPlottingSystem("Plot 1")
    openPyDevConsole()
    
    plotting_script_test(system)
    
    closeOrDetachFromDAWN()