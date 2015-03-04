source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "peakfit_shared.py"))

def main():
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Data Browsing (default)")
    
    #Create space so the drop-down menus show all items
    createPeakFitSpace(steps=25)
    snooze(1)
    
    #expand data tree and open metal mix
    loadMetalMix()
#    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
#    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
#    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
#    
#    for child in children:
#        if "metalmix.mca" in child.text:
#            doubleClick(child, 5, 5, 0, Button.Button1)
#            continue
    
    mouseClick(waitForObject(":Plot data as separate plots_ToolItem"), 18, 11, 0, Button.Button1)
    
    for i in range(16):
        mouseClick(waitForObjectItem(":Data_Table", str(i) + "/0"), 9, 7, 0, Button.Button1)
    
    snooze(1)
        
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
    snooze(5)
    test.verify(tab.getItemCount()==4,"Expected: 4 Actual: " + str(tab.getItemCount()))
    
    for i in range(4):
        txt = waitForObjectItem(":Peak Fitting_Table",  str(i) + "/1").text
        test.verify(txt == "Peak " + str(i+1),"peak present")
    
    mouseClick(waitForObject(":Choose trace for fit._ToolItem"), 29, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Select all"))
    
    snooze(30)
    
    test.verify(tab.getItemCount()==64,"64 peaks in table")
    
    mouseClick(waitForObject(":Name_TableColumn"), 82, 18, 0, Button.Button1)
    snooze(1)
    mouseClick(waitForObject(":Name_TableColumn"), 82, 18, 0, Button.Button1)
    snooze(1)
    
    for i in range(8):
        txt = waitForObjectItem(":Peak Fitting_Table", str(i) + "/1").text

        test.verify(txt == "Peak " + str(i+1),"peak present")
    
    closeOrDetachFromDAWN()