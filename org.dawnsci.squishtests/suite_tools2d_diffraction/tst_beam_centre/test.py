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
            test.verify(str(meta["distance"])[:4] in child[2].getText()[:4])
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
    openPerspective("Data Browsing (default)")
    
    openExample("001.img")
    
    system = getPlottingSystem("ref-testscale_1_001.img")
    
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Diffraction"))
    mouseClick(waitForObject(":Calibrants_ToolItem"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Cr2O3"))
    mouseClick(waitForObject(":Resolution rings_ToolItem"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Calibrant"))
    
    regions=system.getRegions()
    
    testRegionsAdded(regions, "calibrant")
    
    c = waitForObject(":Image_Composite")
    b = c.bounds
    
    ob = waitForObject(":Diffraction_Tree")
    x,y = getBeamCentreFromTable(ob)
    trc = system.getTraces().toArray().at(0)
    
    meta = getMetaDictionary(trc)
    
    testDiffractionTree(ob,meta)
    
    wid  = waitForObjectItem(":Diffraction_Tree", "X")

    mouseClick(waitForObject(":One-click beam centre_ToolItem"), 7, 17, 0, Button.Button1)
    
    mouseClick(c, b.x+b.width/8, b.y+b.height/8, 0, Button.Button1);
    
    xnew,ynew = getBeamCentreFromTable(ob)
    test.verify(not xnew in x, "Beam X changed")
    test.verify(not ynew in y, "Beam Y changed")
    x = xnew
    y = ynew
    
    mouseClick(waitForObject(":Resolution rings_ToolItem"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Calibrant"))
    
    mouseClick(waitForObject(":Select 3 or 4 points on ring to fit a circle or 5 points or more for an ellipse_ToolItem"), 6, 24, 0, Button.Button1)

    mouseClick(c, b.x+b.width/3.32, b.y+b.height/4.39, 0, Button.Button1);
    mouseClick(c, b.x+b.width/2.61, b.y+b.height/3.25, 0, Button.Button1);
    mouseClick(c, b.x+b.width/2.28, b.y+b.height/1.89, 0, Button.Button1);
    mouseClick(c, b.x+b.width/3.35, b.y+b.height/1.31, 0, Button.Button1);
    
    doubleClick(c, b.x+b.width/7.7, b.y+b.height/1.88, 0, Button.Button1);
    regions=system.getRegions()
    testRegionsAdded(regions, "RingPicker")

    mouseClick(waitForObject(":Refine beam centre_ToolItem"), 18, 17, 0, Button.Button1)
    
    snooze(1)
    
    xnew,ynew = getBeamCentreFromTable(ob)
    test.verify(not xnew in x, "Beam X changed")
    test.verify(not ynew in y, "Beam Y changed")

    snooze(1)
    
    closeOrDetachFromDAWN()