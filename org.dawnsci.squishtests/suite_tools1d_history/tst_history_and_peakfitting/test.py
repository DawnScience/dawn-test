source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_constants.py"))

def main():
    
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Data Browsing (default)")
    vals = dawn_constants
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    for child in children:
        if "metalmix.mca" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            break
    
    mouseClick(waitForObject(":Plot data as separate plots_ToolItem"), 12, 12, 0, Button.Button1)
    
    mouseClick(waitForObjectItem(":Data_Table", "0/0"), 18, 7, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table", "0/0"), 3, 13, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table", "1/0"), 7, 6, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table", "2/0"), 11, 10, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table", "3/0"), 9, 3, 0, Button.Button1)
    mouseClick(waitForObject(":XY plotting tools_ToolItem_2"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "History"))
    mouseClick(waitForObject(":Add currently plotted plot(s) to history_ToolItem"), 16, 12, 0, Button.Button1)
    clickTab(waitForObject(":Data_CTabItem"), 32, 11, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table", "3/0"), 10, 14, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table", "2/0"), 7, 9, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table", "1/0"), 10, 12, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table", "0/0"), 12, 9, 0, Button.Button1)
    clickTab(waitForObject(":History_CTabItem"), 30, 18, 0, Button.Button1)
    mouseClick(waitForObject(":XY plotting tools_ToolItem_2"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Peak Fitting"))
    
    
    c = waitForObject(":Plot_Composite")
    b = c.bounds

    test.log("Image at (%d, %d) is %d x %d" % (b.x,b.y, b.width, b.height))
    mouseDrag(c, b.x+b.width/3, b.y+b.height/3, int(b.width/1.7),b.height/3, 0, Button.Button1)
    snooze(1)
    
    mouseClick(waitForObject(":Choose trace for fit._ToolItem"), 25, 7, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Select all"))
    
    snooze(5)
    
    test.verify(waitForObjectItem(":Peak Fitting_Table", "0/0").text == "Column_4 (metalmix.mca)")
    test.verify(waitForObjectItem(":Peak Fitting_Table", "1/0").text == "Column_3 (metalmix.mca)")
    test.verify(waitForObjectItem(":Peak Fitting_Table", "2/0").text == "Column_2 (metalmix.mca)")
    test.verify(waitForObjectItem(":Peak Fitting_Table", "3/0").text == "Column_1")
    
    closeOrDetachFromDAWN()