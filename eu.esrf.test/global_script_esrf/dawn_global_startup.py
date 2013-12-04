import os, shutil
from datetime import datetime
DAWN_WORKSPACE_ROOT=os.path.join(os.environ['WORKSPACE'],"eu.esrf.test/dawn_workspace")
DAWN_SUITE_WORKSPACE="suite_test_single_workspace"
USE_ATTACH=False

testSettings.logScreenshotOnFail = True
testSettings.logScreenshotOnError = True



def startDAWNSuiteWorkspace():

    # We start each test in a new workspace
    cwd = os.getcwd()
    parent_path, test_name = os.path.split(cwd)
    suite_name = os.path.basename(parent_path)
    workspace = "%s/%s/%s" % (DAWN_WORKSPACE_ROOT, suite_name, DAWN_SUITE_WORKSPACE)
    
    start = datetime.now()
    startApplication("dawn -consoleLog -data %s" % workspace, "", -1, 90)
    end = datetime.now()
    
    test.log("Application took " + str(end-start) + " to start")
    
    window = waitForObject(":Workbench Window")
    window.setMaximized(True)
    # Let any setup items continue (e.g. Jython interpreter setup)
    # XXX This is a hack because we don't have a better way to determine if
    # the GUI is fully started
    snooze(1.0)
    test.passes("startOrAttachToDAWNOnly: Success")
    
    try:
        #find should fail fast if no welcome screen
        findObject(":Welcome_CTabItem")
        dismissWelcomScreen()
    except:
        pass
    

def startOrAttachToDAWNOnly(clean_workspace=True):
    if USE_ATTACH:
        attachToApplication("attachable_dawn")
    else:
        # We start each test in a new workspace
        cwd = os.getcwd()
        parent_path, test_name = os.path.split(cwd)
        suite_name = os.path.basename(parent_path)
        workparent = os.path.join(DAWN_WORKSPACE_ROOT, suite_name, test_name)
        workspace = os.path.join(workparent, 'workspace')
        osgi_user_area = os.path.join(workparent, 'osgi_user_area')
        osgi_configuration_area = os.path.join(workparent, 'osgi_configuration_area')
        if clean_workspace:
            try:
                shutil.rmtree(workparent)
            except OSError:
                # Ignore error here, check below
                # that directory is gone
                pass
            snooze(1)
            test.verify(not os.path.exists(workparent), "startOrAttachToDAWNOnly: Workspace is clean")
        
        start = datetime.now()
        startApplication("dawn -consoleLog -data %s -user %s -configuration %s -name %s-%s" %
                         (workspace, osgi_user_area, osgi_configuration_area, suite_name, test_name), "", -1, 90)
        end = datetime.now()
        test.log("Application took " + str(end-start) + " to start")
        
    window = waitForObject(":Workbench Window")
    window.setMaximized(True)
    # Let any setup items continue (e.g. Jython interpreter setup)
    # XXX This is a hack because we don't have a better way to determine if
    # the GUI is fully started
    snooze(1.0)
    test.passes("startOrAttachToDAWNOnly: Success")

def dismissWelcomScreen():
    clickTab(waitForObject(":Welcome_CTabItem"), 10, 10, 0, Button.Button3)
    activateItem(waitForObjectItem(":Pop Up Menu", "Close"))
    test.passes("dismissWelcomScreen: Success")

def startOrAttachToDAWN():
    startOrAttachToDAWNOnly()
    dismissWelcomScreen()
    test.passes("startOrAttachToDAWN: Success")
    
def closeDAWN():
    closeWindow(":Workbench Window")
    clickButton(waitForObject(":Confirm Exit.OK_Button"))
    test.passes("closeDAWN: Success")
    
def closeOrDetachFromDAWN():
    if USE_ATTACH:
        # nothing to do
        pass
    else:
        closeDAWN()
    test.passes("closeOrDetachFromDAWN: Success")
    
def openPerspective(perspectiveName):
    waitForObject(":Workbench Window")
    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Open Perspective"))
    activateItem(waitForObjectItem(":Open Perspective_Menu", "Other..."))
    mouseClick(waitForObject("{caption='%s' column='0' container=':Open Perspective_Table' type='com.froglogic.squish.swt.TableCell'}" % perspectiveName), 5, 5, 0, Button.Button1)
    mouseClick(waitForObject(":Open Perspective.OK_Button"))
    # Opening a perspective can (more than most) kick off things in the background
    # This background processing can make the workbench window appear fully ready
    # but the perspective isn't. Therefore we snooze a few seconds to let everything
    # catchup 
    waitForObject(":Workbench Window")
    snooze(3.0)
    waitForObject(":Workbench Window")
    test.passes("openPerspective: %s" % perspectiveName)

def openView(viewName, matchOpen=False):
    ''' Open the view named viewName. If matchOpen is true, will assume that an open view with 
        viewName in the title bar of the view is the expected one and only activate it '''
    waitForObject(":Workbench Window")
    if matchOpen:
        viewRealObjectName = "{caption='%s' type='org.eclipse.swt.custom.CTabItem' window=':Workbench Window'}" % viewName;
        if object.exists(viewRealObjectName):
            mouseClick(waitForObject(viewRealObjectName))
            test.passes("openView (matchOpen): %s" % viewName)
            return
    
    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Show View"))
    activateItem(waitForObjectItem(":Show View_Menu", "Other..."))
    type(waitForObject(":Show View_Text"), viewName)
    mouseClick(waitForObjectItem(":Show View_Tree", viewName))
    mouseClick(waitForObject(":Show View.OK_Button"))
    waitForObject(":Workbench Window")
    test.passes("openView: %s" % viewName)


    
def getErrorItems():
    ''' Return the Java Array that contains the list of entries in the Error Log '''
    openView("Error Log", True)
    errorTree = waitForObject(":Error Log_Tree")
    return errorTree.getItems()
    
def openAndClearErrorLog():
    ''' Open and clear the Eclipse Error Log. Use getErrorItems() first to find out if there is
        anything in them '''
    if getErrorItems().length > 0:
        snooze(2)
        mouseClick(waitForObject(":Delete Log_ToolItem"))
        clickButton(waitForObject(":Confirm Delete.OK_Button"))

def verifyAndClearErrorLog():
    ''' Verifies that the error log is empty and clears it if not '''
    if getErrorItems().length > 0:
        test.fail("Items are in error log view (if this test fails, see console output as -consoleLog is on)")
        mouseClick(waitForObject(":Delete Log_ToolItem"))
        clickButton(waitForObject(":Confirm Delete.OK_Button"))
    else:
        # provide a less verbose message when the test just passed
        test.passes("No items are in error log view")
