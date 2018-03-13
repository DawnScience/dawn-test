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
    openPerspective("Data Browsing")


    openExternalFile("ref-testscale_1_001.img")
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Masking"))
    
    mouseClick(waitForObject(":Square brush_ToolItem"), 16, 8, 0, Button.Button1)
    
    mouseClick(waitForObject(":Set pen size to 10_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Pen size of 64"))
  
    
    proxy = waitForObject(":ref-testscale_1_001.img_CTabItem")
    widget = proxy.control
    b = widget.bounds
    mouseDrag(widget, b.x+100, b.y+100, 300, 300, 0, Button.Button1)
    snooze(2) # While zoom...
    
    system = getPlottingSystem("ref-testscale_1_001.img")

    test.verify(system.getTraces().size() == 1)

    test.passes("One trace plotted") 

    imageTrace = system.getTraces().iterator().next()
    imageData  = imageTrace.getData()
    test.verify(imageData!=None)
    
    maskData  = imageTrace.getMask()
    test.verify(maskData!=None)


    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()