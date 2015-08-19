source(findFile("scripts", "dawn_global_startup.py"))

# This test makes sure we can start and stop DAWN
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
        if "2.img" in child.text:
            doubleClick(child)
            continue
    
    snooze(3)#while the file opens
    
    mouseClick(waitForObject(":Configure Settings..._ToolItem"))
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    mouseClick(waitForObject(":Change Settings.Title: _Text"), 64, 8, 0, Button.Button1)
    type(waitForObject(":Change Settings.Title: _Text"), "<Backspace>")
    type(waitForObject(":Change Settings.Title: _Text"), "<Backspace>")
    type(waitForObject(":Change Settings.Title: _Text"), "<Backspace>")
    type(waitForObject(":Change Settings.Title: _Text"), "<Backspace>")
    type(waitForObject(":Change Settings.Title: _Text"), "<Backspace>")
    type(waitForObject(":Change Settings.Title: _Text"), "<Backspace>")
    type(waitForObject(":Change Settings.Title: _Text"), "Test X")
    clickButton(waitForObject(":Configure Graph Settings.Apply_Button"))
    mouseClick(waitForObjectItem(":Select Axis_Combo", "Y-Axis(Y-Axis)"), 61, 15, 0, Button.Button1)
    mouseClick(waitForObject(":Change Settings.Title: _Text"), 32, 12, 0, Button.Button1)

    type(waitForObject(":Change Settings.Title: _Text"), "e")
    type(waitForObject(":Change Settings.Title: _Text"), "<Backspace>")
    type(waitForObject(":Change Settings.Title: _Text"), "Test Y")
    clickButton(waitForObject(":Configure Graph Settings.Apply_Button"))

    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))   
    
    # Check axis values    
    mouseClick(waitForObject(":Configure Settings..._ToolItem"), 4, 7, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    widget = waitForObject(":Change Settings.Title: _Text")
    test.verify(widget.text == "Test X")
            
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
