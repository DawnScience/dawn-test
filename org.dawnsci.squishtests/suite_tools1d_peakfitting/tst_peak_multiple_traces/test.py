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
        createPeakFitSpace(steps=25)
    snooze(1)
    
    #expand data tree and open metal mix
    loadMetalMix()
    
    mouseClick(waitForObject(":Plot data as separate plots_ToolItem"), 18, 11, 0, Button.Button1)
    
    for i in range(16):
        if(isEclipse4()):
            mouseClick(waitForObjectItem(":Data_Table_2", str(i) + "/0"), 9, 7, 0, Button.Button1)
        else:
            mouseClick(waitForObjectItem(":Data_Table", str(i) + "/0"), 9, 7, 0, Button.Button1)
    
    snooze(1)
    
    tab = fitOneThenFourPeaks()
        
    mouseClick(waitForObject(":Choose trace for fit._ToolItem"), 29, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Select all"))
    
    snooze(30)
    
    test.verify(tab.getItemCount()==64,"64 peaks in table")
    
    mouseClick(waitForObject(":Name_TableColumn"), 82, 18, 0, Button.Button1)
    snooze(1)
    mouseClick(waitForObject(":Name_TableColumn"), 82, 18, 0, Button.Button1)
    snooze(1)
    
    for i in range(8):
        txt = waitForObjectItem(":Peak Fitting_Table", str(i) + "/1").text

        test.verify(txt == "Peak " + str(i+1),"peak present")
    
    closeOrDetachFromDAWN()