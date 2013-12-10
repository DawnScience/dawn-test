source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_constants.py"))

def main():
    
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Data Browsing (default)")
    vals = dawn_constants
    #expand data tree and open metal mix
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    for child in children:
        if "metalmix.mca" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            continue
    
    mouseClick(waitForObjectItem(":Data_Table", "0/0"), 9, 7, 0, Button.Button1)
    
    #Check data has plotted by looking at graph settings
    conOb = waitForObject(":Configure Settings..._ToolItem")
    check_plotted_trace_name_yval(conOb,"Column_1","600.0","0.0")
    
    #Change to measurement and check again
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Measurement"))
    
    #Check tool tab has opened correctly
    test.verify(waitForObject(":Measurement_CTabItem"), "measurement tab there")
    
    #wid = waitForObject(":_ToolBar_6")
    
    #test.verify(wid.getItem(0).getToolTipText() == "Create new measurement.", "Expected: " + "Create new measurement." + " Actual: " + wid.getItem(3).getToolTipText())
    #test.verify(wid.getItem(5).getToolTipText() == "Copies the region values as text to clipboard which can then be pasted externally.",  "Expected: " + "Copies the region values as text to clipboard which can then be pasted externally." + " Actual: " + wid.getItem(5).getToolTipText())
    #test.verify(wid.getItem(6).getToolTipText() == "Delete selected region, if there is one.",  "Expected: " + "Delete selected region, if there is one." + " Actual: " + wid.getItem(6).getToolTipText())
    
    test.verify(object.exists(":Name_TableColumn"), "name column there")
    test.verify(object.exists(":Region Type_TableColumn"), "region column there")
    tab = waitForObject(":Measurement_Table")
    #starts with one empty item
    test.verify(tab.getItemCount()==1,"table empty")
    
    c = waitForObject(":Plot_Composite")
    b = c.bounds

    test.log("Image at (%d, %d) is %d x %d" % (b.x,b.y, b.width, b.height))
    mouseDrag(c, b.x+b.width/3, b.y+b.height/3, int(b.width/1.7),b.height/3, 0, Button.Button1)
    snooze(1)
    
    test.verify(tab.getItemCount()==1,"one line in table")
    
    mouseClick(waitForObject(":Create new measurement_ToolItem"), 16, 8, 0, Button.Button1)
    
    c = waitForObject(":Plot_Composite")
    b = c.bounds

    test.log("Image at (%d, %d) is %d x %d" % (b.x,b.y, b.width, b.height))
    mouseDrag(c, b.x+b.width/2, b.y+b.height/3, int(b.width/3),b.height/5, 0, Button.Button1)
    snooze(1)
    
    test.verify(tab.getItemCount()==2,"two line in table")
    #check cheat sheet opens
    mouseClick(waitForObject(":View Menu_ToolItem_3"), 9, 6, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open cheat sheet for 'Measurement'"))
    
    test.verify(object.exists(":Cheat Sheets_CTabItem"), "region column there")
    
    closeOrDetachFromDAWN()


    