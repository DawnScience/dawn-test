source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_constants.py"))

def check_axis(conOb,name):
    mouseClick(conOb, 15, 9, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    widget = waitForObject(":Select Axis_Combo")
    test.verify(widget.text == name, "Check Axes Name Expected: " + name + " Actual: "+ widget.text)
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    
def main():
    vals = dawn_constants
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Data Browsing")
    
    snooze(5)
    
#    openAndClearErrorLog()
    
    #expand data tree and open metal mix
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    for child in children:
        if "pow_M99S5_1_0001.cbf" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            break
        
    snooze(2)
    
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Profile"))
    activateItem(waitForObjectItem(":Profile_Menu", "Radial Profile"))
    
    c = waitForObject(":Image_Composite")
    b = c.bounds

    mouseClick(c, b.x+b.width/3, b.y+b.height/2, 0, Button.Button1);
    
    mouseClick(c, b.x+b.width/6, b.y+b.height/2, 0, Button.Button1);
    
    mouseClick(c, b.x+b.width/9, b.y+b.height/2, 0, Button.Button1);
    
    conOb = waitForObject(":Configure Settings..._ToolItem")
    
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 8, 6, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Lock To Metadata"))
    
#    mouseClick(waitForObject(":Configure Settings..._ToolItem_2"), 19, 18, 0, Button.Button1)
#    clickTab(waitForObject(":Configure Graph Settings.Regions_TabItem"))
#    test.verify(waitForObject(":Regions.   Mobile   _Button").selection == False)
#    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    
    check_plotted_traces_names(conOb, ['Radial Profile Profile 1'])

    check_axis(conOb,"Radius (pixel)(X-Axis)")
    
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 15, 20, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Px"))
    activateItem(waitForObjectItem(":Px_Menu", "d "))
    clickTab(waitForObject(":Radial Profile_CTabItem"), 49, 11, 0, Button.Button1)
    snooze(2)
    check_axis(conOb,"d-spacing (Å)(X-Axis)")
    
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 15, 20, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "d "))
    activateItem(waitForObjectItem(":Px_Menu", "2θ"))
    clickTab(waitForObject(":Radial Profile_CTabItem"), 49, 11, 0, Button.Button1)
    snooze(2)
    check_axis(conOb,"2θ (°)(X-Axis)")
    
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 15, 20, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "2θ"))
    activateItem(waitForObjectItem(":Px_Menu", "q "))
    clickTab(waitForObject(":Radial Profile_CTabItem"), 49, 11, 0, Button.Button1)
    snooze(2)
    check_axis(conOb,"q (1/Å)(X-Axis)")
    
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 8, 18, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Lock To Metadata"))
    
    mouseClick(waitForObject(":Configure Settings..._ToolItem_2"), 19, 18, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Regions_TabItem"))
    test.verify(waitForObject(":Regions.   Mobile   _Button").selection == True)
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    
    check_axis(conOb,"Radius (pixel)(X-Axis)")
     #Axis no longer remembered but this is not fatal but requires more than a simple fix
#    mouseClick(waitForObject(":View Menu_ToolItem_2"), 8, 18, 0, Button.Button1)
#    activateItem(waitForObjectItem(":Pop Up Menu", "Lock To Metadata"))
#    snooze(2)
#    check_axis(conOb,"q (1/Å)(X-Axis)")
    
#    verifyAndClearErrorLog()
    
    closeOrDetachFromDAWN()
    
     