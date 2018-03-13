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
    
    snooze(5)
    
    #openAndClearErrorLog()
    # On a test you may add test code here 
    openPerspective("Data Browsing")
    
    openExample("pow_M99S5_1_0001.cbf")
    
    snooze(15)
    
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Profile"))
    activateItem(waitForObjectItem(":Profile_Menu", "Cross Hair Profile"))
    
    c = waitForObject("{container=':ref-testscale_1_001.img.Image_CTabItem' isvisible='true' occurrence='4' type='org.eclipse.swt.widgets.Composite'}")
    b = c.bounds
    
    mouseClick(c, b.x+b.width/8, b.y+b.height/3, 0, Button.Button1)
    snooze(1)
    mouseClick(c, b.x+b.width/4, b.y+b.height/5, 0, Button.Button1)
    snooze(1)
    mouseClick(c, b.x+b.width/5, b.y+b.height/2, 0, Button.Button1)
    snooze(1)
    mouseClick(c, b.x+b.width/6, b.y+b.height/4, 0, Button.Button1)
    snooze(1)
    
    
    nameList = ["X Profile 1",       "Y Profile 1", 
                "Profile 1",         "Profile 1", 
                "X Profile Static 1","Y Profile Static 1",
                "Profile Static 1",  "Profile Static 1",
                "X Profile Static 2","Y Profile Static 2",
                "Profile Static 2",  "Profile Static 2",
                "X Profile Static 3","Y Profile Static 3",
                "Profile Static 3",  "Profile Static 3",
                "X Profile Static 4","Y Profile Static 4",
                "Profile Static 4",  "Profile Static 4"]
    
    check_plotted_traces_names_contains(waitForObject(":Configure Settings..._ToolItem"), nameList)
    
    mouseClick(waitForObject(":View Menu_ToolItem_2"), 12, 7, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Clear cross hair profiles"))
    
    clickTab(waitForObject(":ref-testscale_1_001.img_CTabItem"), 103, 7, 0, Button.Button1)
    snooze(1)
    mouseMove(c, b.x+b.width/6, b.y+b.height/4)
    snooze(1)
    mouseMove(c, b.x+b.width/5, b.y+b.height/2)
    clickTab(waitForObject(":ref-testscale_1_001.img_CTabItem"), 103, 7, 0, Button.Button1)
    snooze(1)
    mouseClick(c, b.x + b.width / 8, b.y + b.height / 3, 0, Button.Button1)
    snooze(1)

    
    nameList = ["X Profile 1", "Y Profile 1",  "Profile 1",  "X Profile Static 1",  "Y Profile Static 1" ,"Profile Static 1"]
    
    try:
        check_plotted_traces_names_contains(waitForObject(":Configure Settings..._ToolItem"), nameList)
    except:
        test.fail("Cross hair profile plot showing no traces")

    closeOrDetachFromDAWN()
