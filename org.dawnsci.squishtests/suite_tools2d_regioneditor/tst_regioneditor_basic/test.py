source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_constants.py"))
import sys
# This test makes sure we can start and stop DAWN
def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    
    # On a test you may add test code here 
    #Open data browsing perspective
    openPerspective("Data Browsing")
    vals = dawn_constants
    snooze(2)
    
    openExample("pow_M99S5_1_0001.cbf")
    snooze(1)

    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 30, 9, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Region Editor"))
    
    c = waitForObject(":Image_Composite")
    b = c.bounds

    mouseDrag(c, b.x+b.width/8, b.y+b.height/3, int(b.width/4),b.height/3, 0, Button.Button1)

    snooze(1)
    #region 2
    mouseClick(waitForObject(":Create new region_ToolItem"), 7, 8, 0, Button.Button1)
    c = waitForObject(":Image_Composite")
    b = c.bounds
    mouseDrag(c, b.x+b.width/6, b.y+b.height/3, int(b.width/8),b.height/4, 0, Button.Button1)
    snooze(1)
    #region 3
    mouseClick(waitForObject(":Create new region_ToolItem"), 7, 8, 0, Button.Button1)
    c = waitForObject(":Image_Composite")
    b = c.bounds
    mouseDrag(c, b.x+b.width/10, b.y+b.height/5, int(b.width/3),b.height/6, 0, Button.Button1)
    snooze(1)
    #we get the plotting system
    system = getPlottingSystem("pow_M99S5_1_0001.cbf")
    test.verify(system.getRegions().size()==3, "3 Regions created : Success")
    snooze(1)
    clickTab(waitForObject(":Region Editor_CTabItem"), 75, 15, 0, Button.Button1)
    snooze(0.5)
    mouseClick(waitForObject(":Region 2 *_TreeSubItem_2"), 37, 12, 0, Button.Button1)
    snooze(0.5)
    type(waitForObject(":Region Editor_Tree"), "<Delete>")
    snooze(0.5)
    #test if the region has been deleted from the plotting system
    test.verify(system.getRegions().size()==2, "1 Region deleted: Success")
    
    mouseClick(waitForObject(":Expand All_ToolItem"), 16, 15, 0, Button.Button1)
    mouseClick(waitForObject(":Region 1 *_TreeSubItem_2"), 47, 15, 0, Button.Button1)
    
    if sys.platform.startswith('win'):
        mouseClick(waitForObject(":X Start.233 *_TreeSubItem"), 23, 10, 0, Button.Button1)
    else:
        mouseClick(waitForObject(":X Start.230 *_TreeSubItem"), 74, 6, 0, Button.Button1)

    type(waitForObject(":Region Editor_Spinner"), "500")

    #test if the region one xstart is 500
    test.verify(system.getRegion("Region 1").getROI().getPointX()==500.0, "Region 1 X Start was updated, value of X was " + str(system.getRegion("Region 1").getROI().getPointX()))
   
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
