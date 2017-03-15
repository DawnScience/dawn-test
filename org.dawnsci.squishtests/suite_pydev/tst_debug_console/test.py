source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_python_setup.py"))
source(findFile("scripts", "use_case_utils.py"))

# We test that Debug integration of the console is working

def main():
    startOrAttachToDAWN()
    setupPython()
    
    openPerspective("Debug")
    setPyDevPref_ConnectToDebugSession()
    openPyDevConsole()
    
    filename = openExternalFile("debug_console.py")
    typeInConsole("runfile(r'" + filename + "')") # to cope with quoting of backslashes in Windows
# FIXME uncomment after upstream has fixed PyDev 5.5 for blank variables view when debug with console
#     waitFor("getVariableNames() >= set(['my_func'])", 10000)
    clickTab(waitForObject(":debug_console_CTabItem"))
    toggleBreakpointAtLine(":debug_console_StyledTextWithoutVerticalBar", 2)
    type(waitForObject(":PyDev Console"), 'res=my_func(1)')
    type(waitForObject(":PyDev Console"), "<Return>")

    waitFor("getVariableNames() >= set(['var1'])")
    waitFor("'res' not in getVariableNames()")
    mouseClick(waitForObject(":Step &Over (F6)_ToolItem"))
    waitFor("getVariableNames() >= set(['var1', 'var2'])")
    mouseClick(waitForObject(":Step &Over (F6)_ToolItem"))
    waitFor("getVariableNames() >= set(['var1', 'var2', 'var3'])")
    mouseClick(waitForObject(":Resu&me (F8)_ToolItem"))
    waitForPrompt()
#     waitFor("getVariableNames() >= set(['res'])")
#     waitFor("'var1' not in getVariableNames()")
#     waitFor("getVariable('res') == 'int: 6'")

    closeOrDetachFromDAWN()


