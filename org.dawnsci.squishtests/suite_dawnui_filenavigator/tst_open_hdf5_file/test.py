source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_global_prefs_toggles.py"))

# UI test to check that an hdf5 file can be opened and its tree can be expanded 
def main():
    startOrAttachToDAWN()
    
    toggleDATFileMDDecorators()
    
    openPerspective("DExplore")

    # Add h5 customisations
    mouseClick(waitForObject(":View Menu_ToolItem"), 12, 7, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Customize View..."))
    clickTab(waitForObject(":Available Customizations.Content_CTabItem"), 20, 13, 0, Button.Button1)
    mouseClick(waitForObject(":HDF5 File Contents_ItemCheckbox_2"), 8, 9, 0, Button.Button1)
    clickButton(waitForObject(":Available Customizations.OK_Button"))
    
    # Expand hdf5 file and open
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    expand(waitForObjectItem(":Project Explorer_Tree", "i22-4996.nxs"))
    test.passes("expandNXSFile: Success")
    expand(waitForObjectItem(":Project Explorer_Tree", "entry1 "))
    expand(waitForObjectItem(":Project Explorer_Tree", "Calibration "))
    expand(waitForObjectItem(":Project Explorer_Tree", "data "))
    doubleClick(waitForObjectItem(":Project Explorer_Tree", "data "), 12, 14, 0, Button.Button1)
    test.passes("openNXSFile: Success")

    snooze(2.5)
    
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()

