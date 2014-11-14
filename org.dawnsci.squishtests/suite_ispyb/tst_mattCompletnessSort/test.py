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


    mouseClick(waitForObject(":Search using query_ToolItem"), 15, 10, 0, Button.Button1)
    
    # This checks that at least 4 results were found with complete>=99.9
    type(waitForObject(":Data Collections_Combo"), "complete ge 99.9")
    type(waitForObject(":Data Collections_Combo"), "<Return>")
    snooze(10)    
    mouseClick(waitForObjectItem(":Data Collections_Table", "0/1"), 82, 10, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data Collections_Table", "1/1"), 85, 8, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data Collections_Table", "2/1"), 89, 13, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data Collections_Table", "3/1"), 92, 16, 0, Button.Button1)
    
    # this checks that at least 9 results were found with complete>=99.8
    type(waitForObject(":Data Collections_Combo"), "complete ge 99.8")
    type(waitForObject(":Data Collections_Combo"), "<Return>")
    snooze(10)    
    mouseClick(waitForObjectItem(":Data Collections_Table", "0/2"), 87, 16, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data Collections_Table", "1/2"), 84, 12, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data Collections_Table", "2/2"), 92, 7, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data Collections_Table", "3/2"), 102, 15, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data Collections_Table", "4/2"), 106, 9, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data Collections_Table", "5/2"), 96, 8, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data Collections_Table", "6/2"), 106, 12, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data Collections_Table", "7/2"), 109, 12, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data Collections_Table", "8/2"), 114, 5, 0, Button.Button1)
    
    # Checks that at least 4 are found with this query.
    type(waitForObject(":Data Collections_Combo"), "protein.contains(\"JMJD2AA\") and complete gt 99.8")
    type(waitForObject(":Data Collections_Combo"), "<Return>")
    snooze(10)
    mouseClick(waitForObjectItem(":Data Collections_Table", "0/1"), 88, 5, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data Collections_Table", "1/1"), 88, 11, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data Collections_Table", "2/1"), 97, 10, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data Collections_Table", "3/1"), 98, 16, 0, Button.Button1)
    
    
    closeOrDetachFromDAWN()
