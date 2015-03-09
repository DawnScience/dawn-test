source(findFile("scripts", "swt_TabsCTabs.py"))

import glob, os, shutil
from datetime import datetime

DAWN_WORKSPACE_ROOT = os.environ.get('DAWN_WORKSPACE_ROOT',  "/scratch/workspace")
DAWN_SUITE_WORKSPACE= os.environ.get('DAWN_SUITE_WORKSPACE', "suite_test_single_workspace")
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
    

def startOrAttachToDAWNOnly(clean_workspace=True, copy_configuration_and_p2=False, vmArgs=None):
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

            if copy_configuration_and_p2:
                # We need the AUT directory, see squishrun_guest.{bat,sh} for when that is setup
                DAWN_ROOTS = glob.glob(os.environ['AUT_DIR'])
                if len(DAWN_ROOTS) != 1:
                    test.fail('Could not find exactly one DAWN_ROOT, "*%s" expands to %s' % (os.environ['AUT_DIR'], DAWN_ROOTS))
                DAWN_ROOT = DAWN_ROOTS[0]
                # Copy in p2 and configuration data
                os.makedirs(workparent)
                shutil.copytree(os.path.join(DAWN_ROOT, 'configuration'), osgi_configuration_area)
                shutil.copytree(os.path.join(DAWN_ROOT, 'p2'), os.path.join(workparent, 'p2'))

        start = datetime.now()
        
        # Make sure that we have args
        if not vmArgs:
            vmArgs = ""

        # On linux set set some things up
        # This is similar to module load dawn - TODO Could the AUT just be module load dawn/nightly?
        from sys import platform as _platform
        
        # We think this will not work at this point because
        # the shell needs to be set up in Squish job from Jenkins. 
        # However these are the things that need to be set from jenkins
        # We need to tell Matt Webber that these changes need to be made... 
        if _platform == "linux" or _platform == "linux2":
            os.system("export MALLOC_ARENA_MAX=4")
            os.system("gconftool-2 --type boolean --set /desktop/gnome/interface/menus_have_icons true")
            os.system("module unload use.own controls controls_rdb controls_dev vxworks/2.2 epics/3.14.11")
            os.system("module load python/ana")
            
            mailto=" -Duk.ac.diamond.scisoft.feedback.recipient=scisoftjira@diamond.ac.uk"
            xulfix=" -Dorg.eclipse.swt.browser.XULRunnerPath=/dls_sw/apps/xulrunner/64/xulrunner-1.9.2"
            usage=" -Dorg.dawnsci.usagedata.gathering.enabled=true -Dorg.dawnsci.usagedata.recording.ask=false"
            osgi_area=" -Dosgi.configuration.area=/tmp/squish/.dawn_osgi"
        
            vmArgs = mailto+xulfix+usage+osgi_area+" "+vmArgs
            
        # Expand the command
        cmd = "dawn -consoleLog -data %s -user %s -configuration %s -name %s-%s --launcher.appendVmargs -vmargs %s" % (workspace, osgi_user_area, osgi_configuration_area, suite_name, test_name, vmArgs)

        startApplication(cmd, "", -1, 90)
            
        end = datetime.now()
        test.log("Application took " + str(end-start) + " to start")
        
    window = waitForObject(":Workbench Window")
    window.setMaximized(True)
    # Let any setup items continue (e.g. Jython interpreter setup)
    # XXX This is a hack because we don't have a better way to determine if
    # the GUI is fully started
    snooze(1.0)
    test.passes("startOrAttachToDAWNOnly: Success")


def dismissWelcomeScreen():
    clickTab(waitForObject(":Welcome_CTabItem"), 10, 10, 0, Button.Button3)
    activateItem(waitForObjectItem(":Pop Up Menu", "Close"))
    test.passes("dismissWelcomeScreen: Success")

#Wrapper to correct typo.
def dismissWelcomScreen():
    dismissWelcomeScreen()

def startOrAttachToDAWN(copy_configuration_and_p2=False, vmArgs=None):
    startOrAttachToDAWNOnly(copy_configuration_and_p2=copy_configuration_and_p2, vmArgs=vmArgs)
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
        #Get the already open View and set it active with a mouse click
        #The viewRealObjectName is needed as the alreadyOpenView doesn't exist 
        #(although it's visible) - no idea why.
        alreadyOpenView = waitForFirstSwtCTabItem(item_text=viewName)
        viewRealObjectName = "{caption='%s' type='org.eclipse.swt.custom.CTabItem' window=':Workbench Window'}" % viewName;
        if object.exists(viewRealObjectName):
            mouseClick(alreadyOpenView)
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
    
def openAndClearErrorLog(errorsOnly=False):
    ''' Open and clear the Eclipse Error Log. Use getErrorItems() first to find out if there is
        anything in them '''
  
    if getErrorItems().length > 0:
        snooze(2)
        mouseClick(waitForObject(":Delete Log_ToolItem"))
        clickButton(waitForObject(":Confirm Delete.OK_Button"))
        
    if errorsOnly:
        mouseClick(waitForObject(":Workspace Log.View Menu_ToolItem"), 14, 14, 0, Button.Button1)
        activateItem(waitForObjectItem(":Pop Up Menu", "Filters..."))
        clickButton(waitForObject(":Event Types.OK_Button"))
        clickButton(waitForObject(":Event Types.Information_Button"))
        clickButton(waitForObject(":Event Types.Warning_Button"))
        clickButton(waitForObject(":Log Filters.OK_Button"))

  

def verifyAndClearErrorLog():
    ''' Verifies that the error log is empty and clears it if not '''
    if getErrorItems().length > 0:
        test.fail("Items are in error log view (if this test fails, see console output as -consoleLog is on)")
        mouseClick(waitForObject(":Delete Log_ToolItem"))
        clickButton(waitForObject(":Confirm Delete.OK_Button"))
    else:
        # provide a less verbose message when the test just passed
        test.passes("No items are in error log view")
