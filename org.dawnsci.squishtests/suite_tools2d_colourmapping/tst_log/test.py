source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_constants.py"))

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
    
    snooze(2)
    type(waitForObject(":_FigureCanvas"), "h")
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Colour mapping"))    
        
    snooze(1.0)
    mouseClick(waitForObject(":Configure Settings..._ToolItem"))
    clickTab(waitForObject(":Configure Graph Settings.Image Traces_TabItem"))
    mouseClick(waitForObject(":Histogramming.Histogram Type_CCombo"))
    mouseClick(waitForObjectItem(":_List", "Median"))
    clickButton(waitForObject(":Configure Graph Settings.Apply_Button"))
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    type(waitForObject(":_FigureCanvas"), "h")
        
    snooze(1.0)
    mouseClick(waitForObject(":Configure Settings..._ToolItem"))
    clickTab(waitForObject(":Configure Graph Settings.Image Traces_TabItem"))
    mouseClick(waitForObject(":Histogramming.Histogram Type_CCombo"))
    mouseClick(waitForObjectItem(":_List", "Outlier Values"))
    clickButton(waitForObject(":Configure Graph Settings.Apply_Button"))
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    type(waitForObject(":_FigureCanvas"), "h")
       
    closeOrDetachFromDAWN()