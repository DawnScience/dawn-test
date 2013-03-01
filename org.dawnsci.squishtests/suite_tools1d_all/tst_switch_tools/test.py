source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))

def the_actual_test():
    
    #Open each tool and check it closes ok when the next tool opens
    #Peak fitting
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), 25, 8, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Peak Fitting"))
    
    #fit peak
    c = waitForObject(":Plot_Composite")
    b = c.bounds

    test.log("Image at (%d, %d) is %d x %d" % (b.x,b.y, b.width, b.height))
    mouseDrag(c, b.x+b.width/2.35, b.y+b.height/4, int(b.width/7.5),0, 0, Button.Button1)
    snooze(1)
    
    #check being shown
    names = ["Column_3","Peak 1"]
    check_plotted_traces_names(waitForObject(":Configure Settings..._ToolItem"), names)
    
    #activate derivative tool, which should deactivate the peak fitting
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), 25, 8, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Derivative"))
    names = ["Peak 1","Column_3'"]
    #check_plotted_traces_names(waitForObject(":Configure Settings..._ToolItem"), names)
    check_plotted_trace_name_yval(waitForObject(":Configure Settings..._ToolItem"), "Peak 1", "400.0", "-400.0")
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), 25, 8, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Measurement"))
    #Check derivative tool has reset
    
    names = ["Peak 1","Column_3"]
    check_plotted_traces_names(waitForObject(":Configure Settings..._ToolItem"), names)
    check_plotted_trace_name_yval(waitForObject(":Configure Settings..._ToolItem"),"Peak 1", "800.0","0.0")
    
    #do measurement
    c = waitForObject(":Plot_Composite")
    b = c.bounds

    test.log("Image at (%d, %d) is %d x %d" % (b.x,b.y, b.width, b.height))
    mouseDrag(c, b.x+b.width/2.35, b.y+b.height/4, int(b.width/7.5),0, 0, Button.Button1)
    snooze(1)
    
    clickTab(waitForObject(":Measurement_CTabItem"), 61, 12, 0, Button.Button1)
    test.verify(waitForObjectItem(":Measurement_Table", "0/0").text == "Measurement 1", "Verify measurement text");
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), 25, 8, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Line Fitting"))
    
    #do fit
    c = waitForObject(":Plot_Composite")
    b = c.bounds

    test.log("Image at (%d, %d) is %d x %d" % (b.x,b.y, b.width, b.height))
    mouseDrag(c, b.x+b.width/2.35, b.y+b.height/4, int(b.width/7.5),0, 0, Button.Button1)
    snooze(1)
    
    names = ["Peak 1","Column_3", "Fit 1"]
    check_plotted_traces_names(waitForObject(":Configure Settings..._ToolItem"), names)
    
    test.verify(waitForObjectItem(":Line Fitting_Table", "0/0").text == "Column_3", "Verify measurement text");
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), 25, 8, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Clear tool"))
    
    mouseClick(waitForObject(":No tool_CTabCloseBox"), 12, 6, 0, Button.Button1)
    

def main():
    
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
    #and again
    the_actual_test()

    closeOrDetachFromDAWN()