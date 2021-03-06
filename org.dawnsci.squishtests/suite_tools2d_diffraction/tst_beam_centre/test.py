source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))
source(findFile("scripts", "diffractionutils.py"))

def getMetaDictionary(trace):
    diffenv = trace.getData().getMetadata().getDiffractionCrystalEnvironment()
    detProp= trace.getData().getMetadata().getDetector2DProperties()
    meta = {};
    meta["wavelength"] = diffenv.getWavelength()
    meta["exposure"] = diffenv.getExposureTime()
    
    meta["distance"] = detProp.getBeamCentreDistance()

    return meta

def testDiffractionTree(tree,meta):
    first = tree.getItems()
    
    for i in range(first.length):
        node = first.at(i)
        
        if ("Detector" in node.getText()):
            testDetectorNode(node,meta)
        
        if ("Experimental Information" in node.getText()):
            testExperimentalInfoNode(node,meta)

def testDetectorNode(node,meta):
    first = node.getItems()
    
    time = False
    
    for i in range(first.length):
        node = first.at(i)
        
        if ("Exposure Time" in node.getText()):
            child = object.children(node)
            test.verify(str(meta["exposure"])[0] in child[2].getText())
            time = True
    
    test.verify(time, "was exposure time checked")

def testExperimentalInfoNode(node,meta):
    first = node.getItems()
    
    dist = False
    wave = False
    
    for i in range(first.length):
        node = first.at(i)
            
        if ("Distance" in node.getText()):
            child = object.children(node)
            test.verify(str(meta["distance"])[:3] in child[2].getText()[:4])
            dist = True
        
        if ("Wavelength" in node.getText()):
            child = object.children(node)
            test.verify(str(meta["wavelength"])[:4] in child[2].getText()[:4])
            wave = True
    
    test.verify(dist,"was distance checked")
    test.verify(wave, "was wavelength checked")

def testRegionsAdded(regions, name):
    
    for i in range(regions.size()):
        if (name in regions.get(i).getName()):
            test.passes("Expected name: " + name + " found")
            return
    
    test.fail("Expected name: " + name + " not found")

def main():
    
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Data Browsing")
    
    
#     expandObjectLeft(waitForObject(":Data_CTabItem"), 6)

#     clickTab(waitForObject(":Project Explorer_CTabItem"), 49, 22, 0, Button.Button3)
    openExample("pow_M99S5_1_0001.cbf")

    
    system = getPlottingSystem("pow_M99S5_1_0001.cbf")
    
    #getScreenPosition(plottingSystem,x,y)

    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem_6"), 32, 12, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Science"))
    activateItem(waitForObjectItem(":Science_Menu_2", "Diffraction"))
    
    c = waitForObject(":Image_Composite_2")
    b = c.bounds

    ob = waitForObject(":Diffraction_Tree")
    clickTab(ob, 40, 12, 0, Button.Button1)
    
    snooze(3)

    x, y = getBeamCentreFromTable()
    trc = system.getTraces().toArray().at(0)
    
    meta = getMetaDictionary(trc)
    
    testDiffractionTree(waitForObject(":Diffraction_Tree_2"),meta)
    
    wid  = waitForObjectItem(":Diffraction_Tree_2", "X")

    mouseClick(waitForObject(":One-click beam centre_ToolItem"), 7, 17, 0, Button.Button1)
    
    cx,cy = getScreenPosition(system,100,100)
    
    mouseClick(c, cx, cy, 0, Button.Button1);
    
    xnew,ynew = getBeamCentreFromTable()
    test.verify(not xnew in x, "Beam X changed")
    test.verify(not ynew in y, "Beam Y changed")
    x = xnew
    y = ynew
    
    snooze(1)
    
    clickTab(waitForObject(":Diffraction_CTabItem"), 50, 10, 0, Button.Button1)
    mouseClick(waitForObject(":Select 3 or 4 points on ring to fit a circle or 5 points or more for an ellipse_ToolItem"))
    
    rx1,ry1 = getScreenPosition(system,1242,255)
    rx2,ry2 = getScreenPosition(system,2024,1771)
    rx3,ry3 = getScreenPosition(system,423,1778)
    
    mouseClick(c,rx1,ry1, 0, Button.Button1)
    mouseClick(c,rx2,ry2, 0, Button.Button1)
    
    doubleClick(c,rx3,ry3, 0, Button.Button1)


    regions=system.getRegions()
    testRegionsAdded(regions, "RingPicker")
    
    snooze(1)
    
    clickTab(waitForObject(":Diffraction_CTabItem"), 50, 10, 0, Button.Button1)
    mouseClick(waitForObject(":Refine beam centre_ToolItem"))
    
    snooze(1)

    
    xnew,ynew = getBeamCentreFromTable()
    test.verify(not xnew in x, "Beam X changed")
    test.verify(not ynew in y, "Beam Y changed")
    
    mouseClick(waitForObject(":Calibrants_ToolItem"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Cr2O3"))
    mouseClick(waitForObject(":Resolution rings_ToolItem"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Calibrant"))
    regions=system.getRegions()
    testRegionsAdded(regions, "calibrant")
    
    mouseClick(waitForObject(":Find outer rings_ToolItem"), 12, 13, 0, Button.Button1)
    
    i = 0
    while object.exists(":Shows background operations in Progress view_ToolItem") and i < 100:
        snooze(5)
        i=i+1
    
    regions=system.getRegions()
    testRegionsAdded(regions, "Ring")

    closeOrDetachFromDAWN()
