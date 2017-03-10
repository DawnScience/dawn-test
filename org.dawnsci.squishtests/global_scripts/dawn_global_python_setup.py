source(findFile("scripts", "swt_toolitems.py"))

import os
import subprocess

#This is a wrapper to catch typos
def openPydevConsole(type="Python"):
	openPyDevConsole(type)

def openPyDevConsole(type="Python"):
    ''' Open a PyDev console waiting for the console to be fully open.
        WARNING: This code probably does not cope with opening two consoles
        at the same time and may not wait long enough for the second console'''
    openView("Console", matchOpen=True)
    # Explanation of the warning. The wait depends on certain events in the console. But
    # we don't have a great way to detect that those events we are waiting on aren't in
    # the previously launched console. What is probably needed is additional code
    # to detect the names of the existing consoles so that the new one can be detected  
    
    mouseClick(waitForSwtToolItem('Open Console'))
    activateItem(waitForObjectItem(":Pop Up Menu", "4 PyDev Console"))
    
    clickButton(waitForObject(":%s console_Button" % type))
    clickButton(waitForObject(":OK_Button"))
    
    # This is a bit difficult to know when we are fully ready, so we wait
    # for these two events to happen. 
    snooze(10)
    waitForSwtToolItem('Clear Console')
    waitForPrompt()
    
    # Finally activate the console so text can be sent to it
    # we do that by clicking in it 
    mouseClick(waitForObject(":PyDev Console"), 252, 66, 0, Button.Button1)
    # We type return so that the cursor ends up in the right place
    # see https://sw-brainwy.rhcloud.com/tracker/PyDev/237
    typeReturnAndWaitForPrompt()

def typeInConsole(text, object_name=":PyDev Console", prompt=">>> ", timeout=20000, wait=True):
    type(waitForObject(object_name), text)
    typeReturnAndWaitForPrompt(object_name=object_name, prompt=prompt, timeout=timeout, wait=wait)

def typeReturnAndWaitForPrompt(object_name=":PyDev Console", prompt=">>> ", timeout=20000, wait=True):
    type(waitForObject(object_name), "<Return>")
    if wait:
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

def setupPython(needScipy = False):
    waitForObject(":Workbench Window")
    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Preferences"))
    expand(waitForObjectItem(":Preferences_Tree", "PyDev"))
    # turn off automatic parentheses insertion as it plays havoc with the type commands
    expand(waitForObjectItem(":Preferences_Tree", "Editor"))
    mouseClick(waitForObjectItem(":Preferences_Tree", "Typing"))
    clickButton(waitForObject(":Preferences.Automatic parentheses insertion_Button"))

    # turn off all code completion too
    mouseClick(waitForObjectItem(":Preferences_Tree", "Code Completion"))
    clickButton(waitForObject(":Preferences.Use code completion?_Button"))
    clickButton(waitForObject(":Preferences.Use code completion on debug console sessions?_Button"))
    clickButton(waitForObject(":Preferences.Apply_Button"))

    expand(waitForObjectItem(":Preferences_Tree", "Interpreters"))
    mouseClick(waitForObjectItem(":Preferences_Tree", "Python Interpreter"))
    
    clickButton(waitForObject(":Preferences.Auto Config_Button"))
    
    # Wait for auto config list to come up
    multiOptions = waitFor('object.exists(":ListDialog_Shell")', 20000)
    multiOptions = multiOptions and object.exists(":Select Interpreter Available_Caption")
    multiOptions = multiOptions and object.exists(":Select Interpreter Available_Table")
    if multiOptions:
        availableList = object.children(waitForObject(":Select Interpreter Available_Table"))
        #We're not testing installations
        allowedList = filter(lambda x: "select to install" not in x.text, availableList)
        #We want to use anaconda
        anaList = filter(lambda x: "anaconda" in x.text, availableList)
        if len(anaList) != 0:
            allowedList = anaList
        #This is needed since the I07 (and other?) scripts sometimes rely on scipy.
        if needScipy:
            test.compare(allowedList, anaList, 'Suite requires either anaconda (or another scipy providing environment).')
            
        clickItem(waitForObject(":Select Interpreter Available_Table"), "%d/0" % allowedList[0].row, 5, 5)
        clickButton(waitForObject(":Select Interpreter Available_OK_Button"))

    _finishPythonSetup()
    test.passes("setupPython: Success")

def getPythonLocation():
    """Searches for full path to python executable
    'which' used to return full path of anaconda or just first python executable"""
    loc = None
    #New behaviour, return a path to a python interpreter
    #Thanks to M. Webber for this snippet
    whichRun = subprocess.Popen(('which','-a','python'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout, stderr) = whichRun.communicate(None)
    if not whichRun.returncode:
        spltout = stdout.split('\n')
        if 'anaconda' in stdout:
            for anaLoc in spltout:
                if 'anaconda' in anaLoc:
                    loc = anaLoc 
        else:
            loc = spltout[0]

    return loc

def setPyDevPref_ConnectToDebugSession(connect=True):
    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Preferences"))
    expand(waitForObjectItem(":Preferences_Tree", "PyDev"))
    mouseClick(waitForObjectItem(":Preferences_Tree", "Interactive Console"))
    connectDebug = waitForObject(":Preferences.Connect console to a Debug Session?_Button")
    current = connectDebug.getSelection()
    if current != connect:
        clickButton(connectDebug)
    clickButton(waitForObject(":Preferences.OK_Button"))


def toggleBreakpointAtLine(line):
    ''' Toggle the breakpoint at the given line number of the active file.
        Note this requires <Ctrl+Shift+b> to respond which does not work
        in all perspectives. e.g. Debug is a good one '''
    type(waitForObject(":Workbench Window"), "<Ctrl+l>")
    type(waitForObject(":Go to Line.Enter line number ...:_Text"), str(line))
    clickButton(waitForObject(":Go to Line.OK_Button"))
    type(waitForObject(":Workbench Window"), "<Ctrl+Shift+b>")

def getVariableNames():
    ''' Return a set of all the variable names visible in the Variables view
        Doing something like
          waitFor("getVariableNames() == set(['a', 'b', 'v'])")
        to test exact list of variables, or:
          waitFor("getVariableNames() >= set(['a', 'b'])")
        to check that at least the list of variables exists
     '''
    variableTree = waitForObject(":Variables_Tree")
    vNames = set()
    for row_i in range(variableTree.getItemCount()):
        vName = variableTree.getItem(row_i).getText(0)
        vNames.add(vName)
    return vNames

def getVariable(name):
    ''' Return the value of the named variable, or None if not found
     '''
    variableTree = waitForObject(":Variables_Tree")
    for row_i in range(variableTree.getItemCount()):
        vName = variableTree.getItem(row_i).getText(0)
        if vName == name:
            return variableTree.getItem(row_i).getText(1)
    return None
