source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_constants.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))

def main():
    
    #Start using clean workspace
    startOrAttachToDAWN()
    
    vals = dawn_constants
    
    # Open data browsing perspective 
    openPerspective("Data Browsing (default)")
    
    #expand data tree and open metal mix
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    snooze(5)
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
    
    conOb = waitForObject(":Configure Settings..._ToolItem_3")
    #Verify all is correct on the first open of the tool

    doubleClick(waitForObject(":Derivative View_CTabItem"), 82, 5, 0, Button.Button1)

    check_plotted_trace_name_yval(conOb, "Column_1'", "250.0", "-300.0")

    widget = waitForObject(":First_ToolItem")
    test.verify(widget.item.getSelection(), "Check Default Selection is 1st Derivative")
    
    
    widget = waitForObject(":Original_ToolItem")
    test.verify(not widget.item.getSelection(), "Check Default Selection is not data")
    
    widget = waitForObject(":Second_ToolItem")
    test.verify(not widget.item.getSelection(), "Check Default Selection is not 2nd Derivative")
    
    doubleClick(waitForObject(":Derivative View_CTabItem"), 80, 8, 0, Button.Button1)
    
    closeOrDetachFromDAWN()
    
    
    
    
    