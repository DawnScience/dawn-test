source(findFile("scripts", "utilities.py"))

def main():
    startOrAttachToDAWN()
    setupEPDPython()

    waitForObject(":Workbench Window")

    openPerspective("Python")

    # Make sure Plot 1 starts up in expected clean state (no *)
    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Show Plot View"))
    test.verify(waitFor('waitForObjectItem(":Show Plot View_Menu", "Plot 1")', 20000), "Plot 1 has no data")
    activateItem(waitForObjectItem(":Show Plot View_Menu", "Plot 1"))

    openPyDevConsole()

    mouseClick(waitForObject(":Clear Console_ToolItem"))
    typeInConsole("import scisoftpy as dnp")
    typeInConsole("dnp.plot.image(dnp.random.rand(100,100))")
    test.passes("Sent image plot request for rand(100,100) data")

    # Test that the plot 1 now has data (has *) 
    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Show Plot View"))
    test.verify(waitFor('waitForObjectItem(":Show Plot View_Menu", "Plot 1 *")', 20000), "Plot 1 has newly plotted data")
    activateItem(waitForObjectItem(":Show Plot View_Menu", "Plot 1 *"))
    
    snooze(1.0)

    closeOrDetachFromDAWN()

