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
    openExample("if_example.moml", "workflows", "examples")
    
    widget = waitForObject(":if_example.moml.Edit_CTabItem", 3000)
    clickTab(widget)

    mouseClick(waitForObject(":_ImageFigure_2"), 21, 43, 0, Button.Button1)
    mouseClick(waitForObject(":_ImageFigure_3"), 17, 40, 0, Button.Button1)
    mouseClick(waitForObject(":_ImageFigure"), 17, 43, 0, Button.Button1)

    mouseClick(waitForObjectItem(":Actor Attributes_Table", "5/1"), 191, 16, 0, Button.Button1)
    doubleClick(waitForObjectItem(":Actor Attributes_Table", "5/1"), 191, 16, 0, Button.Button1)

    mouseClick(waitForObject(":Actor Attributes_StyledText"), 440, 6, 0, Button.Button1)
    type(waitForObject(":Actor Attributes_StyledText"), "<Shift+Left>")
    type(waitForObject(":Actor Attributes_StyledText"), "<Shift+Left>")
    type(waitForObject(":Actor Attributes_StyledText"), "<Shift+Left>")
    type(waitForObject(":Actor Attributes_StyledText"), "<Shift+Left>")
    type(waitForObject(":Actor Attributes_StyledText"), "1")
    mouseClick(waitForObjectItem(":Actor Attributes_Table", "4/1"), 431, 15, 0, Button.Button1)

    mouseClick(waitForObjectItem(":Actor Attributes_Table", "3/1"), 146, 13, 0, Button.Button1)
    mouseClick(waitForObject(":_FigureCanvas"), 181, 203, 0, Button.Button1)
    mouseClick(waitForObject(":_ImageFigure"), 21, 26, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Actor Attributes_Table", "4/1"), 27, 18, 0, Button.Button1)

    mouseClick(waitForObject(":Run the workflow from start to end until finished._ToolItem"))
    clickButton(waitForObject(":Save Resource.Yes_Button"))
    snooze(120)
    clickTab(waitForObject(":new_data_file1.h5_CTabItem"), 79, 14, 0, Button.Button1)
    expand(waitForObjectItem(":Tree_Tree", "entry"))
    expand(waitForObjectItem(":Tree_Tree", "dictionary"))
    mouseClick(waitForObjectItem(":Tree_Tree", "x"), 4, 7, 0, Button.Button1)
    clickTab(waitForObject(":Value_CTabItem"), 34, 14, 0, Button.Button1)
    
    widget = waitForObject(":Value_StyledText")
    text  = widget.text
    lines = text.split("\n")

    test.verify(lines[0] == "1.0", "Checking if first line is 1.0")

    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
