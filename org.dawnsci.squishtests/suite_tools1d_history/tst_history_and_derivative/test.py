source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))

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
            break
    
    mouseClick(waitForObject(":Plot data as separate plots_ToolItem"), 12, 12, 0, Button.Button1)
    
    mouseClick(waitForObjectItem(":Data_Table", "0/0"), 8, 12, 0, Button.Button1)
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem_2"), 28, 16, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "History"))
    
    mouseClick(waitForObject(":Add currently plotted plot(s) to history_ToolItem"), 21, 21, 0, Button.Button1)
    mouseClick(waitForObjectItem(":History_Table", "0/0"), 9, 14, 0, Button.Button1)
    mouseClick(waitForObject(":XY plotting tools_ToolItem_2"), 25, 18, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Derivative"))
    
    conOb = waitForObject(":Configure Settings..._ToolItem_2")

    check_plotted_trace_name_yval(conOb,"Column_1'","300.0","-300.0")
    
    mouseClick(waitForObjectItem(":History_Table", "0/0"), 11, 15, 0, Button.Button1)

    #nameList = ['sum', 'ln(I0/It) (MoKedge_1_15.dat)', "Column_1 (metalmix.mca)", "Column_4 (metalmix.mca)"]
    #check_plotted_traces_names(conOb, nameList)
    check_plotted_trace_name_yval(conOb,"Column_1'","600.0","-400.0")
    
    mouseClick(waitForObject(":Add currently plotted plot(s) to history_ToolItem"), 16, 14, 0, Button.Button1)
    
    clickButton(waitForObject(":Derivative.Display f'(Data)_Button"))
    
    clickButton(waitForObject(":Derivative.Display f''(Data)_Button"))
    
    mouseClick(waitForObject(":Add currently plotted plot(s) to history_ToolItem"), 21, 21, 0, Button.Button1)


    mouseClick(waitForObject(":Derivative_CTabCloseBox"), 8, 5, 0, Button.Button1)
    
    mouseClick(waitForObjectItem(":History_Table", "0/0"), 9, 14, 0, Button.Button1)
    mouseClick(waitForObjectItem(":History_Table", "1/0"), 9, 14, 0, Button.Button1)
    mouseClick(waitForObjectItem(":History_Table", "2/0"), 9, 14, 0, Button.Button1)
    
    mouseClick(waitForObjectItem(":History_Table", "2/0"), 9, 14, 0, Button.Button1)
    
    check_plotted_trace_name_yval(conOb,"Column_1 (metalmix.mca)","600.0","-400.0")

    mouseClick(waitForObjectItem(":History_Table", "1/0"), 9, 14, 0, Button.Button1)

    check_plotted_trace_name_yval(conOb,"Column_1 (metalmix.mca)","600.0","-400.0")
    

    closeOrDetachFromDAWN()