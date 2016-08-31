source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_constants.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))

def main():
    
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Data Browsing (default)")
    
    snooze(5)
    vals = dawn_constants
    #expand data tree and open metal mix
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    for child in children:
        if "96356.dat" in child.text:
            doubleClick(child)
            break
    
    snooze(1)
    
    if(isEclipse4()):
        mouseClick(waitForObjectItem(":Data_Table_7", "3/0"), 7, 9, 0, Button.Button1)
    else:
        mouseClick(waitForObjectItem(":Data_Table", "3/0"), 6, 12, 0, Button.Button1)
    
    snooze(1)
    
    for child in children:
        if "metalmix.mca" in child.text:
            doubleClick(child)
            break
    
    snooze(1)
    
    if(isEclipse4()):
        mouseClick(waitForObjectItem(":Data_Table_5", "0/0"), 11, 15, 0, Button.Button1)
        mouseClick(waitForObjectItem(":Data_Table_5", "3/0"), 9, 12, 0, Button.Button1)
    else:
        mouseClick(waitForObjectItem(":Data_Table_2", "0/0"), 10, 13, 0, Button.Button1)
        mouseClick(waitForObjectItem(":Data_Table_2", "3/0"), 10, 12, 0, Button.Button1)
    mouseClick(waitForObject(":Plot data as separate plots_ToolItem"))
    
    snooze(1)
    
    for child in children:
        if "MoKedge_1_15.dat" in child.text:
            doubleClick(child)
            break
    
    snooze(1)
    
    if(isEclipse4()):
        mouseClick(waitForObjectItem(":Data_Table_6", "4/0"), 4, 15, 0, Button.Button1)
    else:
        mouseClick(waitForObjectItem(":Data_Table_3", "4/0"), 10, 14, 0, Button.Button1)
    
    snooze(1)
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "History"))  
    mouseClick(waitForObject(":View Menu_ToolItem_3"), 9, 11, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open 'History' in dedicated view"))
    
    if (not object.exists(":Add currently plotted plot(s) to history_ToolItem_3")):
        test.fail("History tool not active")
        snooze(1)
        clickTab(waitForObject(":MoKedge_1_15.dat_CTabItem"), 51, 12, 0, Button.Button1)
    
    mouseClick(waitForObject(":Add currently plotted plot(s) to history_ToolItem_3"))

    clickTab(waitForObject(":metalmix.mca_CTabItem"))
    mouseClick(waitForObject(":Add currently plotted plot(s) to history_ToolItem_3"))
    clickTab(waitForObject(":96356.dat_CTabItem"))
    
    conOb = waitForObject(":Configure Settings..._ToolItem")
    check_plotted_trace_name_yval(conOb,"sum","3.0E7","0.0")
    nameList = ['sum', 'ln(I0/It) (MoKedge_1_15.dat)', "Column_4 (metalmix.mca)", "Column_1 (metalmix.mca)"]
    check_plotted_traces_names(conOb, nameList)
    
    snooze(2)
    
    test.verify(waitForObject(":History_Table").getItemCount() ==3,"check table is populated")
    
    mouseClick(waitForObjectItem(":History_Table", "2/0"))
    
    check_plotted_traces_names(conOb, nameList[:3])

    snooze(1)
       
    mouseClick(waitForObject(":Delete selected_ToolItem_2"))
    
    check_plotted_traces_names(conOb, nameList[:3])
    
    snooze(1)

    mouseClick(waitForObject(":Clear history_ToolItem_2"))
    
    check_plotted_trace_name_yval(conOb, "sum", "3.0E7", "5000000.0")
    
    closeOrDetachFromDAWN()
