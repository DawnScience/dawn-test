source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))

# This test makes sure we can start and stop DAWN
def main():
    vals = dawn_constants
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    
    # On a test you may add test code here 
    #Open data browsing perspective
    openPerspective("Data Browsing (default)") 
    openExample("001.img")
    snooze(1) 
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Line Profile"))
    clickTab(waitForObject(":Line Profile_CTabItem"), 64, 11, 0, Button.Button1)
    
    proxy = waitForObject(":ref-testscale_1_001.img_CTabItem")
    widget = proxy.control
    b = widget.bounds

    mouseDrag(widget, b.x+b.width/8, b.y+b.height/8, int(b.width/3),b.height/3, 0, Button.Button1)
    snooze(2) # While fit...

    
    system = getPlottingSystem("Line Profile")
    test.verify(system.getTraces().iterator().next().getData().getRank() == 1, "Check XY plot in profile")

    
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()