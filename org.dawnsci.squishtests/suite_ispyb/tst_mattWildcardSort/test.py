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

    
    mouseClick(waitForObject(":Search using wildcard_ToolItem"), 18, 10, 0, Button.Button1)
    type(waitForObject(":Data Collections_Combo"), "J")
    snooze(1)
    type(waitForObject(":Data Collections_Combo"), "<Backspace>")
    snooze(1)
    type(waitForObject(":Data Collections_Combo"), "J")
    snooze(1)
    type(waitForObject(":Data Collections_Combo"), "M")
    snooze(1)
    type(waitForObject(":Data Collections_Combo"), "J")
    snooze(1)
    type(waitForObject(":Data Collections_Combo"), "D")
    snooze(1)
    type(waitForObject(":Data Collections_Combo"), "2")
    snooze(1)
    type(waitForObject(":Data Collections_Combo"), "A")
    snooze(1)
    type(waitForObject(":Data Collections_Combo"), "A")
    snooze(1)
    type(waitForObject(":Data Collections_Combo"), "-")
    snooze(1)
    type(waitForObject(":Data Collections_Combo"), "x")
    snooze(1)
    type(waitForObject(":Data Collections_Combo"), "5")
    snooze(1)
    type(waitForObject(":Data Collections_Combo"), "4")
    snooze(1)
    type(waitForObject(":Data Collections_Combo"), "7")
    snooze(1)

    mouseClick(waitForObjectItem(":Data Collections_Table", "0/1"), 53, 14, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data Collections_Table", "1/1"), 58, 16, 0, Button.Button1)
    closeOrDetachFromDAWN()
