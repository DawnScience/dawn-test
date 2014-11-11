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
    
    openPerspective("Workflow")
    createProject("workflows")
    openExample("python_pydev_numpy_example1.moml", "workflows", "examples")
    
    widget = waitForObject(":python_pydev_numpy_example1.moml.Edit_CTabItem", 3000)
    clickTab(widget)

#    mouseClick(waitForObject(":_ImageFigure_6"), 24, 5, 0, Button.Button1)
#    mouseClick(waitForObjectItem(":Actor Attributes_Table", "6/1"), 272, 5, 0, Button.Button1)
#
#
#    mouseClick(waitForObjectItem(":Actor Attributes_Table", "3/1"), 633, 11, 0, Button.Button1)
#    mouseClick(waitForObject(":Actor Attributes_CCombo"), 685, 7, 0, Button.Button1)
#    freeLocation = "Enthought EPD Free - " + getPythonLocation(epdInstalled=True) # Need to change setupPython to setupEPDPython()
#    mouseClick(waitForObjectItem(":_List", freeLocation), 178, 12, 0, Button.Button1)
# 
#
#    mouseClick(waitForObject(":Save (Ctrl+S)_ToolItem"), 12, 4, 0, Button.Button1)
    mouseClick(waitForObject(":Run the workflow from start to end until finished._ToolItem"))
    snooze(120)


    clickTab(waitForObject(":MoKedge_1_151.h5_CTabItem"), 81, 9, 0, Button.Button1)

    system = getPlottingSystem("MoKedge_1_151.h5")
    test.verify(system.getTraces().size() == 4, "Check correct traces plotted")
    
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
