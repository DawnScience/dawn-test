source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))
source(findFile("scripts", "file_utils.py"))

def main():
    # This test should only run on Linux x86_64
    # use platform instead of os since os fails on windows
    import platform, sys
    if platform.uname()[0] != 'Linux' or platform.uname()[4] != 'x86_64':
        return

    startOrAttachToDAWN()

    addExternalFile("results_b21-2672_detector_040713_102411.nxs", "suite_ncd", "tst_ncd_model_builder", "data", "examples")
    openPerspective("NCD Model Builder Perspective")
    squishDirectory = createAndChangeToSquishtestsTempDirectory()
    sasDirectoryPrefixPattern = "EDApplicationSASPipeline*"
    deleteOldLogFiles(sasDirectoryPrefixPattern)

    expand(waitForObjectItem(":Project Explorer_Tree_2", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree_2", "examples"))
    r = waitForObjectItem(":Project Explorer_Tree_2", "results__b21-2672__detector__040713__102411.nxs")
    mouseClick(r, 186, 12, 0, Button.Button1)
    mouseClick(r, 186, 12, 0, Button.Button1)
    mouseClick(waitForObject(":Data parameters.Working directory_Text"), 144, 5, 0, Button.Button1)
    type(waitForObject(":Data parameters.Working directory_Text"), "<Ctrl+a>")
    type(waitForObject(":Data parameters.Working directory_Text"), squishDirectory)
    type(waitForObject(":Data parameters.Working directory_Text"), "<Ctrl+a>")
    type(waitForObject(":Data parameters.Working directory_Text"), "<Ctrl+c>")

    clickButton(waitForObject(":Data parameters.Run NCD model building_Button"))
    snooze(130)

    logfile = findLogFile(sasDirectoryPrefixPattern, 100)
    test.verify(logfile != None, "Existence of log file")

    import shutil
    shutil.rmtree(squishDirectory,ignore_errors=True)

    closeOrDetachFromDAWN()
