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
    openExample("001.img")
    
    snooze(1)

    # TODO FIXME Find way to iterate these actions one day.
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Pixel Information"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Line Profile"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Box Profile"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Radial Profile"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Azimuthal Profile"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Cross Hair Profile"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Masking"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Circle/Ellipse Fitting"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Zoom Profile"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Image History"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Diffraction"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Colour mapping"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Clear tool"))

    snooze(1)

    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()