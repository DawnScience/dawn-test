source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "peakfit_shared.py"))

def main():
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Data Browsing (default)")
    
    #Create space so the drop-down menus show all items
    createPeakFitSpace()
    snooze(1)
    
    #expand data tree and open metal mix
    loadMetalMix()
    
    mouseClick(waitForObjectItem(":Data_Table", "0/0"), 9, 7, 0, Button.Button1)
    
    snooze(1)
    
    fitOneThenFourPeaks()
        
    closeOrDetachFromDAWN()
