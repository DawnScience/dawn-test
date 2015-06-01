source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_constants.py"))

def main():
    vals = dawn_constants
    startOrAttachToDAWN(vmArgs="-Dorg.dawnsci.histogram.v1.x.colourMapping=true")
    
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
       
    combo = waitForObject(":Colour mapping_CCombo")
    items = combo.getItems()
    
    mouseClick(waitForObject(":Colour mapping_CCombo"), 8, 7, 0, Button.Button1)
    mouseClick(waitForObjectItem(":_List", items.at(0)), 13, 10, 0, Button.Button1)
    snooze(0.2)
        
    mouseClick(waitForObject(":Colour mapping_Twistie"))    
    
    red_combo = waitForObject(":Colour mapping.Red_CCombo")
    items = red_combo.getItems()
    for i in range(0,items.length-2,3):
        mouseClick(waitForObject(":Colour mapping.Red_CCombo"))
        mouseClick(waitForObjectItem(":_List", items.at(i)))
        mouseClick(waitForObject(":Colour mapping.Green_CCombo"))
        mouseClick(waitForObjectItem(":_List", items.at(i+1)))
        mouseClick(waitForObject(":Colour mapping.Blue_CCombo"))
        mouseClick(waitForObjectItem(":_List", items.at(i+2)))
    
        snooze(0.05)
        clickButton(waitForObject(":Colour mapping.Inverse_Button"))
        clickButton(waitForObject(":Colour mapping.Inverse_Button_2"))
        clickButton(waitForObject(":Colour mapping.Inverse_Button_3"))
        snooze(0.05)
        clickButton(waitForObject(":Colour mapping.Inverse_Button"))
        clickButton(waitForObject(":Colour mapping.Inverse_Button_2"))
        clickButton(waitForObject(":Colour mapping.Inverse_Button_3"))
             
    snooze(1.0)
    closeOrDetachFromDAWN()

    

