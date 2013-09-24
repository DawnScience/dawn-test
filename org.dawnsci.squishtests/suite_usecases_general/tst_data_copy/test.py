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
    mouseClick(waitForObject(":Adds an expression which can be plotted. Must be function of other data sets._ToolItem_2"))
    type(waitForObject(":Data_Text"), "dat:mean(Pilatus,0)")
    type(waitForObject(":Data_Text"), "<Return>")
    
    system = getPlottingSystem("315029.dat")
    test.verify(system.getTraces().size()==1)
    test.verify(system.getTraces().iterator().next().getData().getRank()==2)
    
    mouseClick(waitForObjectItem(":Data_Table", "11/1"), 23, 7, 0, Button.Button3)
    activateItem(waitForObjectItem(":_Menu_3", "Copy 'dat:mean(Pilatus,0)' (can be paste to other data)."))
  
    openExternalFile("9758.nxs")

    mouseClick(waitForObjectItem(":Data_Table", "24/1"), 67, 0, 0, Button.Button3)
    activateItem(waitForObjectItem(":_Menu_3", "Paste 'dat:mean(Pilatus,0)' (from file 315029.dat) into this data."))
   
    system = getPlottingSystem("9758.nxs")
    test.verify(system.getTraces().size()==1)
    test.verify(system.getTraces().iterator().next().getData().getRank()==2)

    closeOrDetachFromDAWN()

