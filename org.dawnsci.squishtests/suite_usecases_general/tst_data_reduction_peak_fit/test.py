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
    snooze(0.5)
    expandObjectLeft(waitForObject(":Data_CTabItem_2"))
    clickTab(waitForObject(":Project Explorer_CTabItem_2"), 93, 16, 0, Button.Button1)
    snooze(0.5)
    openExternalFile("9758.nxs")
    snooze(0.5)

    chooseSlice()    

    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Peak Fitting"))

    
    proxy  = waitForObject(":9758.nxs_CTabItem")
    widget = proxy.control
    b = widget.bounds
    mouseDrag(widget, b.x+100, b.y+100, 300, 300, 0, Button.Button1)
    snooze(10) # While fit...

    mouseClick(waitForObject(":Data reduction..._ToolItem_4"), 19, 16, 0, Button.Button1)
    snooze(1)
    mouseClick(waitForObject(":Dataset Name_CCombo"))
    mouseClick(waitForObjectItem(":_List", "/entry1/EDXD_Element_01/data"), 214, 11, 0, Button.Button1)
    snooze(5)
    # Do some reduction
    #clickButton(waitForObject(":Overwrite file if it exists._Button"))
    clickButton(waitForObject(":Finish_Button"))
    
    # Plot some reduction
    snooze(90) # While open file...
    
#    clickTab(waitForObject(":Data_CTabItem_2",180000), 77, 14, 0, Button.Button1)

    clickTab(waitForObject(":9758_Peak_Fitting.nxs_CTabItem"))
    mouseClick(waitForObjectItem(":Data_Table_2", "0/0"))
    mouseClick(waitForObjectItem(":Data_Table_2", "1/0"))
    mouseClick(waitForObjectItem(":Data_Table_2", "3/0"))
    mouseClick(waitForObjectItem(":Data_Table_2", "4/0"))
    mouseClick(waitForObjectItem(":Data_Table_2", "2/0"))
    
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
