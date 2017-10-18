source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_constants.py"))

# This test makes sure we can start and stop DAWN
def main():
    vals = dawn_constants
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    
    # On a test you may add test code here 
    #Open data browsing perspective
    openPerspective("Data Browsing (default)")
    
    snooze(5)
    #openAndClearErrorLog()
    
    openExample("pow_M99S5_1_0001.cbf")
    snooze(1)
    

    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Profile"))
    activateItem(waitForObjectItem(":Profile_Menu", "Zoom Profile"))
    
    c = waitForObject("{container=':ref-testscale_1_001.img.Image_CTabItem' isvisible='true' occurrence='4' type='org.eclipse.swt.widgets.Composite'}")
    b = c.bounds

    mouseDrag(c, b.x+b.width/8, b.y+b.height/3, int(b.width/4),b.height/3, 0, Button.Button1)
    
    snooze(2)
    
    mouseClick(waitForObject(":Configure Settings..._ToolItem"), 8, 5, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Image Traces_TabItem"))
    test.verify(waitForObject(":Select Trace_Combo_2").text == "Zoom 1","Test Zoom trace present")
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    
    
    
    mouseClick(waitForObject(":Configure Settings..._ToolItem_2"), 6, 9, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Regions_TabItem"))

    mouseClick(waitForObjectItem(":Regions.Region Location_Table", "0/1"), 49, 12, 0, Button.Button1)
    type(waitForObject(":Regions_Text"), "500")
    mouseClick(waitForObjectItem(":Regions.Region Location_Table", "0/2"), 5, 11, 0, Button.Button1)
    type(waitForObject(":Regions_Text"), "500")
    mouseClick(waitForObjectItem(":Regions.Region Location_Table", "1/1"), 94, 7, 0, Button.Button1)
    type(waitForObject(":Regions_Text"), "1000")
    mouseClick(waitForObjectItem(":Regions.Region Location_Table", "1/2"), 30, 11, 0, Button.Button1)
    type(waitForObject(":Regions_Text"), "1000")
    clickButton(waitForObject(":Configure Graph Settings.Apply_Button"))
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    mouseClick(waitForObject(":Configure Settings..._ToolItem"), 18, 20, 0, Button.Button1)

    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    
    maxX = float(findObject(":Change Settings.Maximum_Text").text)
    minX = float(findObject(":Change Settings.Minimum: _Text").text)
    
    size = abs(maxX-minX)
    test.verify(abs(maxX-minX) == 1000,"Test Zoom trace dimensions")
    
    mouseClick(waitForObjectItem(":Select Axis_Combo", "(Y-Axis)"), 18, 20, 0, Button.Button1)
    
    maxY = float(findObject(":Change Settings.Maximum_Text").text)
    minY = float(findObject(":Change Settings.Minimum: _Text").text)
    
    test.verify(abs(maxY-minY) == 1000,"Test Zoom trace dimensions")
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    
    mouseClick(waitForObject(":View Menu_ToolItem"), 13, 6, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open 'Zoom Profile' in dedicated view"))
    
    mouseClick(waitForObject(":Configure Settings..._ToolItem"), 8, 5, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Image Traces_TabItem"))
    test.verify(waitForObject(":Select Trace_Combo_2").text == "Zoom 1","Test Zoom trace present")
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    
    #verifyAndClearErrorLog()
    # Exit (or disconnect) DAWN

    closeOrDetachFromDAWN()
