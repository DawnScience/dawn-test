source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_constants.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "tools1d_utils.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))

def the_actual_test(system):
    vals = dawn_constants
    #Open each tool and check it closes ok when the next tool opens
    #Peak fitting
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Peak Fitting"))
    
    #Fit peak
    mouseDragRegion(system)
    snooze(5)
    
    #check being shown
    names = ["Column_3","Peak 1"]
    check_plotted_traces_names(waitForObject(":Configure Settings..._ToolItem"), names)
    
    #activate derivative tool, which should deactivate the peak fitting
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Derivative View"))
#    names = ["Peak 1","Column_3'"]
#    #check_plotted_traces_names(waitForObject(":Configure Settings..._ToolItem"), names)
#    check_plotted_trace_name_yval(waitForObject(":Configure Settings..._ToolItem"), "Peak 1", "400.0", "-400.0")
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Measurement"))
    #Check derivative tool has reset
    
    names = ["Column_3", "Peak 1"]
    check_plotted_traces_names(waitForObject(":Configure Settings..._ToolItem"), names)
    check_plotted_trace_name_yval(waitForObject(":Configure Settings..._ToolItem"),"Column_3", "800.0","0.0")
    
    #Measure across peak
    mouseDragRegion(system)
    
    clickTab(waitForObject(":Measurement_CTabItem"), 61, 12, 0, Button.Button1)
     
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Line Fitting"))
    
    #Fit line to peak
    mouseDragRegion(system)
    
    names = ["Column_3", "Peak 1", "Fit 1"]
    check_plotted_traces_names(waitForObject(":Configure Settings..._ToolItem"), names)
    
    test.verify(waitForObjectItem(":Line Fitting_Table", "0/0").text == "Column_3", "Verify measurement text");
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Clear tool"))
    
    mouseClick(waitForObject(":No tool_CTabCloseBox"), 12, 6, 0, Button.Button1)
    

def main():
    
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Data Browsing (default)")
    openExample("pow_M99S5_1_0001.cbf")
    system = getPlottingSystem("pow_M99S5_1_0001.cbf")
    
    #Open datafile and get the plotting system for the tests
    openExample("metalmix.mca")
    system = getPlottingSystem("metalmix.mca")
    if(isEclipse4()):
        mouseClick(waitForObjectItem(":Data_Table_2", "2/0"), 9, 5, 0, Button.Button1)
    else:
        mouseClick(waitForObjectItem(":Data_Table", "2/0"), 9, 5, 0, Button.Button1)
    
    snooze(2)
    the_actual_test(system)
    #and again
    the_actual_test(system)

    closeOrDetachFromDAWN()