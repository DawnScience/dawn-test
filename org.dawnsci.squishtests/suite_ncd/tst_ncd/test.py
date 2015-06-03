source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))

import os

def main():
    
    startOrAttachToDAWN()
    openPerspective("NCD Calibration")
    
    system = getPlottingSystem("Dataset Plot")

    ncdFile = openExample("i22-104749.nxs", subfolder="saxs", findOnly=True)
    
    mouseClick(ncdFile, 5, 5, 0, Button.Button3)
    activateItem(waitForObjectItem(":_Menu_2", "NCD"))
    activateItem(waitForObjectItem(":NCD_Menu", "Read Detector Information"))
    clickButton(waitForObject(":NCD Detector Parameters.SAXS_Button"))
    mouseClick(waitForObjectItem(":NCD Detector Parameters.SAXS_Combo", "Pilatus2M"), 7, 14, 0, Button.Button1)
    
    mouseClick(ncdFile, 5, 5, 0, Button.Button3)
    
    activateItem(waitForObjectItem(":_Menu_2", "NCD"))
    activateItem(waitForObjectItem(":NCD_Menu", "Load Calibration Image"))
    imageToolsMenu = waitForImageToolsMenu()
    mouseClick(waitForObject(imageToolsMenu), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Masking"))
    clickButton(waitForObject(":Masking 'data'.Enable lower mask    _Button"))

    clickButton(waitForObject(":Masking 'data'.Apply_Button"))
    mouseClick(waitForObject(":Masking 'data'_Spinner"))

    type(waitForObject(":Masking 'data'_Spinner"), "<Backspace>")
    type(waitForObject(":Masking 'data'_Spinner"), "<Numpad 1>")
    clickButton(waitForObject(":Masking 'data'.Apply_Button"))
    
    snooze(1)
    
    mouseClick(waitForObject(imageToolsMenu), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Profile"))
    activateItem(waitForObjectItem(":Profile_Menu", "Radial Profile"))
    
    c = waitForObject(system.getPlotComposite())
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
    
    # This seems to be where the test fails and there are few calls to waitForXYPlottingToolsMenu
    mouseClick(waitForXYPlottingToolsMenu(cTabItemText="Radial Profile"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Peak Fitting"))
    
    mouseClick(waitForSwtToolItem("Number peaks to fit"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Fit 10 Peaks"))
    
    rx1, ry1 = getScreenPosition(system, 360, 1200)
    rx2,ry2 = getScreenPosition(system,1200,1200)
    
    mouseClick(c,rx1,ry1, 0, Button.Button1)
    mouseClick(c,rx2,ry2, 0, Button.Button1)

    snooze(5)
    text_widget = waitForSwtTextWithLabel("Gradient")
    test.verify(text_widget.text == "--")
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
    
    ncdDataRedParams = waitForSwtCTabItem("NCD Data Reduction Parameters")
    clickTab(waitForObject(ncdDataRedParams))

    clickButton(waitForObject(":Data reduction pipeline.2. Sector integration_Button_2"))
    
    resultsDirText = waitForObject(":Results directory_Text")
    mouseClick(waitForObject(resultsDirText))

    type(waitForObject(resultsDirText), "<Ctrl+a>")
    type(waitForObject(resultsDirText), "<Delete>")
    type(waitForObject(resultsDirText), location)
#    type(waitForObject(resultsDirText), location[1:]) #This input means we don't get the autocomplete box.
#    type(waitForObject(resultsDirText), "<Home>")
#    type(waitForObject(resultsDirText), location[0])

    clickTab(waitForObject(ncdDataRedParams))
    snooze(1)

    clickButton(waitForObject(":NCD Data Reduction Parameters.Radial Profile_Button_2"))

    snooze(1)
    
    clickTab(waitForObject(ncdDataRedParams))
    snooze(1)
    
    mouseClick(ncdFile, 5, 5, 0, Button.Button3)
    activateItem(waitForObjectItem(":_Menu_2", "NCD"))
    activateItem(waitForObjectItem(":NCD_Menu_2", "Run Data Reduction"))
    
    projExplore = waitForTreeWithItem("data")
    mouseClick(waitForObjectItem(projExplore, "examples"), 49, 5, 0, Button.Button1)
    type(waitForObject(projExplore), "<F5>")
    snooze(5)
    
    children = object.children(waitForObjectItem(projExplore, "examples"))
    
    found = False
    for child in children:
        if "i22-104749" in child.text:
            found = True
            break
    
    test.verify(found,"File is found")
    
    closeOrDetachFromDAWN()


