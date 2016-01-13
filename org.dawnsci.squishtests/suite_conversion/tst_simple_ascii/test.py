source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))

# This test makes sure we can start and stop DAWN
def main():
    vals = dawn_constants
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    
    # On a test you may add test code here 
    #Open data browsing perspective
    openPerspective("Data Browsing (default)")

    # select file 
    openExample("MoKedge_1_15.nxs")

    # Open wizard
    projectViewMenu = getToolItemOfCTabFolder(cTabItemText="Project Explorer", cTabItemTooltipText="Workspace",
                                      toolItemTooltipText="View Menu")
    mouseClick(waitForObject(projectViewMenu))
    activateItem(waitForObjectItem(":Pop Up Menu", "Convert..."))

    # Use wizard
    clickButton(waitForObject(":Next >_Button"))
    clickButton(waitForObject(":Overwrite file if it exists._Button"))
    mouseClick(waitForObject(":Please tick data to export:.Select None_ToolItem"), 9, 12, 0, Button.Button1)
    mouseClick(waitForObject(":/entry1/FFI0/Energy_ItemCheckbox"), 9, 10, 0, Button.Button1)
    mouseClick(waitForObject(":/entry1/FFI0/Time_ItemCheckbox"), 7, 8, 0, Button.Button1)
    mouseClick(waitForObject(":/entry1/counterTimer01/Energy_ItemCheckbox"), 15, 8, 0, Button.Button1)
    mouseClick(waitForObject(":/entry1/counterTimer01/Iref_ItemCheckbox"), 6, 10, 0, Button.Button1)
    mouseClick(waitForObject(":/entry1/counterTimer01/Time_ItemCheckbox"), 5, 11, 0, Button.Button1)
    mouseClick(waitForObject(":/entry1/counterTimer01/lnI0It_ItemCheckbox"), 9, 14, 0, Button.Button1)
    clickButton(waitForObject(":Finish_Button"))
    mouseClick(waitForObjectItem(":Data_Table_5", "0/0"), 8, 13, 0, Button.Button1)

    # Check plotting
    system = getPlottingSystem("MoKedge_1_15.dat")

    test.verify(system.getTraces().iterator().next().getData().getRank()==1, "Check 1d plotted")

    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()

