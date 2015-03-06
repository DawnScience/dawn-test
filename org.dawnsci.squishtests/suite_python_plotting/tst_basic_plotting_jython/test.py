source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_global_python_setup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))
source(findFile("scripts", "plotting_test.py"))
    
def main():
    
    #Start using clean workspace and open Python perspective with
    #space for the console
    startOrAttachToDAWN()
    openPerspective("Python")
    createConsoleSpace()

    #Get the plotting system and open a Jython console
    system = getPlottingSystem("Plot 1")
    openPyDevConsole(type="Jython")
    
    counter = 0
    while (not object.exists(":PyDev Console")):
        if (counter < 50):
            snooze(2)
            counter +=1
        else:
            test.fatal("time out waiting for console")
            closeOrDetachFromDAWN()
            return
    
    got = waitForObject(":PyDev Console").text
    ready = False
    counter = 0
    
    while (not got.endswith("\n>>> ") or not ready):
        ready = got.endswith("\n>>> ")
        snooze(2)
        got = waitForObject(":PyDev Console").text
        if (counter > 50):
            test.fatal("Console did not initialize")
            closeOrDetachFromDAWN()
            return
        counter +=1
    
    plotting_script_test(system)
    
    closeOrDetachFromDAWN()