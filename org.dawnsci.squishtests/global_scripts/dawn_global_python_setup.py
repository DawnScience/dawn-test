EPD_FREE_LOCATIONS=[
  'C:\\Python27\\python.exe', 
  'C:\\Python26\\python.exe',
  'C:\\scratch\\epd_free\\python.exe', 
  '/home/tester/epd_free/bin/python', 
  '/scratch/epd_free/bin/python']

# Add in the current home directory as a place to look for EPD
# free. This doesn't really apply to the test vm machines
# but it can make local development of the tests easier
import os
home = os.getenv("HOME")
if home is not None:
     EPD_FREE_LOCATIONS.append("%s/epd_free/bin/python" % home)



def openPyDevConsole(type="Python"):
    ''' Open a PyDev console waiting for the console to be fully open.
        WARNING: This code probably does not cope with opening two consoles
        at the same time and may not wait long enough for the second console'''
    # Explanation of the warning. The wait depends on certain events in the console. But
    # we don't have a great way to detect that those events we are waiting on aren't in
    # the previously launched console. What is probably needed is additional code
    # to detect the names of the existing consoles so that the new one can be detected  
    mouseClick(waitForObject(":Open Console_ToolItem"))
    activateItem(waitForObjectItem(":Pop Up Menu", "5 PyDev Console"))
    clickButton(waitForObject(":%s console_Button" % type))
    clickButton(waitForObject(":OK_Button"))
    
    # This is a bit difficult to know when we are fully ready, so we wait
    # for these two events to happen. 
    waitForObject(":Clear Console_ToolItem")
    waitForPrompt()
    
    # Finally activate the console so text can be sent to it
    # we do that by clicking in it 
    mouseClick(waitForObject(":PyDev Console"), 252, 66, 0, Button.Button1)

def typeInConsole(text, object_name=":PyDev Console", prompt=">>> ", timeout=20000):
    type(waitForObject(object_name), text)
    typeReturnAndWaitForPrompt(object_name=object_name, prompt=prompt, timeout=timeout)

def typeReturnAndWaitForPrompt(object_name=":PyDev Console", prompt=">>> ", timeout=20000):
    type(waitForObject(object_name), "<Return>")
    waitForPrompt(object_name=object_name, prompt=prompt, timeout=timeout)

def waitForPrompt(object_name=":PyDev Console", prompt=">>> ", timeout=20000):
    '''Wait for the prompt on the interactive console'''
    console_object=waitForObject(object_name)
    if not waitFor('console_object.text.endswith("%s")' % (prompt), timeout):
        raise LookupError
    
def _finishPythonSetup():
    clickButton(waitForObject(":Selection needed.OK_Button"))

    # All done, close preferences
    clickButton(waitForObject(":Preferences.OK_Button"))
    # It can take a while to configure interpreter, so wait until
    # the workbench window is ready again
    # On windows vm this can take forever! So wait 300 seconds
    waitForObject(":Workbench Window", 300000)    

def setupEPDPython():
    waitForObject(":Workbench Window")
    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Preferences"))
    expand(waitForObjectItem(":Preferences_Tree", "PyDev"))
    mouseClick(waitForObjectItem(":Preferences_Tree", "Interpreter - Python"))
    mouseClick(waitForObject(":Preferences.New..._Button"))
    type(waitForObject(":Select interpreter.Interpreter Name: _Text"), "EPD Free Python")
    found = False
    for loc in EPD_FREE_LOCATIONS:
        if os.path.exists(loc):
            type(waitForObject(":Select interpreter.Interpreter Executable: _Text"), "<Ctrl+a>")
            type(waitForObject(":Select interpreter.Interpreter Executable: _Text"), loc)
            if len(waitForObject(":Select interpreter Error Message_Text").text) == 0:
                # found a good one
                test.verify(True, "setupEPDPython: Using %s as EPD Free Python" % loc)
                found = True
                break
    if found:
        clickButton(waitForObject(":Select interpreter.OK_Button"))
        _finishPythonSetup()
    else:
        test.passes("setupEPDPython: No installed EPD found, deferring to setupPython")
        # We failed to find installed EPD, so try and install it now
        clickButton(waitForObject(":Select interpreter.Cancel_Button"))
        clickButton(waitForObject(":Preferences.Cancel_Button"))
        setupPython(installEPD=True)
    test.passes("setupEPDPython: Success")
        

def setupPython(allowInstallEPD=False, installEPD=False, installEPDPath=None):
    waitForObject(":Workbench Window")
    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Preferences"))
    expand(waitForObjectItem(":Preferences_Tree", "PyDev"))
    mouseClick(waitForObjectItem(":Preferences_Tree", "Interpreter - Python"))
    clickButton(waitForObject(":Preferences.Auto Config_Button"))
    
    # Wait for auto config list to come up
    autoError = waitForObject(":Unable to auto-configure..OK_Button", 100)
    if (autoError!=None):
        clickButton(autoError)
        clickButton(waitForObject(":Preferences.New..._Button"))
        type(waitForObject(":Select interpreter.Interpreter Name: _Text"), "EPD Free Python")
        type(waitForObject(":Select interpreter.Interpreter Executable: _Text"), "C:\\Python26\\python.exe")
        clickButton(waitForObject(":Select interpreter.OK_Button"))
        clickButton(waitForObject(":Selection needed.OK_Button"))
        clickButton(waitForObject(":Preferences.OK_Button", 120000))
        return

    # Wait for auto config list to come up
    multiOptions = waitFor('object.exists(":ListDialog_Shell")', 20000)
    multiOptions = multiOptions and object.exists(":Select Interpreter Available_Caption")
    multiOptions = multiOptions and object.exists(":Select Interpreter Available_Table")
    if multiOptions:
        availableList = object.children(waitForObject(":Select Interpreter Available_Table"))
        if installEPD:
            allowedList = filter(lambda x: "EPD" in x.text and "select to install" in x.text, availableList)
        else:
            allowedList = filter(lambda x: "select to install" not in x.text, availableList)
        
        test.verify(len(allowedList) == 1, "setupPython: Filter to one available Python to Auto Config")
            
        clickItem(waitForObject(":Select Interpreter Available_Table"), "%d/0" % allowedList[0].row, 5, 5)
        clickButton(waitForObject(":Select Interpreter Available_OK_Button"))

    # In the case that there is no Python autofound, allow install of EPD
    # This only applies if the selection interpreter list dialog isn't shown
    elif allowInstallEPD and waitFor('object.exists(":Enthought EPD Free Installer_Label")', 20000):
        installEPD = True

    if installEPD:
        test.verify(object.exists(":Enthought EPD Free Installer_Label"), "setupPython: Enthought Installer Wizard open (if this fails it is because the Enthought wizard didn't open)")
        test.verify(object.exists(":I accept the terms of the license agreement_Button"), "setupPython: License agreement open")
        clickButton(waitForObject(":I accept the terms of the license agreement_Button", 1))
        clickButton(waitForObject(":Next >_Button"))
        
        if installEPDPath is not None:
            type(waitForObject(":Install to:_Text"), installEPDPath)
        clickButton(waitForObject(":Close wizard automatically on successful installation._Button"))
        clickButton(waitForObject(":Finish_Button"))
        # Wait up to 5 minutes for the wizard to finish
        # There is a case here to add event driven check so that if there
        # is an unexpected failure we don't wait so long
        waitForObject(":Selection needed.OK_Button", 300000)

    _finishPythonSetup()
    test.passes("setupPython: Success")

def getPythonLocation():
    for loc in EPD_FREE_LOCATIONS:
        if os.path.exists(loc):
            return loc
    return None
