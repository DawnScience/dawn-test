source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_global_prefs_toggles.py"))

# UI test to check that a dat file can be opened and plotted 
def main():
    startOrAttachToDAWN()
    
    toggleDATFileMDDecorators()
    
    openPerspective("DExplore")
    
    # Expand Dat file
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    expand(waitForObjectItem(":Project Explorer_Tree", "96356.dat"))
    test.passes("expandDATFile: Success")
    doubleClick(waitForObjectItem(":Project Explorer_Tree", "eta"), 12, 14, 0, Button.Button1)
    test.passes("openDATFile: Success")
    mouseClick(waitForObjectItem(":Project Explorer_Tree", "IC1"), 19, 13, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Project Explorer_Tree", "rc"), 19, 13, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Project Explorer_Tree", "eta"), 19, 13, 0, Button.Button1)
    snooze(2.5)
    
    # open plot settings
    conOb = waitForObject(":Configure Settings..._ToolItem")
    
    check_plotted_trace_name_yval(conOb,"eta (96356.dat)","40.0","0.0")

    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()

