source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))

# UI test to check that an hdf5 file can be opened and its tree can be expanded 
def main():
    startOrAttachToDAWN()

    clickTab(waitForObject(":File Viewer_CTabItem"), 49, 8, 0, Button.Button1)

    mouseClick(waitForObject(":Parent_ToolItem"), 11, 13, 0, Button.Button1)
    test.passes("File Viewer parent button: Success")

    mouseClick(waitForObject(":Refresh_ToolItem"), 9, 10, 0, Button.Button1)
    test.passes("File Viewer refresh button: Success")

    mouseClick(waitForObject(":Edit Layout_ToolItem"), 13, 13, 0, Button.Button1)
    test.passes("File Viewer Layout button: Success")

    mouseClick(waitForObject(":Edit Layout_ToolItem"), 13, 13, 0, Button.Button1)
    test.passes("File Viewer Layout2 button: Success")

     # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()

