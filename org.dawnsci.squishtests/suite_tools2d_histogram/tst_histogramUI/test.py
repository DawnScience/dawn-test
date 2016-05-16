source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_constants.py"))


def main():
    vals = dawn_constants
    startOrAttachToDAWN()
    
    snooze(5.0)
    
    openAndClearErrorLog()
    
    # Open our test image..
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    for child in children:
        if "pilatus300k.edf" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            break
        
    snooze(1.0)

    # Open and activate the histogram tool for the image
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    histogram = waitForObjectItem(":Pop Up Menu", "Histogram")
    
    activateItem(histogram)
    
    # If histogram has activated correctly the colour scheme combo should be available
    combo = waitForObject(":Histogram_Combo", 40000)
    items = combo.getItems()
    for i in range(items.length):
        mouseClick(waitForObjectItem(":Histogram_Combo", items.at(i)), 0, 0, 0, Button.NoButton)

    snooze(1.0)
    
    # Toggle the log button
    clickButton(waitForObject(":Histogram.Log Scale_Button"))
    clickButton(waitForObject(":Histogram.Log Scale_Button"))
    
    
    # Enter some values in the min/max spinners
    type(waitForObject(":Histogram_SpinnerMin"), "-5.5")
    type(waitForObject(":Histogram_SpinnerMin"), "<Return>")
    
    type(waitForObject(":Histogram_SpinnerMax"), "17000")
    type(waitForObject(":Histogram_SpinnerMax"), "<Return>")
    
    # Close the histogram
    clickTab(waitForObject(":Histogram_CTabItem"), 10, 9, 0, Button.Button3)
    activateItem(waitForObjectItem(":Pop Up Menu", "Close"))
    
    snooze(1.0)
    
    closeOrDetachFromDAWN()


    

