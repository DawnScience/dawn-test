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
            break
    
    mouseClick(waitForObject(":Plot data as separate plots_ToolItem"), 12, 12, 0, Button.Button1)
    
    mouseClick(waitForObjectItem(":Data_Table", "0/0"), 8, 12, 0, Button.Button1)
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem_2"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "History"))
    
    mouseClick(waitForObject(":View Menu_ToolItem_3"), 11, 12, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open 'History' in dedicated view"))
    mouseClick(waitForObject(":Add currently plotted plot(s) to history_ToolItem_3"), 13, 15, 0, Button.Button1)
    
    if (not object.exists(":Add currently plotted plot(s) to history_ToolItem_3")):
        test.fail("History tool not active")
        clickTab(waitForObject(":metalmix.mca_CTabItem"), 83, 3, 0, Button.Button1)
        snooze(1)
    
    mouseClick(waitForObject(":Add currently plotted plot(s) to history_ToolItem_3"), 21, 21, 0, Button.Button1)
    mouseClick(waitForObjectItem(":History_Table", "0/0"), 9, 14, 0, Button.Button1)
    mouseClick(waitForObject(":XY plotting tools_ToolItem_2"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Derivative View"))
    
    conOb = waitForObject(":Configure Settings..._ToolItem_4")
#    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
#    conOb = waitForObject(":Configure Settings..._ToolItem_2")

    doubleClick(waitForObject(":Derivative View_CTabItem"), 59, 14, 0, Button.Button1)
    check_plotted_trace_name_yval(conOb, "Column_1'", "300.0", "-300.0")
    doubleClick(waitForObject(":Derivative View_CTabItem"), 59, 14, 0, Button.Button1)
    
    mouseClick(waitForObjectItem(":History_Table", "0/0"), 11, 15, 0, Button.Button1)


    #nameList = ['sum', 'ln(I0/It) (MoKedge_1_15.dat)', "Column_1 (metalmix.mca)", "Column_4 (metalmix.mca)"]
    #check_plotted_traces_names(conOb, nameList)
    doubleClick(waitForObject(":Derivative View_CTabItem"), 59, 14, 0, Button.Button1)
    check_plotted_trace_name_yval(conOb,"Column_1'","600.0","-400.0")
    doubleClick(waitForObject(":Derivative View_CTabItem"), 59, 14, 0, Button.Button1)
    
    mouseClick(waitForObject(":Add currently plotted plot(s) to history_ToolItem_3"), 16, 14, 0, Button.Button1)
    
    mouseClick(waitForObject(":First_ToolItem"), 19, 12, 0, Button.Button1)
    mouseClick(waitForObject(":Second_ToolItem"), 14, 13, 0, Button.Button1)
#    clickButton(waitForObject(":Derivative.Display f'(Data)_Button"))
#
#    
#    clickButton(waitForObject(":Derivative.Display f''(Data)_Button"))
    
    mouseClick(waitForObject(":Add currently plotted plot(s) to history_ToolItem_3"), 21, 21, 0, Button.Button1)


    mouseClick(waitForObject(":Derivative View_CTabCloseBox"), 13, 12, 0, Button.Button1)
  #  mouseClick(waitForObject(":Derivative_CTabCloseBox"), 8, 5, 0, Button.Button1)
    

    mouseClick(waitForObject(":metalmix.mca_CTabItem"), 80, 8, 0, Button.Button1)
    mouseClick(waitForObjectItem(":History_Table", "0/0"), 9, 14, 0, Button.Button1)

    mouseClick(waitForObjectItem(":History_Table", "1/0"), 9, 14, 0, Button.Button1)
    mouseClick(waitForObjectItem(":History_Table", "2/0"), 9, 14, 0, Button.Button1)
    
    mouseClick(waitForObjectItem(":History_Table", "2/0"), 9, 14, 0, Button.Button1)
    
    conOb = waitForObject(":Configure Settings..._ToolItem_2")
    
    check_plotted_trace_name_yval(conOb,"Column_1","600.0","-400.0")

    mouseClick(waitForObjectItem(":History_Table", "1/0"), 9, 14, 0, Button.Button1)

    check_plotted_trace_name_yval(conOb,"Column_1","600.0","-400.0")
    

    closeOrDetachFromDAWN()
