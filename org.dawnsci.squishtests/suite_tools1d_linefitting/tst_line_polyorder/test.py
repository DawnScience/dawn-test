source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_constants.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))

def main():
    
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Data Browsing")
    vals = dawn_constants
    #expand data tree and open metal mix
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    for child in children:
        if "metalmix.mca" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            continue
    
#     mouseClick(waitForObject(":Plot data as separate plots_ToolItem"), 18, 11, 0, Button.Button1)
    
    if(isEclipse4()):
        mouseClick(waitForObjectItem(":Data_Table_3", "1/0"), 9, 7, 0, Button.Button1)
    else:
        mouseClick(waitForObjectItem(":Data_Table", "1/0"), 9, 7, 0, Button.Button1)
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem_2"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Line Fitting"))
    
    c = waitForObject(":Plot_Composite_2")
    b = c.bounds

    test.log("Image at (%d, %d) is %d x %d" % (b.x,b.y, b.width, b.height))
    mouseDrag(c, b.x+b.width/3, b.y+b.height/3, int(b.width/1.7),b.height/3, 0, Button.Button1)
    snooze(1)
    
    tab = waitForObject(":Line Fitting_Table")
    
    test.verify(tab.getItemCount()==1,"one line in table")
    
    wid =  waitForObjectItem(":Line Fitting_Table",  "0/2")
    test.verify(wid.text == "1st Order Polynomial","1st poly check")
    
    mouseClick(waitForObject(":Polynomial order to fit_ToolItem"), 30, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Polynomial Order: 2"))
    
    wid =  waitForObjectItem(":Line Fitting_Table",  "0/2")
    test.verify(wid.text == "2nd Order Polynomial","2nd poly check")
    
    for i in range(4,8):
        mouseClick(waitForObject(":Polynomial order to fit_ToolItem"), 30, 10, 0, Button.Button1)
        activateItem(waitForObjectItem(":Pop Up Menu", "Polynomial Order: " + str(i)))
        snooze(1)
        wid =  waitForObjectItem(":Line Fitting_Table",  "0/2")
        test.verify(wid.text == (str(i) +"th Order Polynomial"),"loop poly check")


    closeOrDetachFromDAWN()