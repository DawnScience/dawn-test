source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))
source(findFile("scripts", "file_utils.py"))
import os, platform, shutil, sys

def main():
    # This test should only run on Linux x86_64
    # use platform instead of os since os fails on windows
    if platform.uname()[0] != 'Linux' or platform.uname()[4] != 'x86_64':
        raise Exception("Wrong CPU architecture! This test must be run on x86_64.")
        return

    startOrAttachToDAWN()
    
    openPerspective("NCD Model Builder Perspective")
    #New project must not have spaces in name!
    createProject("NCDModelBuilder", projectType="Data Project (empty or with example data)")
    createFolder("NCDModelBuilder", "NCDTest")
    
    #Add the test file and open it in the model builder
    ncdTestFilePath = addExternalFile("results_b21-2672_detector_040713_102411.nxs", 
                                      "suite_ncd", "tst_ncd_model_builder", "NCDModelBuilder", "NCDTest")
    #Working directory needs to have a short name (use the created project+folder and the test fails)
    workingDir = createAndChangeToSquishtestsTempDirectory()
    
    #Get the file explorer tree and expand down to the added file.
    tree = waitForTreeWithItem("NCDModelBuilder")
    expand(waitForObjectItem(tree, "NCDModelBuilder"))
    expand(waitForObjectItem(tree, "NCDTest"))
    
    #Get the file widget and click on it twice (not double click!) to load
    ncdFileWidget = get_swt_tree_item(tree, ["NCDModelBuilder", "NCDTest", "results_b21-2672_detector_040713_102411.nxs"], file = True)
    mouseClick(ncdFileWidget, 186, 12, 0, Button.Button1)
    mouseClick(ncdFileWidget, 186, 12, 0, Button.Button1)
    
    #Make sure the 
    clickTab(waitForSwtCTabItem("BioSAXS Model Builder"), 92, 13, 0, Button.Button1)
    workDirTextBox = waitForSwtTextWithLabel("Working directory")
    mouseClick(waitForObject(workDirTextBox), 144, 5, 0, Button.Button1)
    type(waitForObject(workDirTextBox), "<Ctrl+a>")
    type(waitForObject(workDirTextBox), "<Delete>")
    type(waitForObject(workDirTextBox), workingDir)
    
    #Make sure we have a
    sasDirectoryPrefixPattern = "EDApplicationSASPipeline*"
    deleteOldLogFiles(sasDirectoryPrefixPattern, workingDir=workingDir)#For testing...
    
    #Kick off the run & wait.
    clickButton(waitForObject(":Data parameters.Run NCD model building_Button"))
    snooze(130)

    logfile = None
    logfile = findLogFile(sasDirectoryPrefixPattern, 100, workingDir=workingDir)
    test.verify(logfile != None, "Found logfile.")
    pipelineOut = findFileInTree(workingDir, "pipelineResults*", dirMasks=[sasDirectoryPrefixPattern, 'ControlSolutionScattering*'])
    test.verify(pipelineOut != None, "Found pipelineResults.html (shown to user).")
    
    shutil.rmtree(workingDir, ignore_errors=True)

    closeOrDetachFromDAWN()
