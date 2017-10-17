source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))
source(findFile("scripts", "diffractionutils.py"))

def main():
    
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Data Browsing (default)")
    
    openExample("pow_M99S5_1_0001.cbf")
    
    system = getPlottingSystem("pow_M99S5_1_0001.cbf")
    
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)

    activateItem(waitForObjectItem(":Pop Up Menu", "Science"))
    activateItem(waitForObjectItem(":Science_Menu", "Diffraction"))
    mouseClick(waitForObject(":Calibrants_ToolItem"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Cr2O3"))
    mouseClick(waitForObject(":Resolution rings_ToolItem"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Calibrant"))
    
    x,y = getBeamCentreFromTable()
    
    mouseClick(waitForObject(":Export metadata to file_ToolItem"), 13, 9, 0, Button.Button1)
    clickButton(waitForObject(":Export_Button"))
    snooze(2)
    expand(waitForObjectItem(":File location.Please choose a location._Tree", "data"))
    mouseClick(waitForObjectItem(":File location.Please choose a location._Tree", "examples"), 4, 12, 0, Button.Button1)
    mouseClick(waitForObject(":File location.File Name:_Text"), 71, 4, 0, Button.Button1)
    type(waitForObject(":File location.File Name:_Text"), "AAASaveMetaData.nxs")
    clickButton(waitForObject(":File location.OK_Button"))
    clickButton(waitForObject(":Export.Finish_Button"))
    
    c = waitForObject(":Image_Composite")
    b = c.bounds
    
    mouseClick(waitForObject(":One-click beam centre_ToolItem"), 7, 17, 0, Button.Button1)
    mouseClick(c, b.x+b.width/8, b.y+b.height/8, 0, Button.Button1);
    
    xnew,ynew = getBeamCentreFromTable()
    test.verify(not xnew in x, "Beam X changed")
    test.verify(not ynew in y, "Beam Y changed")
    
    snooze(1)
    
    mouseClick(waitForObject(":Import metadata from file_ToolItem"), 17, 7, 0, Button.Button1)
    clickButton(waitForObject(":Import_Button"))
    expand(waitForObjectItem(":File location.Please choose a location._Tree", "data"))
    expand(waitForObjectItem(":File location.Please choose a location._Tree", "examples"))

    mouseClick(waitForObjectItem(":File location.Please choose a location._Tree", "AAASaveMetaData.nxs"), 73, 5, 0, Button.Button1)
    clickButton(waitForObject(":File location.OK_Button"))
    clickButton(waitForObject(":Import.Next >_Button"))
    clickButton(waitForObject(":Import.Finish_Button"))
    snooze(1)
    
    xnew,ynew = getBeamCentreFromTable()
    test.verify(xnew in x, "Beam X changed")
    test.verify(ynew in y, "Beam Y changed")
    
    openExample("AAASaveMetaData")

    clickTab(waitForObject(":AAASaveMetaData.nxs.Tree_CTabItem"), 18, 10, 0, Button.Button1)

    tree = waitForObject(":Tree_Tree")
    expand(waitForObjectItem(":Tree_Tree", "entry"))
    expand(waitForObjectItem(":Tree_Tree", "instrument"))
    expand(waitForObjectItem(":Tree_Tree", "detector"))

    text = tree.getItems().at(0).getItems().at(4).getItems().at(0).getItems().at(0).getText()
    
    test.verify("beam_center" in text, "tree contains beam center")
    
    

    closeOrDetachFromDAWN()

