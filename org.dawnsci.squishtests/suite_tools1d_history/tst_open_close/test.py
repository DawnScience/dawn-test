source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))

def main():
    
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Data Browsing (default)")
    
    snooze(5)
    
    #expand data tree and open metal mix
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    for child in children:
        if "96356.dat" in child.text:
            doubleClick(child)
            break
    
    snooze(1)
    
    mouseClick(waitForObjectItem(":Data_Table", "4/0"))
    
    snooze(1)
    
    for child in children:
        if "metalmix.mca" in child.text:
            doubleClick(child)
            break
    
    snooze(1)
    
    mouseClick(waitForObjectItem(":Data_Table_2", "0/0"))
    mouseClick(waitForObjectItem(":Data_Table_2", "3/0"))
    mouseClick(waitForObject(":Plot data as separate plots_ToolItem"))
    
    snooze(1)
    
    for child in children:
        if "MoKedge_1_15.dat" in child.text:
            doubleClick(child)
            break
    
    snooze(1)
    
    mouseClick(waitForObjectItem(":Data_Table_3", "4/0"))
    
    snooze(1)
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "History"))
    
    mouseClick(waitForObject(":Add currently plotted plot(s) to history_ToolItem"))
    clickTab(waitForObject(":metalmix.mca_CTabItem"))
    mouseClick(waitForObject(":Add currently plotted plot(s) to history_ToolItem"))
    clickTab(waitForObject(":96356.dat_CTabItem"))
    
    conOb = waitForObject(":Configure Settings..._ToolItem")
    check_plotted_trace_name_yval(conOb,"sum","3.0E7","0.0")
    nameList = ['sum', 'ln(I0/It) (MoKedge_1_15.dat)', "Column_1 (metalmix.mca)", "Column_4 (metalmix.mca)"]
    check_plotted_traces_names(conOb, nameList)
    
    snooze(2)
    
    test.verify(waitForObject(":History_Table").getItemCount() ==3,"check table is populated")
    
    mouseClick(waitForObjectItem(":History_Table", "2/0"))
    
    check_plotted_traces_names(conOb, nameList[:3])
    
    mouseClick(waitForObject(":Delete selected_ToolItem"))
    
    check_plotted_traces_names(conOb, nameList[:3])
    
    mouseClick(waitForObject(":Clear history_ToolItem"))
    
    check_plotted_trace_name_yval(conOb,"sum","3.0E7","0.0")
    
    closeOrDetachFromDAWN()
