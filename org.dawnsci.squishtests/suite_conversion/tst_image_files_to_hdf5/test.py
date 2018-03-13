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
    openPerspective("Data Browsing")
    
    # Copy external to example.
    checkExample("", "data", "examples", "results")

    # Open wizard
    projectViewMenu = getToolItemOfCTabFolder(cTabItemText="Project Explorer", cTabItemTooltipText="Workspace",
                                      toolItemTooltipText="View Menu")
    mouseClick(waitForObject(projectViewMenu))
    activateItem(waitForObjectItem(":Pop Up Menu", "Convert..."))

    # Use wizard
    mouseClick(waitForObjectItem(":Conversion Type_Combo", " nexus stack from directory of images"), 0, 0, 0, Button.NoButton)    
    clickButton(waitForObject(":Next >_Button"))
    clickButton(waitForObject(":Finish_Button"))
    mouseClick(waitForObjectItem(":Project Explorer_Tree", "data"))
    type(waitForObject(":Project Explorer_Tree"), "<F5>")
    
    # Open result
    openExample("ConvertedImageStack.nxs", "data", "examples", "results")
   
    # Data set is only one, so it will be plotted automatically.    
    system = getPlottingSystem("ConvertedImageStack.nxs")

    test.verify(system.getTraces().iterator().next().getData().getRank() == 2, "Something 2D was plotted")

    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
