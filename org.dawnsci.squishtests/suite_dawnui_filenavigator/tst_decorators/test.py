source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))
source(findFile("scripts", "dawn_global_prefs_toggles.py"))

# UI test to check that an hdf5 file can be opened and its tree can be expanded 
def main():
    startOrAttachToDAWN()
    
    toggleHDFFileMDDecorators()

    openPerspective("Data Browsing (default)")

    # Add h5 customisations
    projectViewMenu = getToolItemOfCTabFolder(cTabItemText="Project Explorer", cTabItemTooltipText="Workspace",
                                      toolItemTooltipText="View Menu")
    mouseClick(waitForObject(projectViewMenu), 12, 7, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Customize View..."))
    clickTab(waitForObject(":Available Customizations.Content_CTabItem"), 20, 13, 0, Button.Button1)
    mouseClick(waitForObject(":HDF5 File Contents_ItemCheckbox"), 8, 9, 0, Button.Button1)
    clickButton(waitForObject(":Available Customizations.OK_Button"))
    
    # Expand hdf5 file and open
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    expand(waitForObjectItem(":Project Explorer_Tree", "i22-4996.nxs"))
    test.passes("expandNXSFile: Success")
    expand(waitForObjectItem(":Project Explorer_Tree", "entry1 NXentry "))
    test.passes("expand Nexus Entry with decorator: Success")
    expand(waitForObjectItem(":Project Explorer_Tree", "Calibration NXdata "))
    test.passes("expand Nexus Entry with decorator: Success")
    doubleClick(waitForObjectItem(":Project Explorer_Tree", "Calibration NXdata "), 12, 14, 0, Button.Button1)
    test.passes("openNXSFile: Success")
    
    # Test the DAT scan command decorators
    expand(waitForObjectItem(":Project Explorer_Tree", "96356.dat * Scan Command: N/A"))
    test.passes("expandDATFile with decorator: Success")
    doubleClick(waitForObjectItem(":Project Explorer_Tree", "eta"), 12, 14, 0, Button.Button1)
    test.passes("openDATFile: Success")
    
    # Test the metadata decorators
    toggleFileMDDecorator()
    snooze(2.5)
    
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples")) 
    childFound = False
    for child in children:
        element = child.text
        if "96356.dat  5.5 KB" in element:
            test.passes("File with metadata decorator found: Success")
            expand(waitForObjectItem(":Project Explorer_Tree", child.text))
            test.passes("expand File with Metadata decorator: Success")
            doubleClick(waitForObjectItem(":Project Explorer_Tree", child.text), 12, 14, 0, Button.Button1)
            test.passes("open File with Metadata decorator: Success")
            childFound = True
            continue
            
    if childFound is False:
        test.fail("file with metadata decorator not found")
    
     # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()