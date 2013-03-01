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
    
    #Verify all is correct on the first open of the tool
    
    check_plotted_trace_name_yval(conOb, "Column_1'","300.0","-300.0")
    
    widget = waitForObject(":Derivative.Display f'(Data)_Button")
    test.verify(widget.getSelection(), "Check Default Selection is 1st Derivative")
    
    widget = waitForObject(":Derivative.Display Data_Button")
    test.verify(not widget.getSelection(), "Check Default Selection is not data")
    
    widget = waitForObject(":Derivative.Display f''(Data)_Button")
    test.verify(not widget.getSelection(), "Check Default Selection is not 2nd Derivative")
    
    wid = waitForObject(":View Menu_ToolItem_2")
    test.verify("View Menu" in wid.getToolTipText(), "View menu Tool Tip text correct")
    
    mouseClick(wid, 14, 7, 0, Button.Button1)
    
    popWid = waitForObjectItem(":Pop Up Menu", "Open cheat sheet for 'Derivative'")
    activateItem(popWid)
    
    test.verify(waitForObject(":Cheat Sheets.Derivative tool_Label"),"Cheat sheet opens")
    
    closeOrDetachFromDAWN()
    
    
    
    
    