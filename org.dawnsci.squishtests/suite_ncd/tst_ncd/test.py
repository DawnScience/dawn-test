source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))

import os

def main():
    
    startOrAttachToDAWN()
    openPerspective("NCD Calibration")
    
    system = getPlottingSystem("Dataset Plot")

    
    expand(waitForObjectItem(":Project Explorer_Tree_2", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree_2", "examples"))
    expand(waitForObjectItem(":Project Explorer_Tree_2", "saxs"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree_2", "saxs"))
    
    for child in children:
        if "i22-104749.nxs" in child.text:
            mouseClick(child, 5, 5, 0, Button.Button3)
            break
    
    activateItem(waitForObjectItem(":_Menu_2", "NCD"))
    activateItem(waitForObjectItem(":NCD_Menu", "Read Detector Information"))
    clickButton(waitForObject(":NCD Detector Parameters.SAXS_Button"))
    mouseClick(waitForObjectItem(":NCD Detector Parameters.SAXS_Combo", "Pilatus2M"), 7, 14, 0, Button.Button1)
    
    mouseClick(child, 5, 5, 0, Button.Button3)
    
    activateItem(waitForObjectItem(":_Menu_2", "NCD"))
    activateItem(waitForObjectItem(":NCD_Menu", "Load Calibration Image"))
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem_2"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Masking"))
    clickButton(waitForObject(":Masking 'data'.Enable lower mask    _Button"))

    clickButton(waitForObject(":Masking 'data'.Apply_Button"))
    mouseClick(waitForObject(":Masking 'data'_Spinner"))

    type(waitForObject(":Masking 'data'_Spinner"), "<Backspace>")
    type(waitForObject(":Masking 'data'_Spinner"), "<Numpad 1>")
    clickButton(waitForObject(":Masking 'data'.Apply_Button"))
    
    snooze(1)
    
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem_2"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Profile"))
    activateItem(waitForObjectItem(":Profile_Menu", "Radial Profile"))
    
    c = waitForObject(":Dataset Plot_Composite")
    b = c.bounds
    
    rx1, ry1 = getScreenPosition(system, 743, 78)
    rx2,ry2 = getScreenPosition(system,802,441)
    rx3,ry3 = getScreenPosition(system,584,1543)
    
    mouseClick(c,rx1,ry1, 0, Button.Button1)
    mouseClick(c,rx2,ry2, 0, Button.Button1)
    mouseClick(c,rx3,ry3, 0, Button.Button1)
    
    system = getPlottingSystem("Radial Profile")
    c = waitForObject(":_FigureCanvas")
    b = c.bounds
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Peak Fitting"))
    
    mouseClick(waitForObject(":Number peaks to fit_ToolItem"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Fit 10 Peaks"))
    
    rx1, ry1 = getScreenPosition(system, 360, 1200)
    rx2,ry2 = getScreenPosition(system,1200,1200)
    
    mouseClick(c,rx1,ry1, 0, Button.Button1)
    mouseClick(c,rx2,ry2, 0, Button.Button1)

    snooze(5)
    text_widget = waitForObject(":Calibration Function.Gradient_Text")
    test.verify(text_widget.text == "--")
    #mouseClick(waitForObject(":Saxs Q-axis Calibration.Calibration Controls_Group"))
    mouseClick(waitForObjectItem(":Calibration Controls.Standard_Combo", "Collagen Dry"))
    clickButton(waitForObject(":Calibration Controls.Calibrate_Button"))
    

    counter = 0
    
    while (text_widget.text == "--" and counter < 60):
        snooze(1)
        counter += 1

    if (not text_widget.text == "--"):
        system = getPlottingSystem("Calibration Plot")
        traces = system.getTraces().toArray()
        contains_fitting_line = False
        
        for i in range(traces.length):
            if "Fitting line" in traces.at(i).getName():
                contains_fitting_line = True
        
        test.verify(contains_fitting_line, "Test fitting line in plot")
        
    else:
        test.fail("calibration did not complete")

    snooze(5)
    
    openPerspective("NCD Data Reduction")
    snooze(2)
    
    activateItem(waitForObjectItem(":_Menu", "File"))
    activateItem(waitForObjectItem(":File_Menu", "Switch Workspace"))
    activateItem(waitForObjectItem(":Switch Workspace_Menu", "Other..."))
    workspaceName = waitForObject(":Workspace Launcher.Workspace:_Combo").text
    clickButton(waitForObject(":Workspace Launcher.Cancel_Button"))

    location = os.path.join(workspaceName, "data","examples");
    
    clickTab(waitForObject(":NCD Data Reduction Parameters_CTabItem_2"))

    #doubleClick(waitForObject(":NCD Data Reduction Parameters_CTabItem"), 128, 17, 0, Button.Button1)
    clickButton(waitForObject(":Data reduction pipeline.2. Sector integration_Button_2"))
 
    mouseClick(waitForObject(":Results directory.Directory:_Text_2"))

    #mouseDrag(waitForObject(":Results directory.Directory:_Text"), 229, 15, -319, -4, Modifier.None, Button.Button1)
    type(waitForObject(":Results directory.Directory:_Text_2"), "<Ctrl+a>")
    type(waitForObject(":Results directory.Directory:_Text_2"), "<Delete>")
    type(waitForObject(":Results directory.Directory:_Text_2"), location[1:])
    type(waitForObject(":Results directory.Directory:_Text_2"), "<Home>")
    type(waitForObject(":Results directory.Directory:_Text_2"), location[0])


    clickTab(waitForObject(":NCD Data Reduction Parameters_CTabItem_2"), 181, 28, 0, Button.Button1)
    snooze(1)
    #clickButton(waitForObject(":Results directory...._Button"))

    #chooseDirectory(waitForObject(":SWT"), "/scratch/workspace/testoutput")
    snooze(1)
    clickButton(waitForObject(":NCD Data Reduction Parameters.Radial Profile_Button_2"))

    snooze(1)
    
    clickTab(waitForObject(":NCD Data Reduction Parameters_CTabItem_2"), 128, 14, 0, Button.Button1)
    #doubleClick(waitForObject(":NCD Data Reduction Parameters_CTabItem"), 128, 17, 0, Button.Button1)
    snooze(1)
    
    mouseClick(child, 5, 5, 0, Button.Button3)
    activateItem(waitForObjectItem(":_Menu_2", "NCD"))
    activateItem(waitForObjectItem(":NCD_Menu_2", "Run Data Reduction"))

    mouseClick(waitForObjectItem(":Project Explorer_Tree_3", "examples"), 49, 5, 0, Button.Button1)
    type(waitForObject(":Project Explorer_Tree_3"), "<F5>")
    snooze(5)
    
    children = object.children(waitForObjectItem(":Project Explorer_Tree_2", "examples"))
    
    found = False
    for child in children:
        if "i22-104749" in child.text:
            found = True
            break
    
    test.verify(found,"File is found")
    
    closeOrDetachFromDAWN()


