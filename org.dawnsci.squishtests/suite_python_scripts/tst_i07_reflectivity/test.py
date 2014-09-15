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

    setupEPDPython()

    #create a pydev project 
    mouseClick(waitForObject(":Project Explorer_Tree"), 118, 187, 0, Button.Button3)
    activateItem(waitForObjectItem(":_Menu_4", "New"))
    activateItem(waitForObjectItem(":New_Menu_3", "Project..."))
    type(waitForObject(":_Text"), "pydev")
    mouseClick(waitForObjectItem(":_Tree", "PyDev Project"), 69, 7, 0, Button.Button1)
    clickButton(waitForObject(":Next >_Button"))
    type(waitForObject(":Project name:_Text"), "reflectivity")
    clickButton(waitForObject(":Next >_Button_2"))
    clickButton(waitForObject(":Finish_Button_2"))
    snooze(1)
    clickButton(waitForObject(":Open Associated Perspective?.No_Button"))
    mouseClick(waitForObjectItem(":Project Explorer_Tree", "reflectivity"), 21, 5, 0, Button.Button3)
    activateItem(waitForObjectItem(":_Menu_4", "New"))
    activateItem(waitForObjectItem(":New_Menu_3", "Source Folder"))
    type(waitForObject(":Name_Text"), "src")
    clickButton(waitForObject(":Finish_Button_2"))
    expand(waitForObjectItem(":Project Explorer_Tree", "reflectivity"))
    mouseClick(waitForObjectItem(":Project Explorer_Tree", "src"), 3, 11, 0, Button.Button3)
    activateItem(waitForObjectItem(":_Menu_4", "New"))
    activateItem(waitForObjectItem(":New_Menu_3", "PyDev Package"))
    doubleClick(waitForObject(":Source Folder_Text"), 80, 14, 0, Button.Button1)
    type(waitForObject(":Source Folder_Text"), "/reflectivity/src")
    doubleClick(waitForObject(":Name_Text"), 6, 13, 0, Button.Button1)
    type(waitForObject(":Name_Text"), "reflectivity")
    clickButton(waitForObject(":Finish_Button_2"))
    
    #create i07 folder in reflectivity python project
    addExternalFile("ErrorProp.py", "suite_python_scripts", "tst_i07_reflectivity", "reflectivity", "src/reflectivity")
    addExternalFile("nsplice.py", "suite_python_scripts", "tst_i07_reflectivity", "reflectivity", "src/reflectivity")
    addExternalFile("re-reflect.py", "suite_python_scripts", "tst_i07_reflectivity", "reflectivity", "src/reflectivity")
    addExternalFile("reflectivity.py", "suite_python_scripts", "tst_i07_reflectivity", "reflectivity", "src/reflectivity")

    #Open Python perspective
    openPerspective("Python") 
    snooze(1)
    #open console
    mouseClick(waitForObject(":Open Console_ToolItem"), 33, 11, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "5 PyDev Console"))
    clickButton(waitForObject(":Python console_Button"))
    clickButton(waitForObject(":OK_Button"))
    snooze(6)
    #expand data tree and open script
    mouseClick(waitForObjectItem(":PyDev Package Explorer_Tree", "reflectivity"), 24, 4, 0, Button.Button1)
    type(waitForObject(":PyDev Package Explorer_Tree"), "<F5>")
    expand(waitForObjectItem(":PyDev Package Explorer_Tree", "reflectivity"))
    expand(waitForObjectItem(":PyDev Package Explorer_Tree", "src"))
    expand(waitForObjectItem(":PyDev Package Explorer_Tree", "reflectivity_1"))

    children = object.children(waitForObjectItem(":PyDev Package Explorer_Tree", "reflectivity_1"))

    for child in children:
        if "re-reflect.py" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            continue
    snooze(1)
    clickTab(waitForObject(":re-reflect_CTabItem"), 40, 14, 0, Button.Button1)
    snooze(1)
    mouseClick(waitForObject(":Activates the interactive console. (Ctrl+Alt+Enter)_ToolItem"), 12, 8, 0, Button.Button1)
    snooze(1)
    
    #run the script the first time to send data to plot 1
    typeInConsole("rerefl(range(184476, 184477))")
    snooze(0.5)
    #test if first image is plotted
    system = getPlottingSystem("Plot 1")
    test.verify(system.getTraces().iterator().next().getData().getRank()==2, "Data plotted: Success")
    
    #create a rectangular roi and type getrois
    clickTab(waitForObject(":Plot 1_CTabItem"), 31, 11, 0, Button.Button1)
    typeInConsole("import scisoftpy.roi as droi")
    typeInConsole("roi = dnp.roi.rectangle()")
    typeInConsole("roi.name='roi'")
    typeInConsole("roi.setPoint([100,50])")
    typeInConsole("roi.setLengths([250, 100])")
    typeInConsole("bean=dnp.plot.getbean('Plot 1')")
    typeInConsole("list = droi.rectangle_list()")
    typeInConsole("list.append(roi)")
    typeInConsole("dnp.plot.setrois(bean, list)")
    typeInConsole("dnp.plot.setbean(bean)")
    snooze(1)
    typeInConsole("getrois()")
    snooze(1)
     #run the script the second time
    typeInConsole("rerefl(range(184476, 184477))")
    snooze(1)   
     
    #open and check results
    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Show Plot View"))
    activateItem(waitForObjectItem(":Show Plot View_Menu", "Plot 2 *"))
    system = getPlottingSystem("Plot 2")
    test.verify(system.getTraces().iterator().next().getData().getRank()==1, "Data plotted: Success")

    mouseClick(waitForObjectItem(":PyDev Package Explorer_Tree", "reflectivity"), 11, 11, 0, Button.Button1)
    type(waitForObject(":PyDev Package Explorer_Tree"), "<F5>")
    children = object.children(waitForObjectItem(":PyDev Package Explorer_Tree", "reflectivity"))
    
    for child in children:
        if "184476_rerefl_bkg1.dat" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            continue
    mouseClick(waitForObjectItem(":Data_Table", "0/0"), 7, 15, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table", "1/0"), 10, 11, 0, Button.Button1)
    #test result is plotted
    system = getPlottingSystem("184476_rerefl_bkg1.dat")
    test.verify(system.getTraces().iterator().next().getData().getRank()==1, "Data plotted: Success")
    test.passes("Result file successfully created")

    closeOrDetachFromDAWN()