source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_constants.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))

def main():
    
    #Start using clean workspace
    startOrAttachToDAWN()
    
    vals = dawn_constants
    
    # Open data browsing perspective 
    openPerspective("Data Browsing")
    
    #expand data tree and open metal mix
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    snooze(1)
    
    for child in children:
        if "metalmix.mca" in child.text:
            doubleClick(child)
            continue
    
    snooze(1)
    
#     mouseClick(waitForObject(":Plot data as separate plots_ToolItem"), 12, 8, 0, Button.Button1)
    
    #open 4 traces
    if(isEclipse4()):
        mouseClick(waitForObjectItem(":Data_Table_3", "0/0"), 9, 7, 0, Button.Button1)
        mouseClick(waitForObjectItem(":Data_Table_3", "1/0"), 10, 5, 0, Button.Button1)
        mouseClick(waitForObjectItem(":Data_Table_3", "0/2"), 19, 13, 0, Button.Button1)
        mouseClick(waitForObjectItem(":_List", "Y1"), 14, 13, 0, Button.Button1)
        mouseClick(waitForObjectItem(":Data_Table_3", "2/0"), 6, 2, 0, Button.Button1)
        mouseClick(waitForObjectItem(":Data_Table_3", "3/0"), 10, 10, 0, Button.Button1)
    else:
        mouseClick(waitForObjectItem(":Data_Table", "0/0"), 9, 7, 0, Button.Button1)
        mouseClick(waitForObjectItem(":Data_Table", "1/0"), 10, 5, 0, Button.Button1)
        mouseClick(waitForObjectItem(":Data_Table", "2/0"), 6, 2, 0, Button.Button1)
        mouseClick(waitForObjectItem(":Data_Table", "3/0"), 10, 10, 0, Button.Button1)
    
    #check plot
    conOb = waitForObject(":Configure Settings..._ToolItem")
    
    check_plotted_trace_name_yval(conOb,"Column_1","700.0","0.0")
    nameList = ["Column_1","Column_2","Column_3","Column_4",
                "Column_1'","Column_2'","Column_3'","Column_4'",
                "Column_1''","Column_2''","Column_3''","Column_4''"]
    check_plotted_traces_names(conOb, nameList[0:4])
    
    #Change to derivative and check again
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Derivative View"))
    
    conOb = waitForObject(":Configure Settings..._ToolItem_3")
    doubleClick(waitForObject(":Derivative View_CTabItem"), 82, 5, 0, Button.Button1)
    check_plotted_trace_name_yval(conOb,"Column_1'","300.0","-300.0")
    #check_plotted_traces_names(conOb, nameList[4:8])
    
    #add data and check again
    mouseClick(waitForObject(":Original_ToolItem"))
    #mouseClick(waitForObject(":Derivative.Display Data_Button"), 25, 8, 0, Button.Button1)
    
    check_plotted_trace_name_yval(conOb,"Column_1","700.0","-300.0")
    #check_plotted_traces_names(conOb, nameList[0:8])
    
    
    #add 2nd der and check again
    mouseClick(waitForObject(":Second_ToolItem"))
    #clickButton(waitForObject(":Derivative.Display f''(Data)_Button"))
    
    check_plotted_trace_name_yval(conOb,"Column_1","700.0","-300.0")
    #check_plotted_traces_names(conOb, nameList)
    
    closeOrDetachFromDAWN()
    
    
