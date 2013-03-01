source(findFile("scripts", "dawn_global_startup.py"))

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
    for i in range(items.length):
        mouseClick(waitForObject(":Colour mapping_CCombo"), 8, 7, 0, Button.Button1)
        mouseClick(waitForObjectItem(":_List", items.at(i)), 13, 10, 0, Button.Button1)
    
    snooze(1.0)
    closeOrDetachFromDAWN()

    

