source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))

# UI test to check that an hdf5 file can be opened and its tree can be expanded 
def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()

     # disable the decorator the metadata decorator
    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Preferences"))
    expand(waitForObjectItem(":Preferences_Tree", "General"))
    expand(waitForObjectItem(":Preferences_Tree", "Appearance"))
    mouseClick(waitForObjectItem(":Preferences_Tree", "Label Decorations"), 27, 14, 0, Button.Button1)
    mouseClick(waitForObject(":File Meta Data Decorator_ItemCheckbox"), 8, 13, 0, Button.Button1)         
    # enable the decorator the HDF5 tree decorator
    mouseClick(waitForObject(":HDF5 tree element Decorator_ItemCheckbox"), 11, 13, 0, Button.Button1)
    clickButton(waitForObject(":Preferences.OK_Button"))
 
#  mouseClick(waitForObject(":DAT file Scan Command Decorator_ItemCheckbox"), 8, 16, 0, Button.Button1)
    
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
    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Preferences"))
    expand(waitForObjectItem(":Preferences_Tree", "General"))
    expand(waitForObjectItem(":Preferences_Tree", "Appearance"))
    mouseClick(waitForObjectItem(":Preferences_Tree", "Label Decorations"), 27, 14, 0, Button.Button1)
    mouseClick(waitForObject(":File Meta Data Decorator_ItemCheckbox"), 8, 13, 0, Button.Button1)         
    clickButton(waitForObject(":Preferences.OK_Button"))
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