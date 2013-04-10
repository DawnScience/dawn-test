source(findFile("scripts", "dawn_constants.py"))

import os


def createProject(projectName, projectType="Workflow Project"):
    
    activateItem(waitForObjectItem(":_Menu", "File"))
    activateItem(waitForObjectItem(":File_Menu", "New"))
    activateItem(waitForObjectItem(":New_Menu_2", "Project..."))
    type(waitForObject(":_Text"), projectType)
    mouseClick(waitForObjectItem(":_Tree", projectType), 59, 10, 0, Button.Button1)
    clickButton(waitForObject(":Next >_Button"))
    mouseClick(waitForObject(":Project name:_Text"), 48, 3, 0, Button.Button1)
    type(waitForObject(":Project name:_Text"), projectName)
    clickButton(waitForObject(":Finish_Button_2"))
    snooze(1)


def openExample(frag, project="data", folder="examples"):
    
    expand(waitForObjectItem(":Project Explorer_Tree", project))
    expand(waitForObjectItem(":Project Explorer_Tree", folder))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", folder))
    for child in children:
        if frag in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)


def openExternalFile(name):
    
    path = findFile("testdata", name)
    path = os.path.abspath(path)
    activateItem(waitForObjectItem(":_Menu", "File"))
    activateItem(waitForObjectItem(":File_Menu", "Open File..."))
    chooseFile(waitForObject(":SWT"), path)


def chooseSlice():
    vals = dawn_constants
    mouseClick(waitForObjectItem(":Data_Table_2", "1/0"), 8, 12, 0, Button.Button1)
    mouseClick(waitForObject(":Slice as line plots_ToolItem"), 12, 14, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table_3", "0/2"), 13, 24, 0, Button.Button1)
    mouseDrag(waitForObject(":Data_Scale"), 18, 22, 20, 0, Modifier.None, Button.Button1)
    mouseClick(waitForObject(":XY plotting tools_ToolItem_2"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)

factory = None

def getPlottingSystem(name):
    
    global factory    
    if factory is not None:
        system  = factory.getPlottingSystem(name)
        return system
    
    gallery = None
    try:
        mouseClick(waitForObjectItem(":Show View_Tree", "Image Gallery"), 79, 7, 0, Button.Button1)
        gallery = waitForObject(":Image Gallery_Gallery", 1000)

    except:
        # Open a widget with the same class loader as the plotting factory
        mouseClick(waitForObject(":_Sash"), 1, 8, 0, Button.Button1)
        activateItem(waitForObjectItem(":_Menu", "Window"))
        activateItem(waitForObjectItem(":Window_Menu", "Show View"))
        activateItem(waitForObjectItem(":Show View_Menu", "Other..."))
        type(waitForObject(":Show View_Text"), "Gallery")
        mouseClick(waitForObjectItem(":Show View_Tree", "Image Gallery"))
        clickButton(waitForObject(":Show View.OK_Button"))
        gallery = waitForObject(":Image Gallery_Gallery")
   
    factoryClass = gallery.getClass().getClassLoader().loadClass("org.dawb.common.ui.plot.PlottingFactory")
    factory = factoryClass.newInstance()
    system  = factory.getPlottingSystem(name)
    
    # Close gallery
    snooze(1)
    try:
        clickTab(waitForObject(":Image Gallery_CTabItem"), 18, 11, 0, Button.Button1)
        mouseClick(waitForObject(":Image Gallery_CTabCloseBox", 1000))
    except:

        print "Could not close gallery"
        
    snooze(1)

    return system

def getScreenPosition(plottingSystem,x,y):
    outX = None
    outY = None
    
    axes = plottingSystem.getAxes()
    
    if axes.get(0).isYAxis():
        outY = axes.get(0).getValuePosition(y)
        outX = axes.get(1).getValuePosition(x)
    elif axes.get(1).isYAxis():
        outY = axes.get(1).getValuePosition(y)
        outX = axes.get(0).getValuePosition(x)
        
    return outX,outY

def dragSash(sash, dx, dy):
    screenPoint = sash.toDisplay(sash.getBounds().width/2,sash.getBounds().height/2)
    startDrag(sash, sash.getBounds().width/2, sash.getBounds().height/2);
#    mousePress(waitForObject(":_Sash"), 5, 316, Button.Button1);
    mouseMove(screenPoint.x - dx, screenPoint.y -dy)
    snooze(1)
    dropOn(sash, sash.getBounds().width/2, sash.getBounds().height/2,DnD.DropDefault);

def dragToolToConstWidth(toolTab,sash):
    current_width = toolTab.getControl().getBounds().width
    
    if (current_width < dawn_constants.TOOL_MIN_WIDTH):
        dx = dawn_constants.TOOL_MIN_WIDTH - current_width
        dragSash(sash, dx, 0)
    
