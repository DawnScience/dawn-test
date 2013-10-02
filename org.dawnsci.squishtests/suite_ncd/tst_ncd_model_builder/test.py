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
    createAndChangeToSquishtestsTempDirectory()
    sasDirectoryPrefixPattern = "EDApplicationSASPipeline*"
    deleteOldLogFiles(sasDirectoryPrefixPattern)

    clickButton(waitForObject(":Data parameters...._Button"))
    chooseFile(waitForObject(":SWT"), "/scratch/workspace/suite_ncd/tst_ncd_model_builder/workspace/data/examples/results_b21-2672_detector_040713_102411.nxs")
    mouseClick(waitForObject(":Data parameters.Working directory_Text"), 144, 5, 0, Button.Button1)
    type(waitForObject(":Data parameters.Working directory_Text"), "<Ctrl+a>")
    type(waitForObject(":Data parameters.Working directory_Text"), "/dls/tmp/squishtests")
    type(waitForObject(":Data parameters.Working directory_Text"), "<Ctrl+a>")
    type(waitForObject(":Data parameters.Working directory_Text"), "<Ctrl+c>")

    type(waitForObject(":Data parameters.HTML results directory_Text"), "<Ctrl+v>")
    clickButton(waitForObject(":Data parameters.Run NCD model building_Button"))
    snooze(130)

    logfile = findLogFile(sasDirectoryPrefixPattern, 100)
    test.verify(logfile != None, "Existence of log file")

    closeOrDetachFromDAWN()
