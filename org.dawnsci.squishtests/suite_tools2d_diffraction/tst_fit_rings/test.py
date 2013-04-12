source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))
source(findFile("scripts", "diffractionutils.py"))

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
    
     #expand data tree and open metal mix
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    expand(waitForObjectItem(":Project Explorer_Tree", "saxs"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "saxs"))
    
    for child in children:
        if "i22-104754.nxs" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            break

    mouseClick(waitForObjectItem(":Data_Table", "0/0"))
    
    system = getPlottingSystem("i22-104754.nxs")
    

    #getScreenPosition(plottingSystem,x,y)
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem_4"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Diffraction"))
    
    c = waitForObject(":Plot_Composite")
    b = c.bounds
    
    mouseClick(waitForObject(":Select 3 or 4 points on ring to fit a circle or 5 points or more for an ellipse_ToolItem_2"))
    
    rx1,ry1 = getScreenPosition(system,350,95)
    rx2,ry2 = getScreenPosition(system,753,465)
    rx3,ry3 = getScreenPosition(system,1139,90)
    
    mouseClick(c,rx1,ry1, 0, Button.Button1)
    mouseClick(c,rx2,ry2, 0, Button.Button1)
    doubleClick(c,rx3,ry3, 0, Button.Button1)


    regions=system.getRegions()
    testRegionsAdded(regions, "RingPicker")
    
    mouseClick(waitForObject(":Refine beam centre_ToolItem_2"))
    snooze(4)
    
    regions=system.getRegions()
    testRegionsAdded(regions, "Pixel")
    
    mouseClick(waitForObject(":Select 3 or 4 points on ring to fit a circle or 5 points or more for an ellipse_ToolItem_2"))
    
    rx1,ry1 = getScreenPosition(system,105,522)
    rx2,ry2 = getScreenPosition(system,751,860)
    rx3,ry3 = getScreenPosition(system,1397,505)
    
    mouseClick(c,rx1,ry1, 0, Button.Button1)
    mouseClick(c,rx2,ry2, 0, Button.Button1)
    doubleClick(c,rx3,ry3, 0, Button.Button1)


    regions=system.getRegions()
    testRegionsAdded(regions, "RingPicker")
    
    mouseClick(waitForObject(":Refine beam centre_ToolItem_2"))
    snooze(4)
    
    regions=system.getRegions()
    testRegionsAdded(regions, "Pixel")
    
    mouseClick(waitForObject(":Select 3 or 4 points on ring to fit a circle or 5 points or more for an ellipse_ToolItem_2"))
    
    rx1,ry1 = getScreenPosition(system,140,1080)
    rx2,ry2 = getScreenPosition(system,901,1241)
    rx3,ry3 = getScreenPosition(system,1359,1078)
    
    mouseClick(c,rx1,ry1, 0, Button.Button1)
    mouseClick(c,rx2,ry2, 0, Button.Button1)
    doubleClick(c,rx3,ry3, 0, Button.Button1)


    regions=system.getRegions()
    testRegionsAdded(regions, "RingPicker")
    
    mouseClick(waitForObject(":Refine beam centre_ToolItem_2"))
    snooze(4)
    
    regions=system.getRegions()
    testRegionsAdded(regions, "Pixel")

    
    
    closeOrDetachFromDAWN()