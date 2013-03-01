source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))

import os

# This test makes sure we can start and stop DAWN
def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    
    # On a test you may add test code here 
    #Open data browsing perspective
    openPerspective("Data Browsing (default)")
    openExternalFile("i22-60191.nxs")
    snooze(15) 
    mouseClick(waitForObjectItem(":Data_Table_2", "0/0"), 7, 11, 0, Button.Button1)
    snooze(15) 

    system = getPlottingSystem("i22-60191.nxs")
    test.verify(system.getTraces().size()==1)
    
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()