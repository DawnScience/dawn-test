source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "file_utils.py"))
source(findFile("scripts", "dawn_constants.py"))
source(findFile("scripts", "dawn_global_python_setup.py"))

import platform
import os.path

# UI test to check that an hdf5 file can be opened and its tree can be expanded 
def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    openPerspective("Python") 
    #create i12 folder in data/examples
    createDirectory("/scratch/workspace/suite_python_scripts/tst_i12_auto_peakfitting/workspace/data/examples", "i12")
    #Add peema test files to data project
    addExternalFile("36153.nxs", "suite_python_scripts", "tst_i12_auto_peakfitting", "data", "examples/i12")
    addExternalFile("i12_edxd_q_calibrator_v3_ceria.py", "suite_python_scripts", "tst_i12_auto_peakfitting", "data", "examples/i12")
    #Open Python perspective
    
    
    openPyDevConsole(type="Jython")
    #expand data tree and open metal mix
    expand(waitForObjectItem(":PyDev Package Explorer_Tree", "data"))
    expand(waitForObjectItem(":PyDev Package Explorer_Tree", "examples"))
    expand(waitForObjectItem(":PyDev Package Explorer_Tree", "i12"))

    children = object.children(waitForObjectItem(":PyDev Package Explorer_Tree", "i12"))
    
    for child in children:
        if "i12_edxd_q_calibrator_v3_ceria.py" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            continue
    snooze(1)
    clickButton(waitForObject(":Python not configured.Don't ask again_Button"))
    snooze(0.5)
    clickTab(waitForObject(":i12_edxd_q_calibrator_v3_ceria_CTabItem"), 131, 15, 0, Button.Button1)
    snooze(2)
    mouseClick(waitForObject(":Activates the interactive console. (Ctrl+Alt+Enter)_ToolItem"), 12, 8, 0, Button.Button1)
    snooze(10)
    
    #change y-axis to log
    mouseClick(waitForObject(":Configure Settings..._ToolItem_4"), 7, 10, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))
    mouseClick(waitForObjectItem(":Select Axis_Combo", "Y-Axis(Y-Axis)"), 0, 0, 0, Button.NoButton)
    clickButton(waitForObject(":Change Settings.Log_Button"))
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    
    snooze(10)
    
    system = getPlottingSystem("Plot 1")

    test.verify(system.getTraces().iterator().next().getData().getRank()==1, "Data plotted: Success")
#    proxy = waitForObject(":Plot 1_CTabItem")
#    c = proxy.control
#    b = c.bounds
    c = system.getPlotComposite()
    b = c.bounds
    test.log("Image at (%d, %d) is %d x %d" % (b.x,b.y, b.width, b.height))

    clickTab(waitForObject(":Plot 1_CTabItem"), 25, 11, 0, Button.Button1)

    mouseClick(waitForObject(":XY plotting tools_ToolItem_3"), 32, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Peak Fitting"))

    clickTab(waitForObject(":Peak Fitting_CTabItem"), 45, 8, 0, Button.Button1)
    mouseClick(waitForObject(":Number peaks to fit_ToolItem_2"), 33, 8, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Fit 7 Peaks"))
    clickTab(waitForObject(":Plot 1_CTabItem"), 30, 10, 0, Button.Button1)

    mouseClick(waitForObject(":XY plotting tools_ToolItem_3"), 18, 10, 0, Button.Button1)
    sx1,sy1 = getScreenPosition(system,408,1500)
    ex1,ey1 = getScreenPosition(system,3130,1500)
    snooze(0.5)
    mouseDrag(c, sx1, sy1, ex1, ey1, 0, Button.Button1)
    snooze(2)

    mouseClick(waitForObject(":PyDev Console"), 436, 255, 0, Button.Button1)
    
    for x in range(0, 24):
        type(waitForObject(":PyDev Console"), "<Return>")
        snooze(3)

    #open plot view result    
    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Show Plot View"))
    activateItem(waitForObjectItem(":Show Plot View_Menu", "Plot 2 *"))
    system = getPlottingSystem("Plot 2")
    test.verify(system.getTraces().iterator().next().getData().getRank()==1, "Data plotted: Success")
    
    #open result file
    mouseClick(waitForObjectItem(":PyDev Package Explorer_Tree", "data"), 11, 11, 0, Button.Button1)
    type(waitForObject(":PyDev Package Explorer_Tree"), "<F5>")
    children = object.children(waitForObjectItem(":PyDev Package Explorer_Tree", "i12"))
    
    for child in children:
        if "36153__TESTING__2014-04-23__calib__CeO2.txt" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            continue

    test.passes("Result file successfully created")

    closeOrDetachFromDAWN()
