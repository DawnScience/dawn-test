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
    
    openExample("001.img")
    
    system = getPlottingSystem("ref-testscale_1_001.img")
    
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)

    activateItem(waitForObjectItem(":Pop Up Menu", "Diffraction"))
    mouseClick(waitForObject(":Calibrants_ToolItem"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Cr2O3"))
    mouseClick(waitForObject(":Resolution rings_ToolItem"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Calibrant"))
    
    ob = waitForObject(":Diffraction_Tree")
    x,y = getBeamCentreFromTable(ob)
    
    mouseClick(waitForObject(":Export metadata to file_ToolItem"), 13, 9, 0, Button.Button1)
    expand(waitForObjectItem(":Export_Tree", "data"))
    expand(waitForObjectItem(":Export_Tree", "examples"))
    mouseClick(waitForObjectItem(":Export_Tree", "examples"), 29, 10, 0, Button.Button1)
    mouseClick(waitForObject(":Export.File name:_Text"), 67, 9, 0, Button.Button1)
    type(waitForObject(":Export.File name:_Text"), "SaveMetaData")
    clickButton(waitForObject(":Export.Next >_Button"))
    clickButton(waitForObject(":Export.Finish_Button"))
    
    c = waitForObject(":Image_Composite")
    b = c.bounds
    
    mouseClick(waitForObject(":One-click beam centre_ToolItem"), 7, 17, 0, Button.Button1)
    mouseClick(c, b.x+b.width/8, b.y+b.height/8, 0, Button.Button1);
    
    
    xnew,ynew = getBeamCentreFromTable(ob)
    test.verify(not xnew in x, "Beam X changed")
    test.verify(not ynew in y, "Beam Y changed")
    
    snooze(1)
    
    mouseClick(waitForObject(":Import metadata from file_ToolItem"), 17, 7, 0, Button.Button1)
    clickButton(waitForObject(":Import...._Button"))
    expand(waitForObjectItem(":File location.Please choose a location to import from._Tree", "data"))
    expand(waitForObjectItem(":File location.Please choose a location to import from._Tree", "examples"))
    mouseClick(waitForObjectItem(":File location.Please choose a location to import from._Tree", "SaveMetaData.nxs"), 98, 9, 0, Button.Button1)
    clickButton(waitForObject(":File location.OK_Button"))
    clickButton(waitForObject(":Import.Next >_Button"))
    clickButton(waitForObject(":Import.Finish_Button"))
    snooze(1)
    
    xnew,ynew = getBeamCentreFromTable(ob)
    test.verify(xnew in x, "Beam X changed")
    test.verify(ynew in y, "Beam Y changed")
    
    openExample("SaveMetaData")

    clickTab(waitForObject(":SaveMetaData.nxs.Tree_CTabItem"), 10, 11, 0, Button.Button1)
    
    tree = waitForObject(":Tree_Tree")

    expand(waitForObjectItem(":Tree_Tree", "entry"))
    expand(waitForObjectItem(":Tree_Tree", "data"))
    expand(waitForObjectItem(":Tree_Tree", "diffraction_metadata"))
    
    text = tree.getItems().at(0).getItems().at(1).getItems().at(0).getText()
    
    test.verify("beam_centre" in text, "tree contains beam centre")
    
    

    closeOrDetachFromDAWN()

