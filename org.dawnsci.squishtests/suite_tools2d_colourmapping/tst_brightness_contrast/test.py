source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_slider_utils.py"))

def main():
    startOrAttachToDAWN()
    
    snooze(5.0)
    
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    for child in children:
        if "pilatus300k.edf" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            break

    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 27, 16, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Colour mapping"))    
       
    combo = waitForObject(":Colour mapping_CCombo")
    items = combo.getItems()
    mouseClick(waitForObject(":Colour mapping_CCombo"), 8, 7, 0, Button.Button1)
    mouseClick(waitForObjectItem(":_List", items.at(1)), 13, 10, 0, Button.Button1)
    
    mouseClick(waitForObject(":Colour mapping_Twistie_2"), 5, 1, 0, Button.Button1)

    brightness_slider = waitForObject(":Colour mapping_Scale")    
    contrast_slider = waitForObject(":Colour mapping_Scale_2")
    
    for i in range(10):
        slide_to_propotion(brightness_slider, float(i)/10.0)
        snooze(0.1)
        slide_to_propotion(contrast_slider, float(i)/10.0)
        snooze(0.1)
        
    snooze(1.0)
    closeOrDetachFromDAWN()
    
    
    
    