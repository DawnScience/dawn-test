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
    openExample("user_interface_example.moml", "workflows", "examples")
    
    widget = waitForObject(":user_interface_example.moml.Edit_CTabItem", 3000)
    clickTab(widget)

    mouseClick(waitForObject(":Run the workflow from start to end until finished._ToolItem"))
    waitForObject(":Set Values_Table",120000)
    mouseClick(waitForObjectItem(":Set Values_Table", "0/1"), 19, 10, 0, Button.Button1)
    type(waitForObject(":Set Values_StyledText"), "fred")
    mouseClick(waitForObjectItem(":Set Values_Table", "1/1"), 25, 11, 0, Button.Button1)
    type(waitForObject(":Set Values_Spinner"), "2")
    mouseClick(waitForObjectItem(":Set Values_Table", "2/1"), 22, 7, 0, Button.Button1)
    type(waitForObject(":Set Values_Spinner"), "3")
    
    mouseClick(waitForObjectItem(":Set Values_Table", "3/1"), 107, 7, 0, Button.Button1)
    type(waitForObject(":Set Values_StyledText"), "<Ctrl+a>")
    type(waitForObject(":Set Values_StyledText"), "opid1454")
    mouseClick(waitForObjectItem(":Set Values_Table", "5/1"), 25, 6, 0, Button.Button1)
    type(waitForObject(":Set Values_Spinner"), "6")
    mouseClick(waitForObjectItem(":Set Values_Table", "6/1"), 207, 6, 0, Button.Button1)
    mouseClick(waitForObject(":Set Values_StyledText"), 205, 14, 0, Button.Button1)
    type(waitForObject(":Set Values_StyledText"), "<Ctrl+a>")
    type(waitForObject(":Set Values_StyledText"), "opid144_1_789.img")
    mouseClick(waitForObjectItem(":Set Values_Table", "7/1"), 80, 13, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Set Values_Combo", "X-low"), 0, 0, 0, Button.NoButton)

    clickButton(waitForObject(":Set Values.Continue_Button"))
    expand(waitForObjectItem(":Tree_Tree", "entry", 120000))
    expand(waitForObjectItem(":Tree_Tree", "dictionary"))
    
    checkItem("comments", "fred");
    checkItem("firstImNum", "2");
    checkItem("numImages", "3");
    checkItem("prefix", "opid1454");
    checkItem("rawDataDir", "/data/id14/eh4/inhouse/opid144/20110117/RAW_DATA");
    checkItem("runNum", "6");
    checkItem("template", "opid144_1_789.img");
    checkItem("xstallConf", "X-low");

    snooze(2)

    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
    
    
    
def checkItem(item, value):
    
    mouseClick(waitForObjectItem(":Tree_Tree", item))
    clickTab(waitForObject(":Value_CTabItem"), 26, 13, 0, Button.Button1)
    widget = waitForObject(":Value_StyledText")
    text  = widget.text
    lines = text.split("\n")
    test.verify(lines[0] == value,"Expected: " + value + " Actual: " + lines[0])

