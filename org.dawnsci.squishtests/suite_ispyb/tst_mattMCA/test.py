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
    
    mouseClick(waitForObject(":MCA Spectra_ToolItem_2"), 7, 10, 0, Button.Button1)
    mouseClick(waitForObjectItem(":MCA Spectra_Table", "1/2"), 8, 12, 0, Button.Button1)
    clickTab(waitForObject(":Spot Summary_CTabItem"), 44, 12, 0, Button.Button1)
    
    system = getPlottingSystem("Spot Summary") # This is really the MCA plot now
    test.verify(system.getTraces().size()==1, "1 Trace in Fluorescence : Success")
    test.verify(system.getAnnotation("OS-L"), "Cannot find the Osmium-L peak, perhaps something went wrong.")

    
    closeOrDetachFromDAWN()
