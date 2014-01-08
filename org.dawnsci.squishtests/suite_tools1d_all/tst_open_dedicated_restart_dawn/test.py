source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_constants.py"))

def the_actual_test():
    vals = dawn_constants
    #Open each tool then make dedicated
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "History"))
    #Peak fitting
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Peak Fitting"))
    
    #fit peak
    c = waitForObject(":Plot_Composite")
    b = c.bounds

    test.log("Image at (%d, %d) is %d x %d" % (b.x,b.y, b.width, b.height))
    mouseDrag(c, b.x+b.width/2.35, b.y+b.height/4, int(b.width/7.5),0, 0, Button.Button1)
    snooze(1)
    
    #check being shown
    names = ["Column_3","Peak 1"]
    check_plotted_traces_names(waitForObject(":Configure Settings..._ToolItem"), names)
    
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 3, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open 'Peak Fitting' in dedicated view"))
    
    #activate derivative tool, which should deactivate the peak fitting
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Derivative"))
    names = ["Column_3'","Peak 1"]
    check_plotted_traces_names(waitForObject(":Configure Settings..._ToolItem"), names)
    #check_plotted_trace_name_yval(waitForObject(":Configure Settings..._ToolItem"), "Column_3'", "400.0", "-400.0")
    
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 4, 5, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open 'Derivative' in dedicated view"))
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Measurement"))
    #Check derivative tool has not reset
    
    check_plotted_traces_names(waitForObject(":Configure Settings..._ToolItem"), names)
    check_plotted_trace_name_yval(waitForObject(":Configure Settings..._ToolItem"),"Column_3'", "400.0","-400.0")
    
    #do measurement
    c = waitForObject(":Plot_Composite")
    b = c.bounds

    test.log("Image at (%d, %d) is %d x %d" % (b.x,b.y, b.width, b.height))
    mouseDrag(c, b.x+b.width/2.35, b.y+b.height/4, int(b.width/7.5),0, 0, Button.Button1)
    snooze(1)
    
    clickTab(waitForObject(":Measurement_CTabItem"), 61, 12, 0, Button.Button1)
    #test.verify(waitForObjectItem(":Measurement_Table", "0/0").text == "Measurement 1", "Verify measurement text");
    
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 3, 7, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open 'Measurement' in dedicated view"))
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Line Fitting"))
    
    #do fit
    c = waitForObject(":Plot_Composite")
    b = c.bounds

    test.log("Image at (%d, %d) is %d x %d" % (b.x,b.y, b.width, b.height))
    mouseDrag(c, b.x+b.width/2.35, b.y+b.height/4, int(b.width/7.5),0, 0, Button.Button1)
    snooze(1)
    
    names = ["Column_3'","Peak 1", "Fit 1"]
    check_plotted_traces_names(waitForObject(":Configure Settings..._ToolItem"), names)
    
    test.verify(waitForObjectItem(":Line Fitting_Table", "0/0").text == "Column_3'", "Verify measurement text");
    
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 12, 14, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open 'Line Fitting' in dedicated view"))
    
    
    

def main():
    vals = dawn_constants
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Data Browsing (default)")
    
    #expand data tree and open metal mix
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    for child in children:
        if "metalmix.mca" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            continue
    
    mouseClick(waitForObjectItem(":Data_Table", "2/0"), 9, 5, 0, Button.Button1)
    
    snooze(1)

    the_actual_test()
    
    closeOrDetachFromDAWN()
    
    startOrAttachToDAWNOnly(False)

    mouseClick(waitForObject(":Line Fitting_CTabCloseBox"), 8, 11, 0, Button.Button1)
    mouseClick(waitForObject(":Data_CTabCloseBox"), 11, 9, 0, Button.Button1)
    mouseClick(waitForObject(":No tool_CTabCloseBox"), 5, 9, 0, Button.Button1)
    mouseClick(waitForObject(":Peak Fitting_CTabCloseBox"), 6, 7, 0, Button.Button1)
    mouseClick(waitForObject(":Derivative_CTabCloseBox"), 7, 10, 0, Button.Button1)
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem"),vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Line Fitting"))
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 8, 8, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open 'Line Fitting' in dedicated view"))
    test.verify(object.exists(":Line Fitting_CTabItem"), "Line fitting there")
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem"),vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Peak Fitting"))
    mouseClick(waitForObject(":View Menu_ToolItem_3"), 3, 6, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open 'Peak Fitting' in dedicated view"))
    test.verify(object.exists(":Peak Fitting_CTabItem"), "Peak fitting there")
    
    snooze(1)
    

    closeOrDetachFromDAWN()
