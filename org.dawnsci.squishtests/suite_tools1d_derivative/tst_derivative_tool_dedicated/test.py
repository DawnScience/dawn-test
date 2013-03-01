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
            continue
    
    mouseClick(waitForObjectItem(":Data_Table", "0/0"), 9, 7, 0, Button.Button1)
    
    #Check data has plotted by looking at graph settings
    conOb = waitForObject(":Configure Settings..._ToolItem")
    check_plotted_trace_name_yval(conOb,"Column_1","600.0","0.0")
    
    #Change to derivative and check again
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), 25, 8, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Derivative"))
    
    widget = waitForObject(":Derivative.Display f'(Data)_Button")
    test.verify(widget.getSelection(), "Check Default Selection")
    

    check_plotted_trace_name_yval(conOb, "Column_1'","300.0","-300.0")
    
    mouseClick(waitForObject(":Derivative_CTabCloseBox"), 11, 4, 0, Button.Button1)
    
    check_plotted_trace_name_yval(conOb,"Column_1","600.0","0.0")
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), 24, 12, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Derivative"))
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 10, 4, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open 'Derivative' in dedicated view"))
    
    check_plotted_trace_name_yval(conOb,"Column_1'","300.0","-300.0")
    
    for child in children:
        if "MoKedge_1_15.dat" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            continue
    
    mouseClick(waitForObjectItem(":Data_Table_2", "4/0"), 10, 7, 0, Button.Button1)
    
    conOb2 = waitForObject(":Configure Settings..._ToolItem_2")
    check_plotted_trace_name_yval(conOb2,"ln(I0/It)'","0.06","-0.02")
    
    mouseClick(waitForObject(":Derivative_CTabItem"), 10, 4, 0, Button.Button1)
    
    widget = waitForObject(":Derivative.Display f'(Data)_Button")
    mouseClick(widget, 5, 5, 0, Button.Button1)
    test.verify(widget.getSelection()==0, "Check click Selection")
    
    
    widget = waitForObject(":Derivative.Display Data_Button")
    mouseClick(widget, 5, 5, 0, Button.Button1)
    test.verify(widget.getSelection()==1, "Check click Selection")
    
    check_plotted_trace_name_yval(conOb2,"ln(I0/It)","-1.5","-2.75")

    clickTab(waitForObject(":metalmix.mca_CTabItem"), 64, 5, 0, Button.Button1)
    
    widget = waitForObject(":Derivative.Display f'(Data)_Button")
    test.verify(widget.getSelection(), "Check default Selection")
    
    check_plotted_trace_name_yval(conOb,"Column_1'","300.0","-300.0")


    closeOrDetachFromDAWN()