source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))

def main():

    startOrAttachToDAWN()

    openPerspective("Data Browsing (default)")

    openExample("pow_M99S5_1_0001.cbf")
    
    snooze(1)
    
    mouseClick(waitForObject(":Configure Settings..._ToolItem_3"))
    clickTab(waitForObject(":Configure Graph Settings.Image Traces_TabItem"))
    mouseClick(waitForObject(":Histogramming.Histogram Type_CCombo"))
    mouseClick(waitForObjectItem(":_List", "Median"))
    mouseClick(waitForObject(":Histogramming.Histogram Type_CCombo"))
    mouseClick(waitForObjectItem(":_List", "Outlier Values"))

    low = waitForObject(":Histogramming_StyledText")
    high = waitForObject(":Histogramming_StyledText_2")
    
    mouseClick(waitForObject(":Histogramming_StyledText"), 5, 8, 0, Button.Button1)
    type(low, "1")
    type(low, "<Ctrl+a>")
    type(low, "<Delete>")
    type(low, "10")
    mouseClick(high, 21, 8, 0, Button.Button1)
    test.verify(low.getForeground().getRed()== 0, "Text is black")

    type(high, "<Ctrl+a>")
    type(high, "<Delete>")
    type(high, "90")
    mouseClick(low, 21, 8, 0, Button.Button1)
    test.verify(high.getForeground().getRed()== 0, "Text is black")
    
    mouseClick(waitForObject(":Histogramming_StyledText"), 5, 8, 0, Button.Button1)
    type(low, "1")
    type(low, "<Ctrl+a>")
    type(low, "<Delete>")
    type(low, "100")
    mouseClick(high, 21, 8, 0, Button.Button1)
    test.verify(low.getForeground().getRed()== 255, "Text is Red")
    test.verify(high.getForeground().getRed()== 255, "Text is Red")
    
    mouseClick(waitForObject(":Histogramming_StyledText"), 5, 8, 0, Button.Button1)
    type(low, "1")
    type(low, "<Ctrl+a>")
    type(low, "<Delete>")
    type(low, "10")
    mouseClick(high, 21, 8, 0, Button.Button1)
    test.verify(low.getForeground().getRed()== 0, "Text is black")
    test.verify(high.getForeground().getRed()== 0, "Text is black")
    
    
    type(waitForObject(":Histogramming_StyledText"), "<Ctrl+a>")
    type(waitForObject(":Histogramming_StyledText"), "10")
    type(waitForObject(":Histogramming_StyledText"), "<Right>")
    type(waitForObject(":Histogramming_StyledText"), "567")
    type(waitForObject(":Histogramming_StyledText"), "<Left>")
    type(waitForObject(":Histogramming_StyledText"), "<Left>")
    type(waitForObject(":Histogramming_StyledText"), "<Left>")
    type(waitForObject(":Histogramming_StyledText"), "78")
    type(waitForObject(":Histogramming_StyledText"), "<Delete>")
    type(waitForObject(":Histogramming_StyledText"), "9")

    #Removing until 
    #test.verify(low.getText() in "10.789 %","Text is correct")
    
    
    clickButton(waitForObject(":Configure Graph Settings.Apply_Button"))
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))

    closeOrDetachFromDAWN()
