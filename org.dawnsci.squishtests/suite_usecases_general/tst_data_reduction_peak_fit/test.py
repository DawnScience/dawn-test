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
    
    clickTab(waitForObject(":Data_CTabItem_2"), 45, 14, 0, Button.Button3)
    activateItem(waitForObjectItem(":Pop Up Menu", "Size"))
    activateItem(waitForObjectItem(":Size_Menu", "Left"))
    type(waitForObject(":_Sash"), "<Left>")
    type(waitForObject(":_Sash"), "<Left>")
    type(waitForObject(":_Sash"), "<Left>")
    type(waitForObject(":_Sash"), "<Left>")
    type(waitForObject(":_Sash"), "<Left>")
    type(waitForObject(":_Sash"), "<Left>")
    openExternalFile("9758.nxs")


    chooseSlice()    

    activateItem(waitForObjectItem(":Pop Up Menu", "Peak Fitting"))
    
    proxy  = waitForObject(":9758.nxs_CTabItem")
    widget = proxy.control
    b = widget.bounds
    mouseDrag(widget, b.x+100, b.y+100, 300, 300, 0, Button.Button1)
    snooze(10) # While fit...
    
    mouseClick(waitForObject(":Data reduction..._ToolItem"), 6, 11, 0, Button.Button1)
    
    # Do some reduction
    #clickButton(waitForObject(":Overwrite file if it exists._Button"))
    snooze(10) 
    clickButton(waitForObject(":Finish_Button"))
    
    # Plot some reduction
    snooze(10) # While open file...
    
    clickTab(waitForObject(":9758_Peak_Fitting.h5_CTabItem",180000), 77, 14, 0, Button.Button1)

    mouseClick(waitForObjectItem(":Data_Table_2", "0/0"), 5, 13, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table_2", "1/0"), 7, 9, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table_2", "3/0"), 6, 5, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table_2", "4/0"), 6, 8, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table_2", "2/0"), 5, 10, 0, Button.Button1)
    
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
