source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "use_case_utils.py"))

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
    mouseClick(waitForObjectItem(":Preferences_Tree", "Label Decorations"), 27, 14, 0, Button.Button1)
    mouseClick(waitForObject(":DAT file Scan Command Decorator_ItemCheckbox"), 8, 16, 0, Button.Button1)
    mouseClick(waitForObject(":File Meta Data Decorator_ItemCheckbox"), 8, 13, 0, Button.Button1)
    clickButton(waitForObject(":Preferences.OK_Button"))
    
    # open DExplore perspective
    # mouseClick(waitForObject(":Open Perspective_ToolItem"), 7, 15, 0, Button.Button1)
    # activateItem(waitForObjectItem(":Pop Up Menu", "DExplore"))
    openPerspective("DExplore")
    
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    doubleClick(waitForObjectItem(":Project Explorer_Tree", "pilatus300k.edf"), 12, 14, 0, Button.Button1)
    mouseClick(waitForObject(":Dataset slicing_Label"), 76, 12, 0, Button.Button1)
    
    #we get the plotting system
    system = getPlottingSystem("Dataset Plot")
    test.verify(system.getTraces().iterator().next().getData().getRank()==2, "Image plotted: Success")
    
    mouseClick(waitForObject(":Data axes selection_CTabFolderChevron"), 18, 6, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "1D plot"))
    
    test.verify(system.getTraces().iterator().next().getData().getRank()==1, "1D plot: Success")

   # activateItem(waitForObjectItem(":Pop Up Menu", "2D image"))
   # test.passes("openNXSFile: Success")

 # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
