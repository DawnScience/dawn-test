source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_constants.py"))

def testColormap():
    mouseClick(waitForObject(":Configure Settings..._ToolItem"), 20, 5, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Image Traces_TabItem"))
    
    low = waitForObject(":Histogramming_StyledText").text
    high = waitForObject(":Histogramming_StyledText_2").text
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    clickButton(waitForObject(":Colour mapping.Log Scale_Button"))
    checkHisto(low,high)
    clickButton(waitForObject(":Colour mapping.Log Scale_Button"))
    checkHisto(low,high)
    clickButton(waitForObject(":Colour mapping.Log Scale_Button"))
    checkHisto(low,high)
    clickButton(waitForObject(":Colour mapping.Log Scale_Button"))

def checkHisto(low,high):
    mouseClick(waitForObject(":Configure Settings..._ToolItem"), 20, 5, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Image Traces_TabItem"))
    
    actualLow = waitForObject(":Histogramming_StyledText").text
    actualHigh = waitForObject(":Histogramming_StyledText_2").text
    
    test.verify(low == actualLow, "Test: " + low + " equals actual value of:" + actualLow)
    test.verify(high == actualHigh, "Test: " + high + " equals actual value of:" + actualHigh)

    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    


def main():
    vals = dawn_constants
    startOrAttachToDAWN()
    
    snooze(5.0)
    
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    for child in children:
        if "pilatus300k.edf" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            break

    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Colour mapping"))    
    
    testColormap()
    
    snooze(1.0)
    mouseClick(waitForObject(":Configure Settings..._ToolItem"), 14, 10, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Image Traces_TabItem"))
    mouseClick(waitForObject(":Histogramming.Histogram Type_CCombo"), 299, 15, 0, Button.Button1)
    mouseClick(waitForObjectItem(":_List", "Median"), 202, 16, 0, Button.Button1)
    clickButton(waitForObject(":Configure Graph Settings.Apply_Button"))
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    type(waitForObject(":_FigureCanvas"), "h")
    
    testColormap()
    
    snooze(1.0)
    mouseClick(waitForObject(":Configure Settings..._ToolItem"), 14, 10, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Image Traces_TabItem"))
    mouseClick(waitForObject(":Histogramming.Histogram Type_CCombo"), 299, 15, 0, Button.Button1)
    mouseClick(waitForObjectItem(":_List", "Outlier Values"), 200, 7, 0, Button.Button1)
    clickButton(waitForObject(":Configure Graph Settings.Apply_Button"))
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    type(waitForObject(":_FigureCanvas"), "h")
    
    testColormap()
    
    closeOrDetachFromDAWN()