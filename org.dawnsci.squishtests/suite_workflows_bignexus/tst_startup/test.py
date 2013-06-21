source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "use_case_utils.py"))

import os

def runTestBrowserDE():
    
    startDAWNSuiteWorkspace()
    #startOrAttachToDAWNOnly(clean_workspace=False)
    # Open data browsing perspective 
    openPerspective("DExplore")
    #Open data browsing perspective 
    
    expand(waitForObjectItem(":Project Explorer_Tree", "Workflow"))
    expand(waitForObjectItem(":Project Explorer_Tree", "output"))
    expand(waitForObjectItem(":Project Explorer_Tree", "BigData"))
    
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "BigData"))
    
    
    for child in children:
        if "Export.h5" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            break
    
    expand(waitForObjectItem(":Tree_Tree", "entry"))
    expand(waitForObjectItem(":Tree_Tree", "data"))
    doubleClick(waitForObjectItem(":Tree_Tree", "image"), 29, 11, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Tree_Tree", "image"), 13, 12, 0, Button.Button1)
    mouseClick(waitForObject(":_Twistie"), 10, 4, 0, Button.Button1)
    snooze(5)
    setValue(waitForObject(":_Slider_2"), 45)

    closeOrDetachFromDAWN()
    

def runTestBrowser():

    
    startOrAttachToDAWNOnly(clean_workspace=False)
    # Open data browsing perspective 
    openPerspective("Data Browsing (default)")
    
    expand(waitForObjectItem(":Project Explorer_Tree", "Workflow"))
    expand(waitForObjectItem(":Project Explorer_Tree", "output"))
    expand(waitForObjectItem(":Project Explorer_Tree", "BigData"))
    
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "BigData"))
    
    
    for child in children:
        if "Export.h5" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            break
    
    
    mouseClick(waitForObjectItem(":Data_Table", "0/0"), 8, 5, 0, Button.Button1)
    snooze(5)
    mouseClick(waitForObject(":Edit the slice with different editors._ToolItem"), 29, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Slice index (only)"))
    mouseClick(waitForObjectItem(":Data_Table_2", "0/2"), 89, 18, 0, Button.Button1)
    snooze(1)
    for i in range(0,100,10):
        setValue(waitForObject(":Data_Spinner"), i)
        snooze(0.01)

    mouseClick(waitForObject(":Slice as line plots_ToolItem"), 13, 10, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table_2", "1/2"), 91, 23, 0, Button.Button1)
    snooze(1)
    for i in range(0,2000,100):
        setValue(waitForObject(":Data_Spinner"), i)
        snooze(0.01)


        
    mouseClick(waitForObject(":Slice as image_ToolItem"), 10, 13, 0, Button.Button1)
    mouseClick(waitForObject(":Keep aspect ratio_ToolItem"), 7, 6, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table_2", "1/2"), 84, 16, 0, Button.Button1)
    snooze(1)

    for i in range(0,2000,100):
        setValue(waitForObject(":Data_Spinner"), i)
        snooze(0.01)
    
    mouseClick(waitForObject(":Export.h5_CTabCloseBox"))
    closeOrDetachFromDAWN()

def main():
    
    #Start using clean workspace
    startDAWNSuiteWorkspace()
    name = "bigData.moml"
    path = findFile("testdata", name)
    path = os.path.abspath(path)
    
    # Open data browsing perspective 
    openPerspective("Data Browsing (default)")
    
    
    activateItem(waitForObjectItem(":_Menu", "File"))
    activateItem(waitForObjectItem(":File_Menu", "New"))
    activateItem(waitForObjectItem(":New_Menu", "Project..."))
    type(waitForObject(":New Project_Text"), "work")
    mouseClick(waitForObjectItem(":New Project_Tree", "Workflow Project"), -1, 6, 0, Button.Button1)
    clickButton(waitForObject(":New Project.Next >_Button"))
    mouseClick(waitForObject(":Project name:_Text"), 198, 7, 0, Button.Button1)
    type(waitForObject(":Project name:_Text"), "Workflow")

    clickButton(waitForObject(":Create example data_Button"))
    clickButton(waitForObject(":Finish_Button"))


    mouseClick(waitForObjectItem(":Project Explorer_Tree", "Workflow"), 49, 12, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Project Explorer_Tree", "Workflow"), 49, 12, 0, Button.Button3)
    activateItem(waitForObjectItem(":_Menu_2", "Import..."))
    type(waitForObject(":Import_Text"), "file")
    mouseClick(waitForObjectItem(":Import_Tree", "File System"), 11, 11, 0, Button.Button1)
    clickButton(waitForObject(":Import.Next >_Button"))
    type(waitForObject(":Import.From directory:_Combo"), os.path.split(path)[0])
    
    type(waitForObject(":Import.From directory:_Combo"), "<Return>")
    clickButton(waitForObject(":Import.Browse..._Button"))
    chooseDirectory(waitForObject(":SWT"), "C:\\SquishTestWorkspaces\\sda\\squishtests\\suite_big_nexus\\shared\\testdata")
    mouseClick(waitForObject(":bigData.moml_ItemCheckbox"), 6, 12, 0, Button.Button1)
    clickButton(waitForObject(":Import.Finish_Button"))
    expand(waitForObjectItem(":Project Explorer_Tree", "Workflow"))
    
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "Workflow"))
    
    for child in children:
        if "bigData.moml" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            continue
    
    snooze(10)
    
    clickButton(waitForObject(":Open Workflow Perspective.Yes_Button"))
    clickButton(waitForObject(":Run.Start_Button"))
    expand(waitForObjectItem(":Project Explorer_Tree_2", "output",120000))
    snooze(100)
    clickTab(waitForObject(":bigData.moml_CTabItem"))
    mouseClick(waitForObject(":bigData.moml_CTabCloseBox"), 8, 9, 0, Button.Button1)
    openPerspective("Data Browsing (default)")

    closeOrDetachFromDAWN()
#    
#    snooze(10)
#    
#    runTestBrowser()
#    
#    snooze(10)
#    
#    runTestBrowserDE()