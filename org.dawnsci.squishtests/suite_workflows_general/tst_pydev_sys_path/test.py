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
    
    activateItem(waitForObjectItem(":_Menu", "File"))
    activateItem(waitForObjectItem(":File_Menu", "Import..."))
    type(waitForObject(":_Text"), "Existing Projects into Workspace")
    mouseClick(waitForObjectItem(":_Tree", "Existing Projects into Workspace"))
    clickButton(waitForObject(":Next >_Button"))
    clickButton(waitForObject(":Select root directory:_Button"))

    path = findFile("testdata", "pydev_test_lib")
    path = os.path.abspath(path)
    rootpath = os.path.dirname(path)

    type(waitForObject(":_Text"), rootpath)
    type(waitForObject(":_Text"), "<Tab>")
    clickButton(waitForObject(":Copy projects into workspace_Button"))
    snooze(5)
    clickButton(waitForObject(":Finish_Button"))

    openExample("python_import.moml", "pydev_test_project", None)
    
    clickTab(waitForObject(":python_import.moml_CTabItem"))

    mouseClick(waitForObject(":Run the workflow from start to end until finished._ToolItem"))
    clickTab(waitForObject(":new_data_file1.h5_CTabItem", 120000))
    expand(waitForObjectItem(":Tree_Tree", "entry"))
    expand(waitForObjectItem(":Tree_Tree", "dictionary"))
    # Make sure that all scripts finished completely and contributed to the data
    mouseClick(waitForObjectItem(":Tree_Tree", "a"))
    mouseClick(waitForObjectItem(":Tree_Tree", "b"))
    mouseClick(waitForObjectItem(":Tree_Tree", "c"))
    mouseClick(waitForObjectItem(":Tree_Tree", "d"))
    mouseClick(waitForObjectItem(":Tree_Tree", "e"))
    
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
