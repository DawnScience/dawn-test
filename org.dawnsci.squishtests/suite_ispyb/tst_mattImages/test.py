source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))

import os

def main():
    
    # This user has a lot of visits.
    startOrAttachToDAWN(False, "-Duser.name=fcp94556")
  
    openPerspective("ISPyB")

    snooze(15) # We wait for a while and if his visits are not here
               # the tests will FAIL. 30s should be long enough for
               # the visits that he has. Although as more visits 
               # accumulate, this limit might be reached.
               

    
    # We are trying to select nt4923-5 here
    mouseClick(waitForObject(":NLS missing message: BreadcrumbItemDropDown_showDropDownMenu_action_toolTip in: org.dawnsci.common.widgets.breadcrumb.BreadcrumbMessages_ToolItem_2"), 6, 10, 0, Button.Button1)
    mouseClick(waitForObjectItem(":_Tree", "2013   (33 visits)"), 50, 10, 0, Button.Button1)
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Return>")
    type(waitForObject(":_Tree"), "<Return>")
    mouseClick(waitForObject(":NLS missing message: BreadcrumbItemDropDown_showDropDownMenu_action_toolTip in: org.dawnsci.common.widgets.breadcrumb.BreadcrumbMessages_ToolItem_4"), 11, 13, 0, Button.Button1)
    mouseClick(waitForObjectItem(":_Tree", "JMJD2AA-x547__2"), 40, 7, 0, Button.Button1)
    mouseClick(waitForObject(":Image Gallery_Gallery"), 456, 199, 0, Button.Button1)
    clickTab(waitForObject(":Image Preview_CTabItem"), 32, 10, 0, Button.Button1)
    mouseClick(waitForObject(":Image Gallery_Gallery"), 461, 204, 0, Button.Button1)
    type(waitForObject(":Image Gallery_Gallery"), "<Right>")
    type(waitForObject(":Image Gallery_Gallery"), "<Right>")
    type(waitForObject(":Image Gallery_Gallery"), "<Right>")
    type(waitForObject(":Image Gallery_Gallery"), "<Right>")
    type(waitForObject(":Image Gallery_Gallery"), "<Right>")
    type(waitForObject(":Image Gallery_Gallery"), "<Right>")

    system = getPlottingSystem("Image Preview")
    test.verify(system.getTraces().size()==1, "1 Trace in Image Preview : Success")
    
    
    closeOrDetachFromDAWN()
