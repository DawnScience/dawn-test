source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))

import os
from datetime import datetime

def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    openPerspective("Data Browsing (default)")
    openExample("metalmix.mca")
    
    snooze(1)


    doubleClick(waitForObjectItem(":Data_Table", "0/0"), 2, 5, 0, Button.Button1)
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Peak Fitting"))
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Derivative"))
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Measurement"))
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "History"))
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Line Fitting"))
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "XAFS Analysis"))
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Clear tool"))

    snooze(1)

    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()