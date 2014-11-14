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
               

    # We try to select nt5966-4.
    mouseClick(waitForObject(":NLS missing message: BreadcrumbItemDropDown_showDropDownMenu_action_toolTip in: org.dawnsci.common.widgets.breadcrumb.BreadcrumbMessages_ToolItem_2"), 10, 10, 0, Button.Button1)
    mouseClick(waitForObjectItem(":_Tree", "2013   (33 visits)"), 38, 11, 0, Button.Button1)
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
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Down>")
    type(waitForObject(":_Tree"), "<Return>")
    
    # Do some testing of MCAs
    mouseClick(waitForObject(":MCA Spectra_ToolItem_2"), 7, 10, 0, Button.Button1)
    mouseClick(waitForObjectItem(":MCA Spectra_Table", "1/2"), 8, 12, 0, Button.Button1)

    clickTab(waitForObject(":Spot Summary_CTabItem"), 44, 12, 0, Button.Button1)
    
    system = getPlottingSystem("Spot Summary") # This is really the MCA plot now
    test.verify(system.getTraces().size()==1, "1 Trace in Fluorescence : Success")
    test.verify(system.getAnnotation("Ni-K"), "Cannot find the Nickel-L peak, perhaps something went wrong.")

    
    closeOrDetachFromDAWN()
