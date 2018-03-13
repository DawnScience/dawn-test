source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))

def main():
    
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Data Browsing")
    
    #expand data tree and open metal mix
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    for child in children:
        if "96356.dat" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            continue
    if (isEclipse4()):
        mouseClick(waitForObjectItem(":Data_Table_2", "3/0"), 11, 12, 0, Button.Button1)
    else:
        mouseClick(waitForObjectItem(":Data_Table_4", "3/0"), 10, 7, 0, Button.Button1)

    snooze(1)
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), 31, 7, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Peak Fitting"))
    
    test.verify(object.exists(":Peak Fitting_CTabItem"), "peak fitting there")
    
    wid = waitForObject(":_ToolBar_4")
 
    test.verify(wid.getItem(0).getToolTipText() == "New fit selection.", "Test tooltips")
    test.verify(wid.getItem(3).getToolTipText() == "Show annotations at the peak position.", "Test tooltips")
    test.verify(wid.getItem(4).getToolTipText() == "Show fitting traces.", "Test tooltips")
    test.verify(wid.getItem(5).getToolTipText() == "Show peak lines.", "Test tooltips")
    
    test.verify(object.exists(":Trace_TableColumn"), "trace column there")
    test.verify(object.exists(":FWHM_TableColumn"), "FWHM column there")
    
    test.verify(not object.exists(":sum_TableCell"), "no table cell")
    
    c = waitForObject(":Plot_Composite")
    b = c.bounds

    test.log("Image at (%d, %d) is %d x %d" % (b.x,b.y, b.width, b.height))
    mouseDrag(c, b.x+b.width/3, b.y+b.height/3, b.height/3, b.width/4, 0, Button.Button1)
    snooze(1)

    conOb = waitForObject(":Configure Settings..._ToolItem_2")

    nameList = ["sum","Peak 1"]
    check_plotted_traces_names(conOb, nameList)
    mouseClick(conOb)
    clickTab(waitForObject(":Configure Graph Settings.Traces_TabItem"))
    widget = waitForObject(":Select Trace_Combo")
    test.verify(widget.text == 'sum', "Check Trace Name")
    clickTab(waitForObject(":Configure Graph Settings.Annotations_TabItem"))
    widget = waitForObject(":Select Annotation_Combo")
    test.verify(widget.text == 'Peak 1', "Check Trace Name")
    clickTab(waitForObject(":Configure Graph Settings.Regions_TabItem"))
    widget = waitForObject(":Selection Region_Combo")
    test.verify(widget.text == 'Peak Area 1', "Check Trace Name")
    
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 7, 8, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open cheat sheet for 'Peak Fitting'"))
    
    test.verify(object.exists(":Cheat Sheets_CTabItem"), "cheat sheet there")

    mouseClick(waitForObject(":View Menu_ToolItem_2"), 10, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Preferences..."))

    clickButton(waitForObject(":Preferences.OK_Button"))
    
    closeOrDetachFromDAWN()

    