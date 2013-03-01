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
    openExample("directory_packing_example.moml", "workflows", "examples")
    
    widget = waitForObject(":directory_packing_example.moml.Edit_CTabItem", 3000)
    clickTab(widget)

    mouseClick(waitForObject(":Run the workflow from start to end until finished._ToolItem"))
    snooze(120)
    clickTab(waitForObject(":export.h5_CTabItem"), 53, 10, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table_5", "0/0"), 10, 9, 0, Button.Button1)
    snooze(1)
    
    system = getPlottingSystem("export.h5")
    test.verify(system.getTraces().iterator().next().getData().getRank() == 2, "Check add plotted")

    
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
