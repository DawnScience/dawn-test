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
               

    
    
    mouseClick(waitForObject(":NLS missing message: BreadcrumbItemDropDown_showDropDownMenu_action_toolTip in: org.dawnsci.common.widgets.breadcrumb.BreadcrumbMessages_ToolItem_2"), 6, 10, 0, Button.Button1)

    # We try to select cm4950-5 THIS MIGHT BREAK as more collections come in.
    mouseClick(waitForObject(":NLS missing message: BreadcrumbItemDropDown_showDropDownMenu_action_toolTip in: org.dawnsci.common.widgets.breadcrumb.BreadcrumbMessages_ToolItem_2"), 2, 10, 0, Button.Button1)
    mouseClick(waitForObjectItem(":_Tree", "Beamlines"), 26, 8, 0, Button.Button1)
    mouseClick(waitForObjectItem(":_Tree", "I03"), 5, 8, 0, Button.Button1)
    mouseClick(waitForObjectItem(":_Tree", "2014   (15 visits)"), 29, 10, 0, Button.Button1)
    type(waitForObject(":_Tree"), "<Return>")


    # We simply click on things and check that they exist. 
    # Not a great test but at least we check UI is selectable as expcected.
    mouseClick(waitForObjectItem(":Data Collections_Table", "0/1"), 60, 10, 0, Button.Button1)
    expand(waitForObjectItem(":Autoprocessing Results_Tree", "xia2    (3dii)"))
    expand(waitForObjectItem(":Autoprocessing Results_Tree", "xia2    (3d)"))
    expand(waitForObjectItem(":Autoprocessing Results_Tree", "fast__dp"))
    mouseClick(waitForObjectItem(":Data Collections_Table", "1/1"), 43, 12, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Characterization Strategy_Tree", "Mosflm native"), -36, 10, 0, Button.Button1)

    mouseClick(waitForObjectItem(":Characterization Strategy_Tree", "Mosflm anomalous"), 111, 10, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Characterization Strategy_Tree", "EDNAStrategy5"), 94, 14, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Characterization Strategy_Tree", "EDNAStrategy4"), 100, 21, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Characterization Strategy_Tree", "EDNAStrategy3"), 100, 11, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Characterization Strategy_Tree", "EDNAStrategy2"), 94, 19, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Characterization Strategy_Tree", "EDNAStrategy1"), 96, 11, 0, Button.Button1)
   
    closeOrDetachFromDAWN()