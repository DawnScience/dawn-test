source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))

import os
from datetime import datetime
import string

def main():
    
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    openPerspective("Workflow")
    createProject("workflows")
    openExample("spec_scan_example.moml", "workflows", "examples")
    
    widget = waitForObject(":spec_scan_example.moml.Edit_CTabItem", 3000)
    clickTab(widget)

    mouseClick(waitForObject(":Run the workflow from start to end until finished._ToolItem"))
    snooze(120)
    clickTab(waitForObject(":new_data_file1.h5_CTabItem", 60000))
    expand(waitForObjectItem(":Tree_Tree", "entry"))
    expand(waitForObjectItem(":Tree_Tree", "dictionary"))
    mouseClick(waitForObjectItem(":Tree_Tree", "ascan__result"), 45, 14, 0, Button.Button1)
    clickTab(waitForObject(":Value_CTabItem"), 35, 13, 0, Button.Button1)
    
    widget = waitForObject(":Value_StyledText")
    text  = widget.text
    lines = text.split("\n")
    stringArray  = (str(lines[12])).strip().split()
    test.verify(stringArray[:4] == ['10', '10.0000', '0', '0'], "Scan output check '")
    snooze(1)
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()

