source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))

import os

def main():
    
    # This user has a lot of visits.
    startOrAttachToDAWN(False, "-Duser.name=awa25")
  
    openPerspective("ISPyB")

    snooze(15) # We wait for a while and if his visits are not here
               # the tests will FAIL. 30s should be long enough for
               # the visits that he has. Although as more visits 
               # accumulate, this limit might be reached.
               
    # We are trying to select cm5925-5 here.
    mouseClick(waitForObject(":NLS missing message: BreadcrumbItemDropDown_showDropDownMenu_action_toolTip in: org.dawnsci.common.widgets.breadcrumb.BreadcrumbMessages_ToolItem_2"), 9, 13, 0, Button.Button1)
    mouseClick(waitForObjectItem(":_Tree", "2013   (135 visits)"), 37, 11, 0, Button.Button1)
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Return>")
    mouseClick(waitForObjectItem(":Data Collections_Table", "7/1"), 65, 12, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Autoprocessing Results_Tree", "xia2    (3daii)"), 12, 12, 0, Button.Button1)
    clickTab(waitForObject(":Image Preview_CTabItem"), 17, 14, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data Collections_Table", "7/1"), 58, 17, 0, Button.Button1)
    clickTab(waitForObject(":2_TabItem"))
    clickTab(waitForObject(":3_TabItem"))
    clickTab(waitForObject(":4_TabItem"))
    clickTab(waitForObject(":Spot Summary_CTabItem"), 49, 12, 0, Button.Button1)
    mouseClick(waitForObject(":Show image by dragging a line on plot_ToolItem"), 7, 13, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data Collections_Table", "7/1"), 94, 16, 0, Button.Button1)

    snooze(20) # Wait for the info to come in from ISPyB
    
    # We check that the spots were plotted after all this and the image too.
    system = getPlottingSystem("Spot Summary")
    test.verify(system.getTraces().size()==3, "3 Traces in Spot Summary : Success")
    
    system = getPlottingSystem("Image")
    test.verify(system.getTraces().size()==1, "1 Image shown for scan start : Success")
    
    # Simply check that we have the plotting systems with images in as expected.
    
    closeOrDetachFromDAWN()

