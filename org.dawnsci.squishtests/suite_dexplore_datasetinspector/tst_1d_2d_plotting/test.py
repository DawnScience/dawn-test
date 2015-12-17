source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_global_prefs_toggles.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))

# UI test to check that an hdf5 file can be opened and its tree can be expanded 
def main():
    startOrAttachToDAWN()
    
    toggleDATFileMDDecorators()
    
    openPerspective("DExplore")
    
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    doubleClick(waitForObjectItem(":Project Explorer_Tree", "pilatus300k.edf"), 12, 14, 0, Button.Button1)
    mouseClick(waitForObject(":Dataset slicing_Label"), 76, 12, 0, Button.Button1)
    
    #we get the plotting system
    system = getPlottingSystem("Dataset Plot")
    test.verify(system.getTraces().iterator().next().getData().getRank()==2, "Image plotted: Success")

    if (not isEclipse4()):    
        mouseClick(waitForObject(":Data axes selection_CTabFolderChevron"), 18, 6, 0, Button.Button1)
    if (isEclipse4()):
        mouseClick(waitForObject(":Show List_ToolItem"), 15, 11, 0, Button.Button1)

    activateItem(waitForObjectItem(":Pop Up Menu", "1D plot"))
    
    test.verify(system.getTraces().iterator().next().getData().getRank()==1, "1D plot: Success")

 # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
