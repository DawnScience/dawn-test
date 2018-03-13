source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))

import os

# This test makes sure we can start and stop DAWN
def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    
    # On a test you may add test code here 
    #Open data browsing perspective
    openPerspective("Data Browsing")

    # Exit (or disconnect) DAWN
    openExternalFile("315029.dat")
    table = ":Data_Table_6" if isEclipse4() else ":Data_Table"
    mouseClick(waitForObject(table))

    mouseClick(waitForObject(":Adds an expression which can be plotted. Must be function of other data sets._ToolItem_3"))

    text = ":Data_Text_4" if isEclipse4() else ":Data_Text"
    type(waitForObject(text), "dat:mean(Pilatus,0)")
    mouseClick(waitForObject(text)) # closes pop-up content proposal
    type(waitForObject(text), "<Return>")
    
    snooze(5)
    system = getPlottingSystem("315029.dat")
    test.verify(system.getTraces().size()==1)
    test.verify(system.getTraces().iterator().next().getData().getRank()==2)
    
    menu = ":_Menu_6" if isEclipse4() else ":_Menu_3"
    mouseClick(waitForObjectItem(table, "11/1"), 5, 5, 0, Button.Button3)
    activateItem(waitForObjectItem(menu, "Copy 'dat:mean(Pilatus,0)' (can be pasted into other data)."))
  
    openExternalFile("9758.nxs")
    snooze(10)

    mouseClick(waitForObjectItem(table, "1/1"), 5, 5, 0, Button.Button3)
    activateItem(waitForObjectItem(menu, "Paste 'dat:mean(Pilatus,0)' (from file 315029.dat) into this data."))
   
    system = getPlottingSystem("9758.nxs")
    snooze(5)
    test.verify(system.getTraces().size()==1, "Size should be 1 and is "+str(system.getTraces().size()))
    test.verify(system.getTraces().iterator().next().getData().getRank()==2)

    closeOrDetachFromDAWN()

