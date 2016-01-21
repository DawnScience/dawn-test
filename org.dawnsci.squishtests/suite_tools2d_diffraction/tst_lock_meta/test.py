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
    
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Science"))
    activateItem(waitForObjectItem(":Science_Menu_2", "Diffraction"))
    
    ob = waitForObject(":Diffraction_Tree")
    clickTab(ob, 40, 12, 0, Button.Button1)
    x,y = getBeamCentreFromTable()
    
    openExample("ref-screentest")
    
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem_2"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Science"))
    activateItem(waitForObjectItem(":Science_Menu_2", "Diffraction"))
   
    ob = waitForObject(":Diffraction_Tree")
    clickTab(ob, 40, 12, 0, Button.Button1) 
    xnew,ynew = getBeamCentreFromTable()
    
    test.verify(not xnew in x, "Beam X changed")
    test.verify(not ynew in y, "Beam Y changed")

    mouseClick(waitForObject(":ref-screentest-crystal1_1_001.mccd_CTabCloseBox"), 13, 10, 0, Button.Button1)
    
    mouseClick(waitForObject(":Lock the diffraction data and apply it to newly opened files._ToolItem"), 12, 18, 0, Button.Button1)
    
    openExample("ref-screentest")
    
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem_2"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Science"))
    activateItem(waitForObjectItem(":Science_Menu_2", "Diffraction"))

    ob = waitForObject(":Diffraction_Tree")
    clickTab(ob, 40, 12, 0, Button.Button1)    
    xnew,ynew = getBeamCentreFromTable()
    
    test.verify(xnew in x, "Beam X locked")
    test.verify(ynew in y, "Beam Y locked")
    
    mouseClick(waitForObject(":ref-screentest-crystal1_1_001.mccd_CTabCloseBox"), 13, 10, 0, Button.Button1)
    mouseClick(waitForObject(":Lock the diffraction data and apply it to newly opened files._ToolItem"), 12, 18, 0, Button.Button1)
    
    openExample("ref-screentest")
    
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem_2"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Science"))
    activateItem(waitForObjectItem(":Science_Menu_2", "Diffraction"))
    
    ob = waitForObject(":Diffraction_Tree")
    clickTab(ob, 40, 12, 0, Button.Button1)
    xnew,ynew = getBeamCentreFromTable()
    
    test.verify(not xnew in x, "Beam X changed")
    test.verify(not ynew in y, "Beam Y changed")

    closeOrDetachFromDAWN()