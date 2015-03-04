def createPeakFitSpace(steps=15):
    #To stop problem of not all menu items in drop-down being visible initially
    clickTab(waitForObject(":Value_CTabItem"), 29, 14, 0, Button.Button1)
    clickTab(waitForObject(":Value_CTabItem"), 29, 14, 0, Button.Button3)
    activateItem(waitForObjectItem(":Pop Up Menu", "Size"))
    activateItem(waitForObjectItem(":Size_Menu", "Top"))
    while steps >= 0:
        type(waitForObject(":_Sash_3"), "<Up>")
        steps -= 1
    clickTab(waitForObject(":Value_CTabItem"), 48, 22, 0, Button.Button1)

def loadMetalMix():
    #expand data tree and open metal mix
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    for child in children:
        if "metalmix.mca" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            continue

def fitOneThenFourPeaks():
    mouseClick(waitForObject(":XY plotting tools_ToolItem_2"), 31, 7, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Peak Fitting"))
    
    c = waitForObject(":Plot_Composite_2")
    b = c.bounds

    test.log("Image at (%d, %d) is %d x %d" % (b.x,b.y, b.width, b.height))
    mouseDrag(c, b.x+b.width/3, b.y+b.height/3, int(b.width/1.7),b.height/3, 0, Button.Button1)
    snooze(5)
    
    tab = waitForObject(":Peak Fitting_Table")
    test.verify(tab.getItemCount()==1,"Expected: 1 Actual: " + str(tab.getItemCount()))
    
    test.verify(waitForObjectItem(":Peak Fitting_Table", "0/1").text == "Peak 1","peak 1 present")
    
    mouseClick(waitForObject(":Number peaks to fit_ToolItem"), 29, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Fit 4 Peaks"))
    
    test.verify(tab.getItemCount()==4,"Expected: 4 Actual: " + str(tab.getItemCount()))
    
    for i in range(4):
        txt = waitForObjectItem(":Peak Fitting_Table",  str(i) + "/1").text
        test.verify(txt == "Peak " + str(i+1),"peak present")
        
    #Need to return tab for the multiple traces & dedicated tests
    return tab