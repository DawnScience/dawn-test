source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_constants.py"))

def main():
    
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Data Browsing (default)")
    vals = dawn_constants
    #expand data tree and open metal mix
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    for child in children:
        if "metalmix.mca" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            continue
    
    mouseClick(waitForObjectItem(":Data_Table", "0/0"), 9, 7, 0, Button.Button1)
    
    #Check data has plotted by looking at graph settings
    conOb = waitForObject(":Configure Settings..._ToolItem")
    check_plotted_trace_name_yval(conOb,"Column_1","600.0","0.0")
    
    #Change to measurement and check again
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Measurement"))
    
    #DRAW ONE
    tab = waitForObject(":Measurement_Table")
    #starts with one empty item
    test.verify(tab.getItemCount()==1,"table empty")
    
    c = waitForObject(":Plot_Composite")
    b = c.bounds

    test.log("Image at (%d, %d) is %d x %d" % (b.x,b.y, b.width, b.height))
    mouseDrag(c, b.x+b.width/3, b.y+b.height/3, int(b.width/1.7),b.height/3, 0, Button.Button1)
    snooze(1)
    
    test.verify(tab.getItemCount()==1,"one line in table")
    #draw lots of lines
    for i in range(1,30):
        #DRAW
        mouseClick(waitForObject(":Create new measurement_ToolItem"), 16, 8, 0, Button.Button1)
    
        c = waitForObject(":Plot_Composite")
        b = c.bounds
        num = 3. + 1./i
        mouseDrag(c, b.x+b.width/num, b.y+b.height/3, int(b.width/3),b.height/5, 0, Button.Button1)
        snooze(1)
    #check table has correct number of items
    test.verify(tab.getItemCount()==30,"lines in table")    
    #check plot setting has the correct number of regions
    mouseClick(waitForObject(":Configure Settings..._ToolItem"), 14, 8, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Regions_TabItem"))
    
    wid = waitForObject(":Selection Region_Combo")
    chil = object.children(wid)
    test.verify(len(chil)==30)
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    closeOrDetachFromDAWN()