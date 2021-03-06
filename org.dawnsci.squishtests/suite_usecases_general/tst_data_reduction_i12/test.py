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
    openExternalFile("40788.nxs")
    snooze(0.5)
    
    # Exit (or disconnect) DAWN
    mouseClick(waitForObjectItem(":Data_Table_2", "0/0"), 6, 13, 0, Button.Button1)
    mouseClick(waitForObject(":Slice as line plots_ToolItem_3"), 11, 14, 0, Button.Button1)
    mouseClick(waitForObject(":XY plotting tools_ToolItem_8"), 30, 9, 0, Button.Button1)
    
    # Peak Fitting
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Peak Fitting"))

    # Drag a peak
    proxy  = waitForObject(":40788.nxs_CTabItem")
    widget = proxy.control
    b = widget.bounds
    mouseDrag(widget, b.x+100, b.y+100, 300, 300, 0, Button.Button1)
    snooze(10) # While fit...

    
    mouseClick(waitForObject(":Data reduction..._ToolItem_4"), 10, 9, 0, Button.Button1)
    mouseClick(waitForObjectItem(":_Table", "1/1"), 32, 21, 0, Button.Button1)
    mouseClick(waitForObjectItem(":_List", "(Range)"), 42, 10, 0, Button.Button1)
    mouseClick(waitForObjectItem(":_Table", "0/1"), 35, 25, 0, Button.Button1)
    mouseClick(waitForObjectItem(":_List", "(Slice)"), 37, 7, 0, Button.Button1)
    clickButton(waitForObject(":Finish_Button"))
    
    snooze(90) # While Reduce...
    
    clickTab(waitForObject(":Data_CTabItem_2"), 24, 13, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table_2", "4/0"), 5, 11, 0, Button.Button1)
    
    # We get the plotting system
    system = getPlottingSystem("40788_Peak_Fitting.nxs")
    trace  = system.getTraces().iterator().next()
    data   = trace.getData()
    test.verify(data != None, "There should be some data")
    
    closeOrDetachFromDAWN()
