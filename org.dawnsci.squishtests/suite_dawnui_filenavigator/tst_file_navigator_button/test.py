source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))

# UI test to check that an hdf5 file can be opened and its tree can be expanded 
def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()

    clickTab(waitForObject(":File Navigator_CTabItem"), 12, 8, 0, Button.Button1)

    mouseClick(waitForObject(":Refresh file tree_ToolItem_2"), 11, 13, 0, Button.Button1)
    test.passes("File Navigator refresh button: Success")
    
    mouseClick(waitForObject(":Collapse All_ToolItem_2"), 14, 14, 0, Button.Button1)
    test.passes("File Navigator collapse button: Success")

    mouseClick(waitForObject(":Refresh file tree_ToolItem_2"), 15, 11, 0, Button.Button1)
    test.passes("File Navigator refresh button: Success")
    
    mouseClick(waitForObject(":Alphanumeric sort for everything._ToolItem_2"), 13, 9, 0, Button.Button1)
    test.passes("File Navigator sort everything button: Success")

    mouseClick(waitForObject(":Sort alphanumeric, directories at top._ToolItem_2"), 8, 13, 0, Button.Button1)
    test.passes("File Navigator sort folder on top button: Success")
    
     # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
