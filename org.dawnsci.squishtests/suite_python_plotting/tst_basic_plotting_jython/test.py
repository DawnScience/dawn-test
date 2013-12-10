source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_global_python_setup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))
source(findFile("scripts", "plotting_test.py"))
    
def main():
    
    #Start using clean workspace
    startOrAttachToDAWN()
    
    openPerspective("Python")
    
    clickTab(waitForObject(":Console_CTabItem_2"), 58, 4, 0, Button.Button3)
    activateItem(waitForObjectItem(":Pop Up Menu", "Size"))
    activateItem(waitForObjectItem(":Size_Menu", "Top"))
    type(waitForObject(":_Sash_2"), "<Up>")
    type(waitForObject(":_Sash_2"), "<Up>")
    type(waitForObject(":_Sash_2"), "<Up>")
    type(waitForObject(":_Sash_2"), "<Up>")
    type(waitForObject(":_Sash_2"), "<Up>")
    type(waitForObject(":_Sash_2"), "<Up>")
    type(waitForObject(":_Sash_2"), "<Up>")
    type(waitForObject(":_Sash_2"), "<Up>")
    type(waitForObject(":_Sash_2"), "<Up>")
    type(waitForObject(":_Sash_2"), "<Up>")
    type(waitForObject(":_Sash_2"), "<Up>")
    type(waitForObject(":_Sash_2"), "<Up>")
    clickTab(waitForObject(":Console_CTabItem_2"), 27, 12, 0, Button.Button1)

    system = getPlottingSystem("Plot 1")
    
    mouseClick(waitForObject(":Open Console_ToolItem"), 16, 14, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "5 PyDev Console"))
    clickButton(waitForObject(":Jython console_Button"))
    clickButton(waitForObject(":OK_Button"))
    
    counter = 0
    while (not object.exists(":PyDev Console")):
        if (counter < 50):
            snooze(2)
            counter +=1
        else:
            test.fatal("time out waiting for console")
            closeOrDetachFromDAWN()
            return
    
    got = waitForObject(":PyDev Console").text
    ready = False
    counter = 0
    
    while (not got.endswith("\n>>> ") or not ready):
        ready = got.endswith("\n>>> ")
        snooze(2)
        got = waitForObject(":PyDev Console").text
        if (counter > 50):
            test.fatal("Console did not initialize")
            closeOrDetachFromDAWN()
            return
        counter +=1
    
    plotting_script_test(system)
    
    closeOrDetachFromDAWN()