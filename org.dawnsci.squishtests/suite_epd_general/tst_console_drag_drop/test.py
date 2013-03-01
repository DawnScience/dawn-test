source(findFile("scripts", "utilities.py"))

def main():
    startOrAttachToDAWN()
    setupEPDPython()
    
    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Preferences"))
    expand(waitForObjectItem(":Preferences_Tree", "PyDev"))
    mouseClick(waitForObjectItem(":Preferences_Tree", "Interactive Console"))
    connectDebug = waitForObject(":Preferences.Connect console to Variables Debug View?_Button")
    if not connectDebug.getSelection():
        clickButton(connectDebug)
    clickButton(waitForObject(":Preferences.OK_Button"))

    openPerspective("Debug")
    openPyDevConsole()
        
    # XXX Dropping in Squish seems to require the horizontal scroll bar to be enabled, do this by printing a long line
    # Squish provided a patched version that resolves this issue, but it doen't appear to work on all platforms (e.g. win64)
    # It is expected a full fix will be available in Squish 4.3
    mouseClick(waitForObject(":Clear Console_ToolItem"))
    type(waitForObject(":PyDev Console"), "print 'X' * 1000")
    type(waitForObject(":PyDev Console"), "<Return>")
    snooze(5)
    type(waitForObject(":PyDev Console"), "myvar='Kichwa Was Here'")
    type(waitForObject(":PyDev Console"), "<Return>")
    mouseClick(waitForObjectItem(":Variables_Tree", "myvar"))
    dragAndDrop(waitForObjectItem(":Variables_Tree", "myvar"), 5, 5, ":PyDev Console", 5, 5, DnD.DropCopy)
    mouseClick(waitForObject(":PyDev Console"))
    type(waitForObject(":PyDev Console"), "<Ctrl+End>")
    type(waitForObject(":PyDev Console"), "<Home>")
    type(waitForObject(":PyDev Console"), "print ")

    type(waitForObject(":PyDev Console"), "<Return>")
    # We need to wait a moment while the python executes the print above
    # We don't (yet?) have a good way to synchronize on this event 
    # (Note, it may be best to waitFor() the text ending with '>>> ' which implies that
    #  python is done and new commands can be entered)
    snooze(10)
    expected = "\nKichwa Was Here\n>>> "
    got = waitForObject(":PyDev Console", 15000).text
    if got.endswith(expected):
        test.verify(True, "Variable dropped successfully and printed expected value")
    else:
    	test.fail("Console had unexpected text, Expected endswith '%s', got '%s'" % (expected, got))

    closeOrDetachFromDAWN()

