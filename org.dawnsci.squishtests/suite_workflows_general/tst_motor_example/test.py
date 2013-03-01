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
    openExample("motor_example.moml", "workflows", "examples")
    
    widget = waitForObject(":motor_example.moml.Edit_CTabItem", 3000)
    clickTab(widget)

    mouseClick(waitForObject(":Run the workflow from start to end until finished._ToolItem"))
    snooze(120)
    mouseClick(waitForObjectItem(":Review_Table", "0/1"))
    type(waitForObject(":Review_StyledText"), "1")
    type(waitForObject(":Review_StyledText"), "<Return>")
    clickButton(waitForObject(":Review.Continue_Button"))
    snooze(2)

    clickTab(waitForObject(":new_data_file1.h5_CTabItem"))
    
    expand(waitForObjectItem(":Tree_Tree", "entry"))
    expand(waitForObjectItem(":Tree_Tree", "dictionary"))
    mouseClick(waitForObjectItem(":Tree_Tree", "kap1"))

    clickTab(waitForObject(":Value_CTabItem"))
    widget = waitForObject(":Value_StyledText")
    text  = widget.text
    lines = text.split("\n")

    test.verify(lines[0] == "10.0", "Checking if first line is 10.0")


    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()