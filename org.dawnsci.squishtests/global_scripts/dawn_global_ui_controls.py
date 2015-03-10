#Importing all the swt_* scripts makes their methods available to tests which
#import dawn_global_ui_controls
source(findFile("scripts", "swt_ctabitems.py"))
source(findFile("scripts", "swt_sashitems.py"))
source(findFile("scripts", "swt_tableitems.py"))
source(findFile("scripts", "swt_toolitems.py"))
source(findFile("scripts", "swt_treeitems.py"))

def createToolSpace(viewTabName=None, direction=None, steps=15):
    if viewTabName is None:
        raise LookupError("ERROR: Must specify a viewTabName to right click on!")
    if direction is None:
        raise LookupError("ERROR: Must specify a direction to drag the ")
    
    #To make test case insensitive
    direction = direction.lower()
    if direction == "up":
        sashDirection = "Top"
        arrowKey = "<Up>"
    elif direction == "down":
        sashDirection = "Bottom"
        arrowKey = "<Down>"
    elif direction == "left":
        sashDirection = "Left"
        arrowKey = "<Left>"
    elif direction == "right":
        sashDirection = "Right"
        arrowKey = "<Right>"
    else:
    	raise LookupError("ERROR: Unrecognised direction to move sash (must be one of up, down, left or right (case insensitive).")
    
    viewTabObject = waitForFirstSwtCTabItem(item_text=viewTabName)
    clickTab(waitForObject(viewTabObject), 49, 4, 0, Button.Button3)
    activateItem(waitForObjectItem(":Pop Up Menu", "Size"))
    activateItem(waitForObjectItem(":Size_Menu", sashDirection))
    
    #Record a reference to the sash object to use in dragging loop
    activeSash = waitForFirstSwtSashItem()
    
    #For compactness, put dragging sash into loop
    a = 0
    while a < steps:
        type(waitForObject(activeSash), arrowKey)
        a += 1
    clickTab(waitForObject(viewTabObject), 27, 12, 0, Button.Button1)