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

    # Exit (or disconnect) DAWN
    openExternalFile("315029.dat")
    mouseClick(waitForObject(":Data_Table"), 70, 293, 0, Button.Button1)
    mouseClick(waitForObject(":Adds an expression which can be plotted. Must be function of other data sets._ToolItem_3"))
    type(waitForObject(":Data_Text_4"), "dat:mean(Pilatus, 0)")
    mouseClick(waitForObject(":Data_Text_4")) # closes pop-up content proposal
    type(waitForObject(":Data_Text_4"), "<Return>")

    
    system = getPlottingSystem("315029.dat")
    test.verify(system.getTraces().size()==1)
    test.verify(system.getTraces().iterator().next().getData().getRank()==2)
    
    closeOrDetachFromDAWN()

