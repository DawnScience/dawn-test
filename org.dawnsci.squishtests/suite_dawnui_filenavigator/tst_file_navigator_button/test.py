source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))

# UI test to check that an hdf5 file can be opened and its tree can be expanded 
def main():
    startOrAttachToDAWN()

    clickTab(waitForSwtCTabItem(caption="File Navigator"))

    mouseClick(waitForSwtToolItem(item_tooltiptext="Refresh file tree"))
    test.passes("File Navigator refresh button: Success")
    
    mouseClick(waitForSwtToolItem(item_tooltiptext="Collapse All"))
    test.passes("File Navigator collapse button: Success")

    mouseClick(waitForSwtToolItem(item_tooltiptext="Refresh file tree"))
    test.passes("File Navigator refresh button: Success")
    
    mouseClick(waitForSwtToolItem(item_tooltiptext="Alphanumeric sort for everything."))
    test.passes("File Navigator sort everything button: Success")

    mouseClick(waitForSwtToolItem(item_tooltiptext="Sort alphanumeric, directories at top."))
    test.passes("File Navigator sort folder on top button: Success")
    
     # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
