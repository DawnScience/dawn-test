source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_python_setup.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "plotting_test.py"))

import os
import shutil

def _getAnacondaInstallPath():
    # Install alongside (not inside) workspace
    return os.path.join(getWorkspaceParent(), "anacondaInstallTestLocation")

def _finishPythonSetup():
    # Say yes to adding selected new paths to PYTHONPATH
    clickButton(waitForObject(":Selection needed.OK_Button"))
    
    # All done, close preferences
    clickButton(waitForObject(":Preferences.OK_Button"))
    # It can take a while to configure interpreter, so wait until
    # the workbench window is ready again
    # On windows vm this can take forever! So wait 300 seconds
    waitForObject(":Workbench Window", 300000)    
    
def setupAnaconda():
    
    # Open up preferences window and select PyDev->Interpreters->Python Interpreter
    waitForObject(":Workbench Window")
    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Preferences"))
    expand(waitForObjectItem(":Preferences_Tree", "PyDev"))
    expand(waitForObjectItem(":Preferences_Tree", "Interpreters"))
    mouseClick(waitForObjectItem(":Preferences_Tree", "Python Interpreter"))
    
    # Hit "Autoconfig"
    clickButton(waitForObject(":Preferences.Auto Config_Button", 30000))
    
    waitFor('object.exists(":ListDialog_Shell")', 20000)
    
    # Verfify Anaconda install option is available
    test.verify(object.exists(":Anaconda_Label"), "setupAnaconda: Anaconda Installer Wizard open (if this fails it is because the Anaconda wizard didn't open)")

    clickButton(waitForObject(":Select Interpreter Available_OK_Button"))
    
    # Anaconda wizard is launched; step through
    test.verify(object.exists(":I accept the terms of the license agreement_Button"), "setupPython: License agreement open")
    clickButton(waitForObject(":I accept the terms of the license agreement_Button", 1))
    clickButton(waitForObject(":Next >_Button"))
    type(waitForObject(":Install to:_Text"), "<Ctrl+a>")
    type(waitForObject(":Install to:_Text"), "<Delete>")
    
    # Replace default location with our install location above and finish
    type(waitForObject(":Install to:_Text"), _getAnacondaInstallPath())
    clickButton(waitForObject(":Close wizard automatically on successful installation._Button"))
    clickButton(waitForObject(":Finish_Button"))
    
    # Wait for 20 minutes *THIS IS A GUESS!*
    waitFor('object.exists(":Selection needed.OK_Button")', 1200000)
    
    _finishPythonSetup()
        
    test.passes("setupPython: Success")
    
def main():
    
    # Start using clean workspace, open Python perspective with 
    # space for the console and setup python
    startOrAttachToDAWN()
    openPerspective("Python")
    createToolSpace(viewTabName="Console", direction="up", steps=15)
    setupAnaconda()
    
    # Get the plotting system and open a Python console
    system = getPlottingSystem("Plot 1")
    openPyDevConsole()
    
    # Run our standard plotting tests
    plotting_script_test(system)
    
    closeOrDetachFromDAWN()
    

    