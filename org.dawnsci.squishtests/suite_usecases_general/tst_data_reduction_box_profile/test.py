source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))

import os

# This test makes sure we can start and stop DAWN
def main():
    vals = dawn_constants
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    
    # On a test you may add test code here 
    #Open data browsing perspective
    openPerspective("Data Browsing")
    snooze(0.5)
    expandObjectLeft(waitForObject(":Data_CTabItem_2"))
    clickTab(waitForObject(":Project Explorer_CTabItem_2"), 93, 16, 0, Button.Button1)
    snooze(0.5)
    openExternalFile("9758.nxs")
    snooze(0.5)
    # Select image and zoom
    clickTab(waitForObject(":Data_CTabItem_2"), 30, 6, 0, Button.Button1)
    mouseClick(waitForObject(":Data_Text_2"), 47, 8, 0, Button.Button1)
    type(waitForObject(":Data_Text_2"), "14/dat")
    mouseClick(waitForObjectItem(":Data_Table_2", "0/0"), 7, 8, 0, Button.Button1)

        
    snooze(5)
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem_2"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Profile"))
    activateItem(waitForObjectItem(":Profile_Menu", "Box Profile"))
    
    snooze(1)
    proxy  = waitForObject(":9758.nxs_CTabItem")
    widget = proxy.control
    b = widget.bounds
    mouseDrag(widget, b.x+100, b.y+100, 300, 300, 0, Button.Button1)
    snooze(2) # While zoom...


    system = getPlottingSystem("9758.nxs")
    test.verify(system.getRegions().size()==1)
    test.passes("One trace plotted") 
    
    clickTab(waitForObject(":Data_CTabItem_2"), 28, 4, 0, Button.Button1)
    mouseClick(waitForObject(":Data reduction..._ToolItem_4"), 14, 11, 0, Button.Button1)
    snooze(1)
    mouseClick(waitForObject(":Dataset Name_CCombo"), 467, 9, 0, Button.Button1)
    mouseClick(waitForObjectItem(":_List", "/entry1/EDXD_Element_01/data"), 214, 11, 0, Button.Button1)
    
    snooze(1) 
    clickButton(waitForObject(":Finish_Button"))
    
    # Show plotted image
    snooze(2) 
    mouseClick(waitForObjectItem(":Data_Table_2", "1/0"), 6, 12, 0, Button.Button1)
    snooze(3) 
    system = getPlottingSystem("9758_Box_Profile.nxs")
    test.verify(system.getRegions().size()==0)
    test.verify(system.getTraces().size()==1)
    test.passes("Something plotted from data reduction") 


    # Do a line fit on it just for fun
    mouseClick(waitForObject(":XY plotting tools_ToolItem_7"), 31, 6, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Line Fitting"))
    
    proxy  = waitForObject(":9758_Box_Profile.nxs_CTabItem")
    widget = proxy.control
    b = widget.bounds
    mouseDrag(widget, b.x+100, b.y+100, 600, 300, 0, Button.Button1)
    snooze(2) # While fit...

    
    mouseClick(waitForObject(":Polynomial order to fit_ToolItem"), 31, 13, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Polynomial Order: 2"))
    mouseClick(waitForObject(":Polynomial order to fit_ToolItem"), 33, 13, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Polynomial Order: 3"))
    mouseClick(waitForObject(":Polynomial order to fit_ToolItem"), 31, 11, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Polynomial Order: 4"))
    mouseClick(waitForObject(":Polynomial order to fit_ToolItem"), 29, 9, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Polynomial Order: 5"))
    mouseClick(waitForObject(":Polynomial order to fit_ToolItem"), 32, 9, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Polynomial Order: 6"))
    mouseClick(waitForObject(":Polynomial order to fit_ToolItem"), 30, 12, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Polynomial Order: 7"))


    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
