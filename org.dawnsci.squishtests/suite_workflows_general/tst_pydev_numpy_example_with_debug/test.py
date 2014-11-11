source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_global_python_setup.py"))

import os
from datetime import datetime

'''
Requires that a path with 'python' in it exists
and that that python has numpy importable.
'''
def main():

    # Start or attach runs (or attaches) to DAWN and then
    # makes sure the workbench window exists and finally
    # will close the Welcome screen
    startOrAttachToDAWN()

    setupPython()

    # Starting the Debug Server wouldn't be needed if http://jira.diamond.ac.uk/browse/DAWNSCI-762
    # is completed/resolved
    openPerspective("Debug")
    activateItem(waitForObjectItem(":_Menu", "Pydev"))
    activateItem(waitForObjectItem(":Pydev_Menu", "Start Debug Server"))

    openPerspective("Workflow")

    createProject("workflows")
    openExample("python_pydev_numpy_example1.moml", "workflows", "examples")

    widget = waitForObject(":python_pydev_numpy_example1.moml.Edit_CTabItem", 3000)
    clickTab(widget)

    # Set PyDev actor to be Debug
    mouseClick(waitForObject(":_ImageFigure_6"), 24, 5, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Actor Attributes_Table", "6/1"), 7, 13, 0, Button.Button1)
    mouseClick(waitForObject(":Save (Ctrl+S)_ToolItem"), 16, 14, 0, Button.Button1)

    mouseClick(waitForObject(":_ImageFigure_6"), 24, 5, 0, Button.Button3)
    activateItem(waitForObjectItem(":_Menu_3", "Open 'python__script5.py'"))
    snooze(3)

    openPerspective("Debug")
    toggleBreakpointAtLine(11)

    clickTab(waitForObject(":python_pydev_numpy_example1.moml_CTabItem"))

    # Run the workflow, it will stop just before defining lnI0It
    # Check:
    mouseClick(waitForObject(":Run the workflow from start to end until finished._ToolItem"))
    # a) that the variables are as expected
    waitFor("getVariableNames() == set(['Globals', 'I0', 'It', 'kwargs'])", 120000)
    # do a single step over
    mouseClick(waitForObject(":Step &Over (F6)_ToolItem"))
    # b) check the new variable is defined
    waitFor("getVariableNames() == set(['Globals', 'I0', 'It', 'kwargs', 'lnI0It'])", 10000)
    # and continue
    mouseClick(waitForObject(":Resu&me (F8)_ToolItem"))

    clickTab(waitForObject(":MoKedge_1_151.h5_CTabItem"), 81, 9, 0, Button.Button1)

    system = getPlottingSystem("MoKedge_1_151.h5")
    test.verify(system!=None, "Check plot expected")

    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
