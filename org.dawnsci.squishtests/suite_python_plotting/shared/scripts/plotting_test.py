def getFirstDataset(system):
    trcs = system.getTraces()
    
    if (trcs.size() == 0): return None
    
    tarray = trcs.toArray()
    
    return tarray.at(0).getData()

def createConsole():
    
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

    setupPython()
    
    system = getPlottingSystem("Plot 1")

    openPydevConsole()
        
    return system

def openPydevConsole():
    mouseClick(waitForObject(":Open Console_ToolItem"), 16, 14, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "5 PyDev Console"))
    clickButton(waitForObject(":Python console_Button"))
    clickButton(waitForObject(":OK_Button"))
    
    waitForResponse()

def openDataBrowsingConsole():
    
    mouseClick(waitForObject(":Open Console_ToolItem_4"), 34, 11, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "5 PyDev Console"))
    clickButton(waitForObject(":Python console_Button"))
    clickButton(waitForObject(":OK_Button"))
    
    waitForResponse()


def waitForResponse():
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

def plotting_script_test(system):
    
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "dnp.plot.image(dnp.random.rand(100,200))")
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "<Return>")
    snooze(1)
    
    trcs = system.getTraces()
    test.verify(trcs.size() == 1, "test image")
    
    data = getFirstDataset(system)
    
    if (data != None):
        test.verify(data.getShape().at(0) == 100, "test shape")
        test.verify(data.getShape().at(1) == 200, "test shape")
    else:
        test.fail("data is none")
    
    
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "dnp.plot.clear()")
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "<Return>")
    snooze(1)
    
    trcs = system.getTraces()
    test.verify(trcs.size() == 0, "test clear")
    
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "dnp.plot.line(dnp.arange(100),dnp.random.rand(100))")
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "<Return>")
    snooze(1)
    trcs = system.getTraces()
    test.verify(trcs.size() == 1, "test trace")
    data = getFirstDataset(system)
    if (data != None):
        test.verify(data.getShape().at(0) == 100, "test shape")
    else:
        test.fail("data is none")
    
    
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "dnp.plot.clear()")
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "<Return>")
    snooze(1)
    
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "dnp.plot.line(dnp.arange(100),(dnp.random.rand(100),dnp.random.rand(100)))")
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "<Return>")
    snooze(1)
    trcs = system.getTraces()
    test.verify(trcs.size() == 2, "test traces")
    data = getFirstDataset(system)
    if (data != None):
        test.verify(data.getShape().at(0) == 100, "test shape")
    else:
        test.fail("data is none")
    
    
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "dnp.plot.clear()")
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "<Return>")
    snooze(1)
    
    trcs = system.getTraces()
    test.verify(trcs.size() == 0, "test clear")
    
    openExternalFile("test_plot.py")
    
    snooze(1)
    
    clickTab(waitForObject(":test_plot_CTabItem"), 54, 11, 0, Button.Button1)
    snooze(1)
    mouseClick(waitForObject(":Activates the interactive console. (Ctrl+Alt+Enter)_ToolItem"), 18, 16, 0, Button.Button1)
    snooze(1)
    
    regs = system.getRegions()
    test.verify(regs.size() == 2, "test plotted")
    
    trcs = system.getTraces()
    test.verify(trcs.size() == 1, "test plotted")