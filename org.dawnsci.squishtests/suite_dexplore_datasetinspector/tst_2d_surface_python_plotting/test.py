source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "utilities.py"))

# UI test to check that an hdf5 file can be opened and its tree can be expanded 
def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    
    # disable the decorators
    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Preferences"))
    expand(waitForObjectItem(":Preferences_Tree", "General"))
    expand(waitForObjectItem(":Preferences_Tree", "Appearance"))
    mouseClick(waitForObjectItem(":Preferences_Tree", "Label Decorations"), 27, 14, 0, Button.Button1)
    mouseClick(waitForObject(":DAT file Scan Command Decorator_ItemCheckbox"), 8, 16, 0, Button.Button1)
    mouseClick(waitForObject(":File Meta Data Decorator_ItemCheckbox"), 8, 13, 0, Button.Button1)
    clickButton(waitForObject(":Preferences.OK_Button"))

    # Install EPD to the default location
    # On a clean machine setupEPDPython will defer
    # to setupPython(installEPD=True)
    # On a machine where EPD is already installed
    # it will simply be selected
    setupEPDPython() 
    
    # open DExplore perspective
    openPerspective("DExplore")
    
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    doubleClick(waitForObjectItem(":Project Explorer_Tree", "pilatus300k.edf"), 12, 14, 0, Button.Button1)
    #we get the plotting system
    system = getPlottingSystem("Dataset Plot")
    test.verify(system.getTraces().iterator().next().getData().getRank()==2, "Image plotted: Success")
 
    mouseClick(waitForObject(":Dataset slicing_Label"), 76, 12, 0, Button.Button1)

    # switch to surface plot mode
    mouseClick(waitForObject(":Data axes selection_CTabFolderChevron"), 6, 11, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "2D surface"))
    snooze(5.0)
    
    #Open python console
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 9, 6, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open New Plot Scripting"))
    clickButton(waitForObject(":Python console_Button"))
    clickButton(waitForObject(":OK_Button"))
    snooze(10.0)
    #get the databean from the dataset plot to check that some data has been plotted in surface mode
    typeInConsole("bean=dnp.plot.getbean('Dataset Plot')")
    snooze(2.0)
    typeInConsole("bean[dnp.plot.parameters.plotmode]")
    snooze(2.0)
    expected ="surf2d\n>>> "
    got = waitForObject(":PyDev Console").text
    if got.endswith(expected):
        test.verify(True, "Image data to 2D Surface plot: Success")
    else:
        test.fail("guibean is not correct: expected '%s', got '%s'" % (expected, got))

    # switch to 2d plot mode
    clickTab(waitForObject(":2D image_CTabItem"), 28, 12, 0, Button.Button1)
    snooze(2.0)
    #get the databean from the dataset plot to check that some data has been plotted in surface mode
    typeInConsole("bean=dnp.plot.getbean('Dataset Plot')")
    snooze(2.0)
    typeInConsole("bean[dnp.plot.parameters.plotmode]")
    snooze(2.0)
    expected ="twod\n>>> "
    got = waitForObject(":PyDev Console").text
    if got.endswith(expected):
        test.verify(True, "2D Surface to image plot: Success")
    else:
        test.fail("guibean is not correct: expected '%s', got '%s'" % (expected, got))
   
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()

