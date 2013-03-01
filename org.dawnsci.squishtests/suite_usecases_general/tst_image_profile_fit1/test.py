source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))

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
    openExample("001.img")
 
    # Now use profile tool
    doubleClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 31, 5, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Line Profile"))
    snooze(1)
    
    proxy = waitForObject(":ref-testscale_1_001.img_CTabItem")
    widget = proxy.control

    b = widget.bounds
    mouseDrag(widget, b.x+100, b.y+100, 300, 300, 0, Button.Button1)
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), 29, 7, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Peak Fitting"))
    mouseClick(waitForObject(":Create new profile._ToolItem"), 8, 5, 0, Button.Button1)    

    proxy  = waitForObject(":Line Profile_CTabItem")
    widget = proxy.control
    b = widget.bounds
    mouseDrag(widget, 100, 300, 100, 10, 0, Button.Button1)
    snooze(2) # While fit...

    # Check number of peaks
    clickTab(waitForObject(":Peak Fitting_CTabItem"), 51, 5, 0, Button.Button1)
    table   = waitForObject(":Peak Fitting_Table");
    test.verify(table.items.length == 1)
    
    mouseClick(waitForObject(":Number peaks to fit_ToolItem"), 30, 5, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Fit 3 Peaks"))
    snooze(2) # While fit...
    table   = waitForObject(":Peak Fitting_Table");
    test.verify(table.items.length == 3)
    
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
