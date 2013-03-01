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
    openExample("loop_example.moml", "workflows", "examples")
    
    widget = waitForObject(":loop_example.moml.Edit_CTabItem", 3000)
    clickTab(widget)

    mouseClick(waitForObject(":Run the workflow from start to end until finished._ToolItem"))
    snooze(120)
    clickButton(waitForObject(":Review.Continue_Button"))
    clickButton(waitForObject(":Review.Continue_Button"))
    clickButton(waitForObject(":Review.Continue_Button"))
    clickButton(waitForObject(":Review.Continue_Button"))
    clickButton(waitForObject(":Review.Continue_Button"))
    clickButton(waitForObject(":Error Message.OK_Button"))

    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()