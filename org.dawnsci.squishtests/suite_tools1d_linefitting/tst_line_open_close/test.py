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
        if "96356.dat" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            continue
    
    mouseClick(waitForObjectItem(":Data_Table", "2/0"), 9, 7, 0, Button.Button1)
    
    snooze(5)
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Line Fitting"))
    
    test.verify(waitForObject(":Line Fitting_CTabItem"), "peak fitting there")
    
    wid = waitForObject(":_ToolBar_4")
    
    test.verify(wid.getItem(0).getToolTipText() == "New fit selection.", "Test tooltips")
    test.verify(wid.getItem(2).getToolTipText() == "Show fitting traces.", "Test tooltips")
    test.verify(wid.getItem(3).getToolTipText() == "Show selection regions for fit", "Test tooltips")
    
    test.verify(object.exists(":Trace_TableColumn"), "trace column there")
    test.verify(object.exists(":Name_TableColumn"), "name column there")
    tab = waitForObject(":Line Fitting_Table")
    test.verify(tab.getItemCount()==0,"table empty")
    
    c = waitForObject(":Plot_Composite")
    b = c.bounds

    test.log("Image at (%d, %d) is %d x %d" % (b.x,b.y, b.width, b.height))
    mouseDrag(c, b.x+b.width/3, b.y+b.height/3, int(b.width/1.7),b.height/3, 0, Button.Button1)
    snooze(1)
    
    test.verify(tab.getItemCount()==1,"one line in table")
    
    conOb = waitForObject(":Configure Settings..._ToolItem_2")

    nameList = ["max","Fit 1"]
    check_plotted_traces_names(conOb, nameList)

    closeOrDetachFromDAWN()
    