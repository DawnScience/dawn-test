#Importing all the swt_* scripts makes their methods available to tests which
#import dawn_global_ui_controls
source(findFile("scripts", "swt_ctabitems.py"))
source(findFile("scripts", "swt_sashitems.py"))
source(findFile("scripts", "swt_tableitems.py"))
source(findFile("scripts", "swt_toolitems.py"))
source(findFile("scripts", "swt_treeitems.py"))
source(findFile("scripts", "swt_widgets.py"))

import sys

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

#These open closely related menus
# - first is for the initial plotting system's menu
# - second is for menu within tools
def waitForImageToolsMenu():
    return waitForFirstSwtToolItem(item_tooltiptext="Image tools used to profile and inspect images.")
def waitForXYPlottingToolsMenu(cTabItemTooltipText=None, cTabItemText=None):
    return getToolItemOfCTabFolder(cTabItemTooltipText=cTabItemTooltipText, cTabItemText=cTabItemText, toolItemTooltipText="XY plotting tools")

def getToolItemOfCTabFolder(cTabItemTooltipText=None, cTabItemText=None, toolItemTooltipText=None, toolItemText=None, squishFiveOne=False):
    
    if (toolItemText is None and toolItemTooltipText is None) or (cTabItemText is None and cTabItemTooltipText is None):
        raise LookupError("ERROR: Must specify the toolItemText/TooltipText to find and the activeTool associated with it.")
    
    # What is 'object' this does not seem to work...
    try:
        #Find the CTabFolder we're interested in and get the items in it
        cTab          = waitForSwtCTabItem(caption=cTabItemText, toolTip=cTabItemTooltipText, squishFiveOne=squishFiveOne)
        
        components = None
        
        # e4 target
        if (isEclipse4()):  
            cTabFolderObj = cTab.item.getParent()
            components = cTabFolderObj.topright.getChildren();

        # e3 target
        else:
            # Works on windows compared to previous e3 code which does not
            cTabFolderObj = cTab.item.getParent()
            components    = cTabFolderObj.getChildren()
            
        #Find all toolbars which are visible within this CTabFolder
        for i in range(components.length):
            c = components.at(i)
            if (c["class"] == "org.eclipse.swt.widgets.ToolBar") and (c["visible"] == 1):
                tbc = object.children(c)
            
                #Find the first toolItem object in the given toolbar, which matches given tool
                for toolItem in tbc:
                    if (toolItem["tooltiptext"] == toolItemTooltipText) | (toolItem["tooltiptext"] == toolItemText):
                        return toolItem
                
     
    except:
        # We do this to try and preserve the original lookup error.
        ae = sys.exc_value
        if (not cTabItemText is None):
            raise Exception(ae.args[0], "Cannot find cTabItemText="+cTabItemText)
        if (not cTabItemTooltipText is None):
            raise Exception(ae.args[0], "Cannot find cTabItemTooltipText="+cTabItemTooltipText)
        raise
    
    raise LookupError('ERROR: Could not find ToolItem with text "' + str(toolItemText) + '" and tooltiptext "' + str(toolItemTooltipText) + '"')

def isEclipse4():
    return 'ECLIPSE_TARGET_VERSION' in globals() and ECLIPSE_TARGET_VERSION==4

def isEclipse3():
    return 'ECLIPSE_TARGET_VERSION' not in globals() or ECLIPSE_TARGET_VERSION==3