source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "peakfit_shared.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))

def main():
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Data Browsing (default)")
    
    #Create space so the drop-down menus show all items
    if(not isEclipse4()):
        createPeakFitSpace()
    snooze(1)
    
    #expand data tree and open metal mix
    loadMetalMix()
    
    if(isEclipse4()):
        mouseClick(waitForObjectItem(":Data_Table_2", "0/0"), 9, 7, 0, Button.Button1)
    else:
        mouseClick(waitForObjectItem(":Data_Table", "0/0"), 9, 7, 0, Button.Button1)
    
    snooze(1)
    
    tab = fitOneThenFourPeaks()
    
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 11, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open 'Peak Fitting' in dedicated view"))
    
    test.verify(tab.getItemCount()==4,"Expected: 4 Actual: " + str(tab.getItemCount()))
    
    for i in range(4):
        txt = waitForObjectItem(":Peak Fitting_Table",  str(i) + "/1").text
        test.verify(txt == "Peak " + str(i+1),"peak present")


    closeOrDetachFromDAWN()