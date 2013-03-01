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
    
    setupEPDPython() 
    
    openPerspective("Workflow")
    createProject("workflows")
    openExample("python_numpy_example1.moml", "workflows", "examples")
    
    widget = waitForObject(":python_numpy_example1.moml.Edit_CTabItem", 3000)
    clickTab(widget)

    mouseClick(waitForObject(":_ImageFigure_5"), 24, 5, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Actor Attributes_Table", "10/1"), 36, 15, 0, Button.Button1)
    type(waitForObject(":Actor Attributes_Text"), getPythonLocation())
    type(waitForObject(":Actor Attributes_Text"), "<Return>")
    mouseClick(waitForObject(":Save (Ctrl+S)_ToolItem"), 12, 4, 0, Button.Button1)
    mouseClick(waitForObject(":Run the workflow from start to end until finished._ToolItem"))
    snooze(120)


    clickTab(waitForObject(":MoKedge_1_151.h5_CTabItem"), 81, 9, 0, Button.Button1)

    system = getPlottingSystem("MoKedge_1_151.h5")
    test.verify(system.getTraces().size() == 4, "Check correct traces plotted")
    
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
