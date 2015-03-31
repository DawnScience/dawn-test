source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))
source(findFile("scripts", "file_utils.py"))
import os, platform, sys


def main():
    # This test should only run on Linux x86_64
    # use platform instead of os since os fails on windows
    if platform.uname()[0] != 'Linux' or platform.uname()[4] != 'x86_64':
        return

    startOrAttachToDAWN()
    
    openPerspective("NCD Model Builder Perspective")

    clickTab(waitForSwtCTabItem("File Navigator"), 57, 14, 0, Button.Button1)
#    clickTab(waitForObject(":File Navigator_CTabItem"), 57, 14, 0, Button.Button1)
    navTree = waitForTreeWithItem("dls")
    expand(waitForObjectItem(navTree, "dls"))
    expand(waitForObjectItem(navTree, "b21"))
    expand(waitForObjectItem(navTree, "data"))
    expand(waitForObjectItem(navTree, "2013"))
    expand(waitForObjectItem(navTree, "cm5947-3"))
    expand(waitForObjectItem(navTree, "processing"))
    
    #Working directory needs to have a short name
    workingDir = createAndChangeToSquishtestsTempDirectory()
    
    #Get the file widget and click on it twice (not double click!) to load
    ncdFileWidget = get_swt_tree_item(navTree, ["dls", "b21", "data", "2013", "cm5947-3", "processing", "results_b21-2672_detector_040713_102411.nxs"], file = True, fsTree = True)
    mouseClick(waitForObject(ncdFileWidget), 40, 8, 0, Button.Button1)
    mouseClick(waitForObject(ncdFileWidget), 40, 8, 0, Button.Button1)
    
    #Activate the tool and set working directory
    clickTab(waitForSwtCTabItem("BioSAXS Model Builder"), 92, 13, 0, Button.Button1)
    workDirTextBox = waitForSwtTextWithLabel("Working directory")
    mouseClick(waitForObject(workDirTextBox), 144, 5, 0, Button.Button1)
    type(waitForObject(workDirTextBox), "<Ctrl+a>")
    type(waitForObject(workDirTextBox), "<Delete>")
    type(waitForObject(workDirTextBox), workingDir)
    type(waitForObject(workDirTextBox), "<Ctrl+a>")
    type(waitForObject(workDirTextBox), "<Ctrl+c>")
    
    #Set the directory label and ensure no old logs present
    sasDirectoryPrefixPattern = "EDApplicationSASPipeline*"
    deleteOldLogFiles(sasDirectoryPrefixPattern)

    type(waitForObject(":Data parameters.HTML results directory_Text"), "<Ctrl+v>")
    clickButton(waitForObject(":Data parameters.Run NCD model building_Button"))
    snooze(130)

    logfile = findLogFile(sasDirectoryPrefixPattern, 100, workingDir=workingDir)
    test.verify(logfile != None, "Found logfile.")
    pipelineOut = findFileInTree(workingDir, "pipelineResults*", dirMasks=[sasDirectoryPrefixPattern, 'ControlSolutionScattering*'])
    test.verify(pipelineOut != None, "Found pipelineResults.html (shown to user).")

    os.removedirs(workingDir)

    closeOrDetachFromDAWN()
