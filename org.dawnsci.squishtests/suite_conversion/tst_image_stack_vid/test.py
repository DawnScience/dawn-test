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
    
    # Copy external to example.
    addExternalFile("two_images.h5", "suite_conversion", "tst_image_stack_vid", "data", "examples")
    openExample("two_images.h5")

    # Open wizard
    projectViewMenu = getToolItemOfCTabFolder(cTabItemText="Project Explorer", cTabItemTooltipText="Workspace",
                                      toolItemTooltipText="View Menu")
    mouseClick(waitForObject(projectViewMenu))
    activateItem(waitForObjectItem(":Pop Up Menu", "Convert..."))

    # Use wizard
    mouseClick(waitForObjectItem(":Conversion Type_Combo", " video from image stack"), 0, 0, 0, Button.NoButton)    
    clickButton(waitForObject(":Next >_Button"))
    clickButton(waitForObject(":Finish_Button"))
    mouseClick(waitForObjectItem(":Project Explorer_Tree", "data"))
    type(waitForObject(":Project Explorer_Tree"), "<F5>")
    
    # Open result
    isExample = checkExample("two_images.avi")
    test.verify(isExample is True, "Checking video file written")

    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
