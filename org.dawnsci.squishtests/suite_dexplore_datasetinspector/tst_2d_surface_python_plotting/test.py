source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_global_prefs_toggles.py"))
source(findFile("scripts", "dawn_global_python_setup.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))
source(findFile("scripts", "use_case_utils.py"))

# UI test to check that an hdf5 file can be opened and its tree can be expanded 
def main():
    startOrAttachToDAWN()
    
    toggleDATFileMDDecorators()
    
    setupPython()
    
    openPerspective("DExplore")
    
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    doubleClick(waitForObjectItem(":Project Explorer_Tree", "pilatus300k.edf"), 12, 14, 0, Button.Button1)
    #we get the plotting system
    system = getPlottingSystem("Dataset Plot")
    test.verify(system.getTraces().iterator().next().getData().getRank()==2, "Image plotted: Success")
 
    mouseClick(waitForObject(":Dataset slicing_Label"), 76, 12, 0, Button.Button1)

    # switch to surface plot mode
    if (not isEclipse4()):
        mouseClick(waitForObject(":Data axes selection_CTabFolderChevron"), 6, 11, 0, Button.Button1)
    if (isEclipse4()):
        mouseClick(waitForObject(":Show List_ToolItem"), 15, 11, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "2D surface"))
    snooze(5.0)
    
    #Open python console
#     datasetPlotViewMenu = getToolItemOfCTabFolder(cTabItemTooltipText="Dataset Plot", toolItemTooltipText="View Menu")
#     mouseClick(waitForObject(datasetPlotViewMenu))
    clickTab(waitForObject(":Dataset Plot_CTabItem"), 44, 17, 0, Button.Button1)
    mouseClick(waitForObject(":Open Pydev console_ToolItem"), 28, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Create new Pydev Console"))
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

