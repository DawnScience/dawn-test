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
    openPerspective("Data Browsing (default)")

    # Exit (or disconnect) DAWN
    openExternalFile("315029.dat")
    if (isEclipse4()):
        mouseClick(waitForObject(":Data_Table_6"), 70, 293, 0, Button.Button1)
    else:
        mouseClick(waitForObject(":Data_Table"), 70, 293, 0, Button.Button1)

    mouseClick(waitForObject(":Adds an expression which can be plotted. Must be function of other data sets._ToolItem_3"))
    if (isEclipse4()):
        type(waitForObject(":Data_Text_4"), "dat:mean(Pilatus,0)")
        type(waitForObject(":Data_Text_4"), "<Return>")
    else:
        type(waitForObject(":Data_Text"), "dat:mean(Pilatus,0)")
        type(waitForObject(":Data_Text"), "<Return>")
    
    snooze(5)
    system = getPlottingSystem("315029.dat")
    test.verify(system.getTraces().size()==1)
    test.verify(system.getTraces().iterator().next().getData().getRank()==2)
    
    if (isEclipse4()):
        mouseClick(waitForObjectItem(":Data_Table_6", "11/1"), 5, 5, 0, Button.Button3)
        activateItem(waitForObjectItem(":_Menu_6", "Copy 'dat:mean(Pilatus,0)' (can be pasted into other data)."))
    else:
        mouseClick(waitForObjectItem(":Data_Table", "11/1"), 5, 5, 0, Button.Button3)
        activateItem(waitForObjectItem(":_Menu_3", "Copy 'dat:mean(Pilatus,0)' (can be pasted into other data)."))
  
    openExternalFile("9758.nxs")
    snooze(10)

    if (isEclipse4()):
        mouseClick(waitForObjectItem(":Data_Table_6", "24/1"), 5, 5, 0, Button.Button3)
        activateItem(waitForObjectItem(":_Menu_6", "Paste 'dat:mean(Pilatus,0)' (from file 315029.dat) into this data."))
    else:
        mouseClick(waitForObjectItem(":Data_Table", "24/1"), 5, 5, 0, Button.Button3)
        activateItem(waitForObjectItem(":_Menu_3", "Paste 'dat:mean(Pilatus,0)' (from file 315029.dat) into this data."))
   
    system = getPlottingSystem("9758.nxs")
    snooze(5)
    test.verify(system.getTraces().size()==1, "Size should be 1 and is "+str(system.getTraces().size()))
    test.verify(system.getTraces().iterator().next().getData().getRank()==2)

    closeOrDetachFromDAWN()

