source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_slider_utils.py"))
source(findFile("scripts", "dawn_constants.py"))

def open_and_close_tool():
    vals = dawn_constants
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Colour mapping"))    

    clickTab(waitForObject(":Colour mapping_CTabItem"), 10, 9, 0, Button.Button3)
    activateItem(waitForObjectItem(":Pop Up Menu", "Close"))
    
    snooze(1.0)
    
    #verifyAndClearErrorLog()

def main():
    startOrAttachToDAWN()

    
    snooze(5.0)
    
    #openAndClearErrorLog()
    
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    for child in children:
        if "pilatus300k.edf" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            break

    for i in range(10):
        open_and_close_tool()


    snooze(1.0)
    closeOrDetachFromDAWN()

    