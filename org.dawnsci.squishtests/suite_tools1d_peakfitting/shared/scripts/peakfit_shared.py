def createPeakFitSpace(steps=15):
    #To stop problem of not all menu items in drop-down being visible initially
    clickTab(waitForObject(":Value_CTabItem"), 29, 14, 0, Button.Button1)
    clickTab(waitForObject(":Value_CTabItem"), 29, 14, 0, Button.Button3)
    activateItem(waitForObjectItem(":Pop Up Menu", "Size"))
    activateItem(waitForObjectItem(":Size_Menu", "Top"))
    while steps >= 0:
        type(waitForObject(":_Sash_3"), "<Up>")
        steps -= 1
    clickTab(waitForObject(":Value_CTabItem"), 48, 22, 0, Button.Button1)
