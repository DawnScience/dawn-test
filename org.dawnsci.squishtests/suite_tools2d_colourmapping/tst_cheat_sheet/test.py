source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_slider_utils.py"))


def main():
    startOrAttachToDAWN(vmArgs="-Dorg.dawnsci.histogram.v1.x.colourMapping=true")
    
    snooze(5.0)
    
    openAndClearErrorLog()
    
        
    activateItem(waitForObjectItem(":_Menu", "Help"))
    activateItem(waitForObjectItem(":Help_Menu", "Cheat Sheets..."))
    expand(waitForObjectItem(":Cheat Sheet Selection_Tree", "Plotting tools"))
    mouseClick(waitForObjectItem(":Cheat Sheet Selection_Tree", "Colour Mapping Example"))
    clickButton(waitForObject(":Cheat Sheet Selection.OK_Button"))

    verifyAndClearErrorLog()

    snooze(1.0)
    closeOrDetachFromDAWN()
    