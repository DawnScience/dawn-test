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
               

    
    # We are trying to select nt4923-9 here
    mouseClick(waitForObject(":NLS missing message: BreadcrumbItemDropDown_showDropDownMenu_action_toolTip in: org.dawnsci.common.widgets.breadcrumb.BreadcrumbMessages_ToolItem_2"), 6, 10, 0, Button.Button1)
    mouseClick(waitForObjectItem(":_Tree", "2013   (33 visits)"), 50, 10, 0, Button.Button1)
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Return>")


    # We simply click on things and check that they exist. 
    # Not a great test but at least we check UI is selectable as expcected.
    mouseClick(waitForObjectItem(":Data Collections_Table", "0/1"), 88, 10, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Autoprocessing Results_Tree", "xia2    (2da)"), 11, 8, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Autoprocessing Results_Tree", "xia2    (3daii)"), 56, 8, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Autoprocessing Results_Tree", "xia2    (3da)"), 66, 11, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Autoprocessing Results_Tree", "fast__dp"), 66, 15, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data Collections_Table", "1/1"), 25, 16, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Characterization Strategy_Tree", "Mosflm native"), 38, 17, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Characterization Strategy_Tree", "Mosflm anomalous"), 34, 13, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Characterization Strategy_Tree", "EDNAStrategy4"), 36, 11, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Characterization Strategy_Tree", "EDNAStrategy3"), 37, 9, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Characterization Strategy_Tree", "EDNAStrategy2"), 39, 5, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Characterization Strategy_Tree", "EDNAStrategy1"), 49, 12, 0, Button.Button1)
    
    
    closeOrDetachFromDAWN()
