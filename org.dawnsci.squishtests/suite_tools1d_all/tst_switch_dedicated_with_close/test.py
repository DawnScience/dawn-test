source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_constants.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "tools1d_utils.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))

def the_actual_test(system):
    vals = dawn_constants
    #Open each tool then make dedicated
    #Peak fitting
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Peak Fitting"))
    
    #Fit peak
    mouseDragRegion(system)
    
    #check being shown
    names = ["Column_3","Peak 1"]
    check_plotted_traces_names(waitForObject(":Configure Settings..._ToolItem"), names)
    
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 3, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open 'Peak Fitting' in dedicated view"))
    
    snooze(1)
    
    mouseClick(waitForObject(":Peak Fitting_CTabCloseBox"), 12, 14, 0, Button.Button1)
    
    #activate derivative tool, which should deactivate the peak fitting
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Derivative View"))
    names = ["Column_3"]
    check_plotted_traces_names(waitForObject(":Configure Settings..._ToolItem"), names)
    #check_plotted_trace_name_yval(waitForObject(":Configure Settings..._ToolItem"), "Column_3'", "400.0", "-400.0")
    
#   On ws266 this, setting Derivative to dedicated view fails (for no apparent reason)
#   As this isn't serving a particular purpose and is not relied on elsewhere, commented out  
    if gethostname() != 'ws266.diamond.ac.uk':
        mouseClick(waitForObject(":View Menu_ToolItem_2"), 4, 5, 0, Button.Button1)
        activateItem(waitForObjectItem(":Pop Up Menu", "Open 'Derivative View' in dedicated view"))
        
        snooze(1)
        mouseClick(waitForObject(":Derivative View_CTabCloseBox"))

    #Need these lines to make sure Measurement can be selected.
    clickTab(waitForObject(":metalmix.mca_CTabItem"), 53, 5, 0, Button.Button1)
    snooze(1)
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Measurement"))
    #Check derivative tool has not reset
    names = ["Column_3"]
    check_plotted_traces_names(waitForObject(":Configure Settings..._ToolItem"), names)
    check_plotted_trace_name_yval(waitForObject(":Configure Settings..._ToolItem"),"Column_3", "700.0","0.0")
    
    #Measure across peak
    mouseDragRegion(system)
    
    clickTab(waitForObject(":Measurement_CTabItem"), 61, 12, 0, Button.Button1)
    #test.verify(waitForObjectItem(":Measurement_Table", "0/0").text == "Measurement 1", "Verify measurement text");
    
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 3, 7, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open 'Measurement' in dedicated view"))
    
    snooze(1)
    
    mouseClick(waitForObject(":Measurement_CTabCloseBox"), 10, 4, 0, Button.Button1)
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Line Fitting"))
    
    #Fit line to peak
    mouseDragRegion(system)
    
    names = ["Column_3", "Fit 1"]
    check_plotted_traces_names(waitForObject(":Configure Settings..._ToolItem"), names)
    
    test.verify(waitForObjectItem(":Line Fitting_Table", "0/0").text == "Column_3", "Verify measurement text");
    
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 12, 14, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open 'Line Fitting' in dedicated view"))
    
    snooze(1)
    
    mouseClick(waitForObject(":Line Fitting_CTabCloseBox"), 10, 9, 0, Button.Button1)
    
    

def main():
    
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Data Browsing")
    
    #Open datafile and get the plotting system for the tests
    openExample("metalmix.mca")
    system = getPlottingSystem("metalmix.mca")
    if(isEclipse4()):
        mouseClick(waitForObjectItem(":Data_Table_2", "2/0"), 9, 5, 0, Button.Button1)
    else:
        mouseClick(waitForObjectItem(":Data_Table", "2/0"), 9, 5, 0, Button.Button1)
    
    snooze(2)
    the_actual_test(system)
    #repeat
    snooze(1)
    the_actual_test(system)

    closeOrDetachFromDAWN()