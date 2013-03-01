source(findFile("scripts", "dawn_global_startup.py"))

def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    
    # On a test you may add test code here 
    #Open data browsing perspective
    openPerspective("Data Browsing (default)")
    
    #expand data tree and open metal mix, the date/time on the metal mix 
    #file may change so we iterate through all the children of the "examples"
    #folder and open "metalmix.mca"
 
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    for child in children:
        if "metalmix" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)

    mouseClick(waitForObjectItem(":Data_Table", "0/0"), 6, 10, 0, Button.Button1)
    snooze(1)
    mouseClick(waitForObject(":Configure Settings..._ToolItem_2"), 12, 3, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    clickButton(waitForObject(":Change Settings.Log_Button"))
    clickButton(waitForObject(":Configure Graph Settings.Apply_Button"))
    mouseClick(waitForObjectItem(":Select Axis_Combo", "(Y-Axis)"), 0, 0, 0, Button.NoButton)
    clickButton(waitForObject(":Change Settings.Log_Button"))
    clickButton(waitForObject(":Configure Graph Settings.Apply_Button"))
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    snooze(1)
    # Check axis values    
    mouseClick(waitForObject(":Configure Settings..._ToolItem_2"), 12, 3, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    widget = waitForObject(":Change Settings.Log_Button")
    test.verify(widget.selection == True)


    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
