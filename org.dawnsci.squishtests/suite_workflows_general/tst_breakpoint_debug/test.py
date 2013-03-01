source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))

import os
from datetime import datetime

def main():
    
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    openPerspective("Workflow")
    createProject("workflows")
    openExample("maths_example.moml", "workflows", "examples")
    
    widget = waitForObject(":maths_example.moml.Edit_CTabItem", 3000)
    clickTab(widget)

    mouseClick(waitForObject(":_ImageFigure_4"), 19, 30, 0, Button.Button3)
    activateItem(waitForObjectItem(":_Menu_3", "Toggle actor breakpoint"))
   
    mouseClick(waitForObject(":Run the workflow from start to end until finished._ToolItem"))
    clickButton(waitForObject(":Save Resource.Yes_Button"))
   
    snooze(60)
    
    clickTab(waitForObject(":Debug Actor_CTabItem", 120000), 66, 7, 0, Button.Button1)

    
    snooze(10)
    
    mouseClick(waitForObject(":Continue_ToolItem", 60000), 10, 13, 0, Button.Button1)
    
    snooze(10)
    
    mouseClick(waitForObject(":Continue_ToolItem", 60000), 10, 13, 0, Button.Button1)
    
    clickTab(waitForObject(":ref-testscale_1_0011.h5_CTabItem",120000), 128, 9, 0, Button.Button1)

    mouseClick(waitForObjectItem(":Data_Table_5", "0/0"), 11, 9, 0, Button.Button1)
    snooze(1)
    
    system = getPlottingSystem("ref-testscale_1_0011.h5")
    test.verify(system.getTraces().iterator().next().getData().getRank()==2, "Check add plotted")
    
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
