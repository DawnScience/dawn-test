source(findFile("scripts", "dawn_constants.py"))

import os
import shutil


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

# All these arguments = bad but not sure how to do his as not python expert.
def openExample(frag, project="data", folder="examples", subfolder=None, subsubfolder=None):
    
    expand(waitForObjectItem(":Project Explorer_Tree", project))
    expand(waitForObjectItem(":Project Explorer_Tree", folder))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", folder))
    
    if (subfolder is not None):
        expand(waitForObjectItem(":Project Explorer_Tree", subfolder))
        children = object.children(waitForObjectItem(":Project Explorer_Tree", subfolder))
        
    if (subsubfolder is not None):
        expand(waitForObjectItem(":Project Explorer_Tree", subsubfolder))
        children = object.children(waitForObjectItem(":Project Explorer_Tree", subsubfolder))
    
    for child in children:
        if frag in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            
'''
Checks if file can be selected from example data.
Tries to select each directory as the locations are processed.
'''            
def checkExample(frag, project="data", folder="examples", subfolder=None, subsubfolder=None):
    
    expand(waitForObjectItem(":Project Explorer_Tree", project))
    
    children = select(folder) 
    
    if (subfolder is not None):
        children = select(subfolder) 
        
    if (subsubfolder is not None):
        children = select(subsubfolder) 
    
    for child in children:
        if frag in child.text:
            return True
        
    return False

def select(name):
    selection = waitForObjectItem(":Project Explorer_Tree", name)
    expand(selection)
    mouseClick(selection, 5, 5, 0, Button.Button1)
    return object.children(waitForObjectItem(":Project Explorer_Tree", name))

def openExternalFile(name):
    
    path = findFile("testdata", name)
    path = os.path.abspath(path)
    activateItem(waitForObjectItem(":_Menu", "File"))
    activateItem(waitForObjectItem(":File_Menu", "Open File..."))
    chooseFile(waitForObject(":SWT"), path)

''' 
Adds an external file to the project.
'''
def addExternalFile(fileName, suiteName, testName, project, subdir):
    
    path = findFile("testdata", fileName)
    path = os.path.abspath(path)
    
    # Path to workspace is something like:
    # /scratch/workspace/suite_conversion/tst_image_stack_tiffs/workspace/data
    # or
    # C:\scratch\workspace\suite_conversion\tst_image_stack_tiffs\workspace\data
    shutil.copyfile(path, "/scratch/workspace/"+suiteName+"/"+testName+"/workspace/"+project+"/"+subdir+"/"+fileName)
    mouseClick(waitForObjectItem(":Project Explorer_Tree", project))
    type(waitForObject(":Project Explorer_Tree"), "<F5>")


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
        return factory.getPlottingSystem(name)
        
    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Show View"))
    activateItem(waitForObjectItem(":Show View_Menu", "Other..."))
    type(waitForObject(":Show View_Text"), "Plotting Systems")
    mouseClick(waitForObjectItem(":Show View_Tree", "Plotting Systems"))
    clickButton(waitForObject(":Show View.OK_Button"))
    waitForObject(":Plotting Systems_CTabItem")
    plotButton = waitForObject(":Plotting Systems.Refresh_RefreshButton")
    
    factoryClass = plotButton.getClass().getClassLoader().loadClass("org.dawnsci.plotting.api.PlottingFactory")

    factory = factoryClass.newInstance()
    system  = factory.getPlottingSystem(name)
    
    # Close gallery
    snooze(1)
    try:
        clickTab(waitForObject(":Plotting Systems_CTabItem"), 18, 11, 0, Button.Button1)
        mouseClick(waitForObject(":Plotting Systems_CTabCloseBox", 1000))
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
    
