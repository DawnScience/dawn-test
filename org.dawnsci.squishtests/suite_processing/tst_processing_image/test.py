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
    
    openExample("315029.dat");
    
    clickButton(waitForObject(":Finish_Button"))
    
    input = getPlottingSystem("Input");
    output = getPlottingSystem("Slice");
    
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
    mouseClick(waitForObjectItem(":Processing_Table", "0/0"), 11, 12, 0, Button.Button1)
    type(waitForObject(":Processing_Text"), "downsample image")
    mouseClick(waitForObjectItem(":_Table", "0/0"), 60, 4, 0, Button.Button1)
    doubleClick(waitForObjectItem(":_Table", "0/0"), 61, 6, 0, Button.Button1)
    
    snooze(1)
    out = output.getTraces();
    #test.verify(not out.isEmpty(), "Output not empty")
    
    mouseClick(waitForObjectItem(":Processing_Table", "1/0"), 443, 12, 0, Button.Button1)
    type(waitForObject(":Processing_Text"), "image integration")
    mouseClick(waitForObjectItem(":_Table", "0/0"), 60, 4, 0, Button.Button1)
    doubleClick(waitForObjectItem(":_Table", "0/0"), 61, 6, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Processing_Table", "0/0"), 443, 12, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Model 'Downsample Image'_Table", "2/1"), 59, 13, 0, Button.Button1)
    type(waitForObject(":Model 'Downsample Image'_Text"), "4")
    mouseClick(waitForObjectItem(":Model 'Downsample Image'_Table", "3/1"), 57, 8, 0, Button.Button1)
    type(waitForObject(":Model 'Downsample Image'_Text"), "4")
    type(waitForObject(":Model 'Downsample Image'_Text"), "<Numpad Return>")
    mouseClick(waitForObjectItem(":Processing_Table", "0/0"), 324, 18, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Processing_Table", "1/0"), 326, 12, 0, Button.Button1)
    mouseClick(waitForObject(":Process all files_ToolItem"), 11, 21, 0, Button.Button1)

    clickButton(waitForObject(":Please select a directory.OK_Button"))
    
    snooze(5)
    
    mouseClick(waitForObjectItem(":Project Explorer_Tree", "examples"), 48, 9, 0, Button.Button3)
    activateItem(waitForObjectItem(":_Menu_2", "Refresh"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    testPass = False;
    
    for child in children:
        if "315029_processed" in child.text:
            testPass = True;

    test.verify(testPass, "file present")

    closeOrDetachFromDAWN()
