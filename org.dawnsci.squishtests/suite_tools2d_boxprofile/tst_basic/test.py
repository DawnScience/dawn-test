source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_constants.py"))

# This test makes sure we can start and stop DAWN
def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    
    # On a test you may add test code here 
    #Open data browsing perspective
    openPerspective("Data Browsing (default)")
    vals = dawn_constants
    snooze(5)
    openAndClearErrorLog()
    
    openExample("001.img")
    snooze(1)
    

    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Box Profile"))
    
    c = waitForObject(":Image_Composite")
    b = c.bounds

    mouseDrag(c, b.x+b.width/8, b.y+b.height/3, int(b.width/4),b.height/3, 0, Button.Button1)

    snooze(2) # While fit...

    check_plotted_traces_names(waitForObject(":Configure Settings..._ToolItem_2"),["X Profile 1","Y Profile 1"])

    mouseClick(waitForObject(":View Menu_ToolItem_2"), 15, 7, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open 'Box Profile' in dedicated view"))
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 13, 4, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open cheat sheet for 'Box Profile'"))
    mouseClick(waitForObject(":Cheat Sheets_CTabCloseBox"), 9, 9, 0, Button.Button1)

    system = getPlottingSystem("Box Profile")
    
    tList = system.getTraces()
    
    test.verify(tList.size() == 2, "2 traces in plot")
    
    tArray = tList.toArray()
    test.verify(tArray.at(0).getName() == "X Profile 1", "verify trace name")
    test.verify(tArray.at(1).getName() == "Y Profile 1", "verify trace name")
    
    verifyAndClearErrorLog()
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()