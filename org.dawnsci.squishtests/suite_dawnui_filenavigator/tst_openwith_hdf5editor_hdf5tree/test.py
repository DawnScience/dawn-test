source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_global_prefs_toggles.py"))

# UI test to check that an hdf5 file can be opened and its tree can be expanded 
def main():
    startOrAttachToDAWN()
    
    toggleDATFileMDDecorators()
    
    openPerspective("Data Browsing (default)")
    
    # Open HDF5 file with HDF5 Editor
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    mouseClick(waitForObjectItem(":Project Explorer_Tree", "i22-4996.nxs"), 10, 16, 0, Button.Button3)
    activateItem(waitForObjectItem(":_Menu_2", "Open With"))
    activateItem(waitForObjectItem(":Open With_Menu", "Nexus/HDF5 Editor"))
    mouseClick(waitForObjectItem(":Data_Table_2", "2/0"), 6, 10, 0, Button.Button1)

    #we get the plotting system
    system = getPlottingSystem("i22-4996.nxs")
    test.verify(system.getTraces().iterator().next().getData().getRank()==2, "Image plotted: Success")
    
    # open DExplore perspective
    openPerspective("DExplore")

    # Open HDF5 file with HDF5 Tree Editor
    mouseClick(waitForObjectItem(":Project Explorer_Tree", "i22-4996.nxs"), 10, 16, 0, Button.Button3)
    activateItem(waitForObjectItem(":_Menu_2", "Open With"))
    activateItem(waitForObjectItem(":Open With_Menu", "Big Tree Editor"))
    expand(waitForObjectItem(":i22-4996.nxs_Tree", "entry1"))
    expand(waitForObjectItem(":i22-4996.nxs_Tree", "Rapid2D"))
    doubleClick(waitForObjectItem(":i22-4996.nxs_Tree", "data"), 25, 11, 0, Button.Button1)
    doubleClick(waitForObjectItem(":i22-4996.nxs_Tree", "data"), 25, 11, 0, Button.Button1)
    snooze(1)
    #we get the plotting system
    system = getPlottingSystem("Dataset Plot")
    test.verify(system.getTraces().iterator().next().getData().getRank()==2, "Image plotted: Success")
 
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
