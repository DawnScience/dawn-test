source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))

# This test makes sure we can start and stop DAWN
def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    
    # On a test you may add test code here 
    #Open data browsing perspective
    openPerspective("Data Browsing")
    
    
    openExternalFile("315029.dat")
    snooze(1) 
    mouseClick(waitForObjectItem(":Data_Table_6", "10/0"), 8, 9, 0, Button.Button1)
    snooze(3) 
    mouseClick(waitForObjectItem(":Data_Table_7", "0/2"), 19, 27, 0, Button.Button1)
    mouseDrag(waitForObject(":Data_Scale_3"), 16, 24, 70, 2, Modifier.None, Button.Button1)
    
    system = getPlottingSystem("315029.dat")
    # Check 2D plotted
    test.verify(system.getTraces().iterator().next().getData().getRank()==2, "Check image plotted")

     
    clickTab(waitForObject(":Data_CTabItem"), 25, 10, 0, Button.Button1)
    mouseClick(waitForObject(":Slice as line plots_ToolItem_4"), 17, 14, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table_7", "1/2"), 30, 36, 0, Button.Button1)
    mouseDrag(waitForObject(":Data_Scale_3"), 19, 22, 45, 1, Modifier.None, Button.Button1)
    # Check 1D plotted
    snooze(2)
    test.verify(system.getTraces().iterator().next().getData().getRank() == 1, "Check XY plot")

    # Exit (or disconnect) DAWN

    closeOrDetachFromDAWN()
