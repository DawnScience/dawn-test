source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))

# UI test to check that an hdf5 file can be opened and its tree can be expanded 
def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()

    # go to the dataexplore perspective
    
    # disable the decorators
    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Preferences"))
    expand(waitForObjectItem(":Preferences_Tree", "General"))
    expand(waitForObjectItem(":Preferences_Tree", "Appearance"))
    mouseClick(waitForObjectItem(":Preferences_Tree", "Label Decorations"))
    mouseClick(waitForObject(":DAT file Scan Command Decorator_ItemCheckbox"))
    mouseClick(waitForObject(":File Meta Data Decorator_ItemCheckbox"))
    clickButton(waitForObject(":Preferences.OK_Button"))
    
    # open DExplore perspective
    # mouseClick(waitForObject(":Open Perspective_ToolItem"), 7, 15, 0, Button.Button1)
    # activateItem(waitForObjectItem(":Pop Up Menu", "DExplore"))
    openPerspective("DExplore")

    # Add h5 customisations
    mouseClick(waitForObject(":View Menu_ToolItem"), 12, 7, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Customize View..."))
    clickTab(waitForObject(":Available Customizations.Content_CTabItem"), 20, 13, 0, Button.Button1)
    mouseClick(waitForObject(":HDF5 File Contents_ItemCheckbox"), 8, 9, 0, Button.Button1)
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
    
    # open plot settings
    #conOb = waitForObject(":Configure Settings..._ToolItem")
    #check_plotted_trace_name_yval(conOb,"eta","40.0","0.0")


    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
    
