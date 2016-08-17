source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_constants.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))

def main():
    
    #Start using clean workspace
    startOrAttachToDAWN()
    
    vals = dawn_constants;
    
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
    
    if(isEclipse4()):
        mouseClick(waitForObjectItem(":Data_Table_3", "0/0"), 9, 7, 0, Button.Button1)
    else:
        mouseClick(waitForObjectItem(":Data_Table", "0/0"), 9, 7, 0, Button.Button1)
    
    #Check data has plotted by looking at graph settings
    conOb = waitForObject(":Configure Settings..._ToolItem")
    check_plotted_trace_name_yval(conOb,"Column_1","600.0","0.0")
    
    #Change to derivative and check again
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Derivative View"))

    mouseClick(waitForObject(":View Menu_ToolItem_2"), 15, 14, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open 'Derivative View' in dedicated view"))
    
    conOb = waitForObject(":Configure Settings..._ToolItem_4")

    check_plotted_trace_name_yval(conOb,"Column_1'","250.0","-300.0")
    
    for child in children:
        if "MoKedge_1_15.dat" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            continue
    
    if(isEclipse4()):
        mouseClick(waitForObjectItem(":Data_Table_4", "4/0"), 10, 7, 0, Button.Button1)
    else:
        mouseClick(waitForObjectItem(":Data_Table_2", "4/0"), 10, 7, 0, Button.Button1)
    
    mouseClick(waitForObject(":Derivative View_CTabItem"), 51, 7, 0, Button.Button1)
    conOb2 = waitForObject(":Configure Settings..._ToolItem_4")
    check_plotted_trace_name_yval(conOb2, "ln(I0/It)'", "0.05", "-0.02")
    
    mouseClick(waitForObject(":Original_ToolItem_2"), 10, 14, 0, Button.Button1)
    mouseClick(waitForObject(":First_ToolItem_2"), 9, 11, 0, Button.Button1)
    check_plotted_trace_name_yval(conOb2, "ln(I0/It)", "-1.3999999999999997", "-2.8")

    clickTab(waitForObject(":metalmix.mca_CTabItem"), 64, 5, 0, Button.Button1)
    
    check_plotted_trace_name_yval(conOb,"Column_1'","250.0","-300.0")

    closeOrDetachFromDAWN()