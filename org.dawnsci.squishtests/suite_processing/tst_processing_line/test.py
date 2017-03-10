source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_constants.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))
source(findFile("scripts", "use_case_utils.py"))

def main():
    
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Processing")
    
    openExample("pilatus300k.edf");
    
    clickButton(waitForObject(":Line [1D]_Button"))

    mouseClick(waitForObjectItem(":_Table_2", "0/1"), 40, 24, 0, Button.Button1)
    mouseClick(waitForObject(":_CLabel"), 572, 81, 0, Button.Button1)
    mouseClick(waitForObject(":_CCombo"), 57, 31, 0, Button.Button1)
    mouseClick(waitForObjectItem(":_List", "(Range)"), 51, 8, 0, Button.Button1)

    clickButton(waitForObject(":Finish_Button"))
    
    input = getPlottingSystem("Input");
    output = getPlottingSystem("Output");
    
    it = input.getTraces();
    out = output.getTraces();
    
    test.verify(not it.isEmpty(), "Input not empty")
    test.verify(out.isEmpty(), "Output is empty")
    
    clickButton(waitForObject(":Data Slice View_Button_4"))
    clickButton(waitForObject(":Data Slice View_Button_5"))
    clickButton(waitForObject(":Data Slice View_Button_6"))
    clickButton(waitForObject(":Data Slice View_Button_3"))
    clickButton(waitForObject(":Data Slice View_Button_2"))
    clickButton(waitForObject(":Data Slice View_Button"))
    
    mouseClick(waitForObjectItem(":Processing_Table", "0/0"), 14, 13, 0, Button.Button1)
    type(waitForObject(":Processing_Text"), "derivative")
    doubleClick(waitForObjectItem(":_Table", "0/0"), 75, 12, 0, Button.Button1)
    
    snooze(1)
    
    out = output.getTraces();
    test.verify(not out.isEmpty(), "Output not empty")
    
    mouseClick(waitForObjectItem(":Processing_Table", "1/0"), 107, 16, 0, Button.Button1)
    mouseClick(waitForObject(":Processing_Text"), 99, 15, 0, Button.Button1)
    type(waitForObject(":Processing_Text"), "standard normal variate")
    doubleClick(waitForObjectItem(":_Table", "0/0"), 96, 9, 0, Button.Button1)
    
    mouseClick(waitForObject(":Process all files_ToolItem"), 11, 21, 0, Button.Button1)

    clickButton(waitForObject(":Please select a directory.OK_Button"))
    
    snooze(5)
    
    mouseClick(waitForObjectItem(":Project Explorer_Tree", "examples"), 48, 9, 0, Button.Button3)
    activateItem(waitForObjectItem(":_Menu_2", "Refresh"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    testPass = False;
    
    for child in children:
        if "pilatus300k_processed" in child.text:
            testPass = True;

    test.verify(testPass, "file present")

    closeOrDetachFromDAWN()
