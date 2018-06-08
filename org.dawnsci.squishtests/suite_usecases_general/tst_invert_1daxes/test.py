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

    #open and display 1d data
    openExample("metalmix.mca")
    mouseClick(waitForObjectItem(":Data_Table_6", "5/0"), 3, 12, 0, Button.Button1)
    
    #invert xaxis
    mouseClick(waitForObject(":Configure Settings..._ToolItem_4"), 5, 9, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    snooze(1)
    clickButton(waitForObject(":Change Settings.Invert Axis_Button"))
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    #check that the min and max have been changed
    mouseClick(waitForObject(":Configure Settings..._ToolItem_4"), 5, 9, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    widget = findObject(":Change Settings.Maximum_Text")
    upper = widget.text
    widget = findObject(":Change Settings.Minimum: _Text")
    lower = widget.text
    test.verify(upper=="0.0", "XAxis maximum has been changed successfully")
    test.verify(lower=="127.0", "XAxis minimum has been changed successfully")
#    test.verify(lower=="140.0", "XAxis minimum has been changed successfully")
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    snooze(1)
    
    #invert yaxis
    mouseClick(waitForObject(":Configure Settings..._ToolItem_4"), 9, 8, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    snooze(1)
    mouseClick(waitForObjectItem(":Select Axis_Combo", "Column_6(Y-Axis)"), 0, 0, 0, Button.NoButton)
    snooze(1)
#     mouseClick(waitForObject(":Axes.Change Settings_Group"), 13, 554, 0, Button.Button1)
#     snooze(3)
    clickButton(waitForObject(":Change Settings.Invert Axis_Button"))
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    #check that the min and max have been changed
    mouseClick(waitForObject(":Configure Settings..._ToolItem_4"), 5, 9, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    mouseClick(waitForObjectItem(":Select Axis_Combo", "Column_6(Y-Axis)"), 0, 0, 0, Button.NoButton)
    widget = findObject(":Change Settings.Maximum_Text")
    upper = widget.text
    widget = findObject(":Change Settings.Minimum: _Text")
    lower = widget.text
    test.verify(upper=="0.0", "YAxis maximum has been changed successfully")
    test.verify(lower=="535.0", "YAxis minimum has been changed successfully")
#    test.verify(lower=="600.0", "YAxis minimum has been changed successfully")
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    snooze(1)

    #revert inversion of xaxis
    mouseClick(waitForObject(":Configure Settings..._ToolItem_4"), 12, 1, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    clickButton(waitForObject(":Change Settings.Invert Axis_Button"))
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    #check that the min and max have been changed
    mouseClick(waitForObject(":Configure Settings..._ToolItem_4"), 5, 9, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    widget = findObject(":Change Settings.Maximum_Text")
    upper = widget.text
    widget = findObject(":Change Settings.Minimum: _Text")
    lower = widget.text
    test.verify(upper=="127.0", "XAxis maximum has been changed successfully")
#    test.verify(upper=="140.0", "XAxis maximum has been changed successfully")
    test.verify(lower=="0.0", "XAxis minimum has been changed successfully")
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    snooze(1)

    #revert inversion of yaxis
    mouseClick(waitForObject(":Configure Settings..._ToolItem_4"), 11, 7, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    mouseClick(waitForObjectItem(":Select Axis_Combo", "Column_6(Y-Axis)"), 0, 0, 0, Button.NoButton)
    clickButton(waitForObject(":Change Settings.Invert Axis_Button"))
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    #check that the min and max have been changed
    mouseClick(waitForObject(":Configure Settings..._ToolItem_4"), 5, 9, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    mouseClick(waitForObjectItem(":Select Axis_Combo", "Column_6(Y-Axis)"), 0, 0, 0, Button.NoButton)
    widget = findObject(":Change Settings.Maximum_Text")
    upper = widget.text
    widget = findObject(":Change Settings.Minimum: _Text")
    lower = widget.text
    test.verify(upper=="535.0", "YAxis maximum has been changed successfully")
#    test.verify(upper=="600.0", "YAxis maximum has been changed successfully")
    test.verify(lower=="0.0", "YAxis minimum has been changed successfully")
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))

    snooze(1)
    
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
    
