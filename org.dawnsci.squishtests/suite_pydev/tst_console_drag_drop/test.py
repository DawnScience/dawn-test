source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_python_setup.py"))

# FIXME this will not run with PyDev 5.5 as the variables view is empty when debug with console
def main():
    startOrAttachToDAWN()
    setupPython()
    
    setPyDevPref_ConnectToDebugSession()
    openPerspective("Debug")
    openPyDevConsole()
        
    # XXX Dropping in Squish seems to require the horizontal scroll bar to be enabled, do this by printing a long line
    # Squish provided a patched version that resolves this issue, but it doen't appear to work on all platforms (e.g. win64)
    # It is expected a full fix will be available in Squish 4.3
    mouseClick(waitForObject(":Clear Console_ToolItem"))
    typeInConsole("print 'X' * 1000")
    typeInConsole("myvar='Kichwa Was Here'")
    mouseClick(waitForObjectItem(":Variables_Tree", "myvar"))
    dragAndDrop(waitForObjectItem(":Variables_Tree", "myvar"), 5, 5, ":PyDev Console", 5, 5, DnD.DropCopy)
    mouseClick(waitForObject(":PyDev Console"))
    type(waitForObject(":PyDev Console"), "<Ctrl+End>")
    type(waitForObject(":PyDev Console"), "<Home>")
    type(waitForObject(":PyDev Console"), "print ")

    typeReturnAndWaitForPrompt()
    expected = "\nKichwa Was Here\n>>> "
    got = waitForObject(":PyDev Console", 15000).text
    if got.endswith(expected):
        test.verify(True, "Variable dropped successfully and printed expected value")
    else:
        test.fail("Console had unexpected text, Expected endswith '%s', got '%s'" % (expected, got))

    closeOrDetachFromDAWN()

