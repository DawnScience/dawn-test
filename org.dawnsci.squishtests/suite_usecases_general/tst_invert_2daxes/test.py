source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))

import os

# This test makes sure we can start and stop DAWN
def main():
    vals = dawn_constants
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    
    # On a test you may add test code here 
    #Open data browsing perspective
    openPerspective("Data Browsing")

    openExample("pow_M99S5_1_0001.cbf")
   
    #invert xaxis


#     startApplication("dawn")
#     clickButton(waitForObject(":Newer Workspace Version.Cancel_Button"))

    mouseClick(waitForObject(":Configure Settings..._ToolItem_2"), 5, 9, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    clickButton(waitForObject(":Change Settings.Invert Axis_Button"))
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    #check that the min and max have been changed
    mouseClick(waitForObject(":Configure Settings..._ToolItem_2"), 5, 9, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    widget = findObject(":Change Settings.Maximum_Text")
    upper = widget.text
    widget = findObject(":Change Settings.Minimum: _Text")
    lower = widget.text
    test.verify(upper=="0.0", "XAxis maximum has been changed successfully")
    test.verify(lower=="2463.0", "XAxis minimum has been changed successfully")
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    snooze(1)
    
    #invert yaxis
    mouseClick(waitForObject(":Configure Settings..._ToolItem_2"), 9, 8, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    mouseClick(waitForObjectItem(":Select Axis_Combo", "(Y-Axis)"), 0, 0, 0, Button.NoButton)
    mouseClick(waitForObject(":Axes.Change Settings_Group"), 13, 554, 0, Button.Button1)
    clickButton(waitForObject(":Change Settings.Invert Axis_Button"))
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    #check that the min and max have been changed
    mouseClick(waitForObject(":Configure Settings..._ToolItem_2"), 5, 9, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    mouseClick(waitForObjectItem(":Select Axis_Combo", "(Y-Axis)"), 0, 0, 0, Button.NoButton)
    widget = findObject(":Change Settings.Maximum_Text")
    upper = widget.text
    widget = findObject(":Change Settings.Minimum: _Text")
    lower = widget.text
    test.verify(upper=="2527.0", "YAxis maximum has been changed successfully")
    test.verify(lower=="0.0", "YAxis minimum has been changed successfully")
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    snooze(1)

    #revert inversion of xaxis
    mouseClick(waitForObject(":Configure Settings..._ToolItem_2"), 12, 1, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    clickButton(waitForObject(":Change Settings.Invert Axis_Button"))
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    #check that the min and max have been changed
    mouseClick(waitForObject(":Configure Settings..._ToolItem_2"), 5, 9, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    widget = findObject(":Change Settings.Maximum_Text")
    upper = widget.text
    widget = findObject(":Change Settings.Minimum: _Text")
    lower = widget.text
    test.verify(upper=="2463.0", "XAxis maximum has been changed successfully")
    test.verify(lower=="0.0", "XAxis minimum has been changed successfully")
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    snooze(1)

    #revert inversion of yaxis
    mouseClick(waitForObject(":Configure Settings..._ToolItem_2"), 11, 7, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    mouseClick(waitForObjectItem(":Select Axis_Combo", "(Y-Axis)"), 0, 0, 0, Button.NoButton)
    clickButton(waitForObject(":Change Settings.Invert Axis_Button"))
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    #check that the min and max have been changed
    mouseClick(waitForObject(":Configure Settings..._ToolItem_2"), 5, 9, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    mouseClick(waitForObjectItem(":Select Axis_Combo", "(Y-Axis)"), 0, 0, 0, Button.NoButton)
    widget = findObject(":Change Settings.Maximum_Text")
    upper = widget.text
    widget = findObject(":Change Settings.Minimum: _Text")
    lower = widget.text
    test.verify(upper=="0.0", "YAxis maximum has been changed successfully")
    test.verify(lower=="2527.0", "YAxis minimum has been changed successfully")
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))

    snooze(1)
    
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN() 
    
    
    
