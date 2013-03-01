source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))

def main():
    
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Data Browsing (default)")
    
    snooze(5)
    
    openAndClearErrorLog()
    
    #expand data tree and open metal mix
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    for child in children:
        if "ref-testscale_1_001.img" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            break
        
    
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 26, 6, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Radial Profile"))
    
    c = waitForObject(":Image_Composite")
    b = c.bounds

    mouseClick(c, b.x+b.width/3, b.y+b.height/2, 0, Button.Button1);
    
    mouseClick(c, b.x+b.width/10, b.y+b.height/2, 0, Button.Button1);
    
    mouseClick(c, b.x+b.width/3, b.y+b.height/1.8, 0, Button.Button1);
    
    conOb = waitForObject(":Configure Settings..._ToolItem")
    
    check_plotted_traces_names(conOb, ['Radial Profile Profile 1'])

    mouseClick(waitForObject(":View Menu_ToolItem_2"), 16, 11, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Center sector 'Profile 1'"))
    activateItem(waitForObjectItem(":Center sector 'Profile 1'_Menu", "Center sector 'Profile 1'"))
    
    #check centre position
    
    mouseClick(waitForObject(":Configure Settings..._ToolItem_2"), 8, 9, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Regions_TabItem"))
    mouseClick(waitForObject(":Regions.Region Location_Label"), 253, 16, 0, Button.Button1)
    
    snooze(1)

    test.verify(waitForObjectItem(":Regions.Region Location_Table", "0/0").text == "Centre (x,y)","Table shows centre")
    test.verify(waitForObjectItem(":Regions.Region Location_Table", "0/1").text == "1,022.832*", "centre x test")
    test.verify(waitForObjectItem(":Regions.Region Location_Table", "0/2").text == "1,000.576*","centre y test")
    
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    
    check_plotted_traces_names(conOb, ['Radial Profile Profile 1'])
    #check centred
    
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 16, 11, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Symmetry setting"))
    activateItem(waitForObjectItem(":Symmetry setting_Menu", "Invert"))
    clickTab(waitForObject(":Radial Profile_CTabItem"), 49, 11, 0, Button.Button1)
    snooze(1)
    
    
    check_plotted_traces_names(conOb, ['Radial Profile Profile 1', 'Symmetry Profile 1'])

    #check two traces
    
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 8, 12, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Combine symmetry"))
    clickTab(waitForObject(":Radial Profile_CTabItem"), 49, 11, 0, Button.Button1)
    
    snooze(1)
    check_plotted_traces_names(conOb, ['Radial Profile Profile 1'])
    #check one trace

    
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 6, 13, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open 'Radial Profile' in dedicated view"))
    
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 2, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open cheat sheet for 'Radial Profile'"))

    snooze(5)
    verifyAndClearErrorLog()

    closeOrDetachFromDAWN()
