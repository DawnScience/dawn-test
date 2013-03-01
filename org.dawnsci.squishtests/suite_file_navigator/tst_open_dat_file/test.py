source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))

# UI test to check that a dat file can be opened and plotted 
def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()

    # go to the dataexplore perspective
    
    # disable the decorators
    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Preferences"))
    expand(waitForObjectItem(":Preferences_Tree", "General"))
    expand(waitForObjectItem(":Preferences_Tree", "Appearance"))
    mouseClick(waitForObjectItem(":Preferences_Tree", "Label Decorations"), 27, 14, 0, Button.Button1)
    mouseClick(waitForObject(":DAT file Scan Command Decorator_ItemCheckbox"), 8, 16, 0, Button.Button1)
    mouseClick(waitForObject(":File Meta Data Decorator_ItemCheckbox"), 8, 13, 0, Button.Button1)
    clickButton(waitForObject(":Preferences.OK_Button"))
    
    # open DExplore perspective
    #mouseClick(waitForObject(":Open Perspective_ToolItem"), 7, 15, 0, Button.Button1)
    #activateItem(waitForObjectItem(":Pop Up Menu", "DExplore"))
    openPerspective("DExplore")
    
     # Expand Dat file
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    expand(waitForObjectItem(":Project Explorer_Tree", "96356.dat"))
    test.passes("expandDATFile: Success")
    doubleClick(waitForObjectItem(":Project Explorer_Tree", "eta"), 12, 14, 0, Button.Button1)
    test.passes("openDATFile: Success")
    mouseClick(waitForObjectItem(":Project Explorer_Tree", "IC1"), 19, 13, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Project Explorer_Tree", "rc"), 19, 13, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Project Explorer_Tree", "eta"), 19, 13, 0, Button.Button1)
    snooze(2.5)
    
    # open plot settings
    conOb = waitForObject(":Configure Settings..._ToolItem")
    check_plotted_trace_name_yval(conOb,"eta (96356.dat)","40.0","0.0")


    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
    
