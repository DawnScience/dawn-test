source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))

import os
from datetime import datetime

def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN(vmArgs="-Dorg.dawnsci.histogram.v1.x.colourMapping=true")
    openPerspective("Data Browsing")
    openExample("001.img")
    vals = dawn_constants
    snooze(1)

    # TODO FIXME Find way to iterate these actions one day.
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Pixel Information"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Profile"))
    activateItem(waitForObjectItem(":Profile_Menu", "Line Profile"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Profile"))
    activateItem(waitForObjectItem(":Profile_Menu", "Box Profile"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Profile"))
    activateItem(waitForObjectItem(":Profile_Menu", "Radial Profile"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Profile"))
    activateItem(waitForObjectItem(":Profile_Menu", "Azimuthal Profile"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Profile"))
    activateItem(waitForObjectItem(":Profile_Menu", "Cross Hair Profile"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Masking"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Circle/Ellipse Fitting"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Profile"))
    activateItem(waitForObjectItem(":Profile_Menu", "Zoom Profile"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Image History"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Science"))
    activateItem(waitForObjectItem(":Science_Menu", "Diffraction"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Colour mapping"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Clear tool"))

    snooze(1)

    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()