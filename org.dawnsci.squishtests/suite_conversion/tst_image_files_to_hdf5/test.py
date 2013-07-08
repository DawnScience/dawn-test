source(findFile("scripts", "dawn_global_startup.py"))
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
    checkExample("", "data", "examples", "results")

    # Open wizard
    doubleClick(waitForObject(":View Menu_ToolItem"), 5, 4, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Convert..."))

    # Use wizard
    mouseClick(waitForObjectItem(":Conversion Type_Combo", " nexus stack from directory of images"), 0, 0, 0, Button.NoButton)    
    clickButton(waitForObject(":Next >_Button"))
    clickButton(waitForObject(":Finish_Button"))
    mouseClick(waitForObjectItem(":Project Explorer_Tree", "data"))
    type(waitForObject(":Project Explorer_Tree"), "<F5>")
    
    # Open result
    openExample("ConvertedImageStack.nxs", "data", "examples", "results")
   
    # Plot the dataset.
    mouseClick(waitForObjectItem(":Data_Table_2", "0/0"))
    
    system = getPlottingSystem("ConvertedImageStack.nxs")

    test.verify(system.getTraces().iterator().next().getData().getRank() == 2, "Something 2D was plotted")

    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
