source(findFile("scripts", "dawn_constants.py"))

import os
import shutil


def createProject(projectName, projectType="Workflow Project"):
    #Move this comment to confluence docs!
    '''This works fine for creating a new project, but the projectType needs to match
    the name in the menu *EXACTLY* 
    Also the following items are needed in the object.map:
    :Finish_Button_2    {caption='Finish' isvisible='true' type='org.eclipse.swt.widgets.Button' window=':_Shell'}
    :New_Menu_2    {caption='New' container=':_Menu' menuStyle='SWT.DROP_DOWN' type='org.eclipse.swt.widgets.Menu'}
    :Next >_Button    {caption='Next >' isvisible='true' type='org.eclipse.swt.widgets.Button' window=':WizardDialog_Shell'}
    :Project name:_Label    {caption='Project name:' isvisible='true' type='org.eclipse.swt.widgets.Label' window=':_Shell'}
    :Project name:_Text    {isvisible='true' leftWidget=':Project name:_Label' type='org.eclipse.swt.widgets.Text' window=':_Shell'}
    :WizardDialog_Shell    {data?='org.eclipse.jface.wizard.WizardDialog@*' isvisible='true' type='org.eclipse.swt.widgets.Shell'}
    :_Text    {isvisible='true' type='org.eclipse.swt.widgets.Text' window=':WizardDialog_Shell'}
    :_Tree    {isvisible='true' type='org.eclipse.swt.widgets.Tree' window=':WizardDialog_Shell'}
    '''
    
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


def createFolder(projectName, folderName):
    '''The following items are needed in the object.map:
    :Finish_Button_3    {caption='Finish' isvisible='true' type='org.eclipse.swt.widgets.Button' window=':WizardDialog_Shell'}
    :Folder name:_Label    {caption='Folder name:' isvisible='true' type='org.eclipse.swt.widgets.Label' window=':WizardDialog_Shell'}
    :Folder name:_Text    {isvisible='true' leftWidget=':Folder name:_Label' type='org.eclipse.swt.widgets.Text' window=':WizardDialog_Shell'}
'''
    activateItem(waitForObjectItem(":_Menu", "File"))
    activateItem(waitForObjectItem(":File_Menu", "New"))
    activateItem(waitForObjectItem(":New_Menu_2", "Other..."))
    type(waitForObject(":_Text"), "Folder")
    mouseClick(waitForObjectItem(":_Tree", "Folder"), 59, 10, 0, Button.Button1)
    clickButton(waitForObject(":Next >_Button"))
    mouseClick(waitForObjectItem(":_Tree", projectName), 82, 12, 0, Button.Button1)
    type(waitForObject(":Folder name:_Text"), folderName)
    mouseClick(waitForObject(":Folder name:_Text"), 126, 13, 0, Button.Button1)
    clickButton(waitForObject(":Finish_Button_3"))
    snooze(1)


# All these arguments = bad but not sure how to do his as not python expert.
def openExample(frag, project="data", folder="examples", subfolder=None, subsubfolder=None, findOnly=False):
    
    expand(waitForObjectItem(":Project Explorer_Tree", project))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", project))

    if (folder is not None):
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
            foundExample = child
            if not findOnly:
                doubleClick(child, 5, 5, 0, Button.Button1)
    
    # We wait for a few seconds for the part to open
    snooze(3)
    return foundExample

            
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
    ''' Open the given testdata file in DAWN and return the full path to the file '''
    pathfound = findFile("testdata", name)
    path = os.path.abspath(pathfound)
    # logging added since it appears that path separators might not be handled correctly on Windows
    test.log('openExternalFile called with "%s". findFile returned "%s". abspath returned "%s"' % (name, pathfound, path))
    activateItem(waitForObjectItem(":_Menu", "File"))
    activateItem(waitForObjectItem(":File_Menu", "Open File..."))
    chooseFile(waitForObject(":SWT"), path)
    return path

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
    destFilePath = "/scratch/workspace/"+suiteName+"/"+testName+"/workspace/"+project+"/"+subdir+"/"+fileName
    shutil.copyfile(path, destFilePath)
    mouseClick(waitForObjectItem(":Project Explorer_Tree", project))
    type(waitForObject(":Project Explorer_Tree"), "<F5>")
    
    return destFilePath


def chooseSlice():

    vals = dawn_constants
    mouseClick(waitForObjectItem(":Data_Table_2", "1/0"), 8, 12, 0, Button.Button1)

    mouseClick(waitForObject(":Slice as line plots_ToolItem_3"), 12, 14, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table_3", "0/2"), 13, 24, 0, Button.Button1)
    mouseDrag(waitForObject(":Data_Scale"), 18, 22, 20, 0, Modifier.None, Button.Button1)
    mouseClick(waitForObject(":XY plotting tools_ToolItem_2"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)

factory = None

def getPlottingSystem(name):
    
    global factory    
    if factory is not None:
        return factory.getPlottingSystem(name)
        
    snooze(5)
    #Unlikely that there is a Plot./Sys. view open, so matchOpen False
    openView("Plotting Systems", matchOpen=False)
    plotButton = waitForObject(":Plotting Systems.Refresh_RefreshButton")
    
    factoryClass = plotButton.getClass().getClassLoader().loadClass("org.eclipse.dawnsci.plotting.api.PlottingFactory")

    factory = factoryClass.newInstance()
    system  = factory.getPlottingSystem(name)
    
    # Close gallery
    snooze(1)
    try:
        plottingSystemsCTab = waitForSwtCTabItem("Plotting Systems")
        cTabChildren = object.children(plottingSystemsCTab.item)
        cTabCloseButton = None
        for c in cTabChildren:
            if "CTabCloseBox" in c["class"]:
                 cTabCloseButton = c
        if cTabCloseButton is None:
            raise Exception("No close button found!")
        
        clickTab(waitForObject(plottingSystemsCTab))
        mouseClick(waitForObject(cTabCloseButton))

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
    
