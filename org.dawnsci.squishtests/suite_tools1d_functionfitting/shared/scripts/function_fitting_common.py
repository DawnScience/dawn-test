source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "swt_treeitems.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))

# Start Function fitting on metalmix.mca
def startFunctionFitting():
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Data Browsing")
    
    #expand data tree and open metal mix
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    for child in children:
        if "metalmix.mca" in child.text:
            doubleClick(child)
            continue
    
    if(isEclipse4()):
        mouseClick(waitForObjectItem(":Data_Table_3", "0/0"), 12, 6, 0, Button.Button1)
    else:
        mouseClick(waitForObjectItem(":Data_Table", "0/0"), 12, 6, 0, Button.Button1)
    
    snooze(1)
    
    # start function fitting
    if(isEclipse4()):
        mouseClick(waitForObject(":XY plotting tools_ToolItem_3"), 28, 14, 0, Button.Button1)
    else:
        mouseClick(waitForObject(":XY plotting tools_ToolItem_2"), 28, 14, 0, Button.Button1)

    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))

    if(isEclipse4()):
        activateItem(waitForObjectItem(":Maths and Fitting_Menu_2", "Function Fitting"))
    else:
        activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Function Fitting"))
    
    
def setFunctionFittingRegion(regionStart, regionLength):
    if(isEclipse4()):
        mouseClick(waitForObject(":Configure Settings..._ToolItem_4"), 8, 13, 0, Button.Button1)
    else:
        mouseClick(waitForObject(":Configure Settings..._ToolItem_3"), 12, 16, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Regions_TabItem"))
    mouseClick(waitForObjectItem(":Regions.Region Location_Table", "0/1"))

    mouseClick(waitForObjectItem(":Regions.Region Location_Table", "0/1"), 34, 16, 0, Button.Button1)

    type(waitForObject(":Regions_Text"), "<Ctrl+a>")
    type(waitForObject(":Regions_Text"), str(regionStart))
    type(waitForObject(":Regions_Text"), "<Return>")

    mouseClick(waitForObjectItem(":Regions.Region Location_Table", "1/1"))

    mouseClick(waitForObjectItem(":Regions.Region Location_Table", "1/1"), 64, 2, 0, Button.Button1)
    type(waitForObject(":Regions_Text"), "<Ctrl+a>")
    type(waitForObject(":Regions_Text"), str(regionLength))
    type(waitForObject(":Regions_Text"), "<Numpad Return>")

    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    
def insertFunction(functionName):
    clickTab(waitForObject(":Function Fitting_CTabItem"))
    type(waitForObject(":Function Fitting_Tree"), "<Insert>")
    type(waitForObject(":Function Fitting_Text"), str(functionName))
    type(waitForObject(":Function Fitting_Text"), "<Return>")
    type(waitForObject(":Function Fitting_Text"), "<Return>")

# Set the field on the given path
# path is passed to  get_swt_tree_item to get the treeitem, see help for that
# field is one of below constants (i.e. column number)
# value is new value to put in field
FUNCTION_COL=0
VALUE_COL=1
LOWER_LIMIT_COL=2
UPPER_LIMIT_COL=3
FITTED_PARAMETERS_COL=4
def setField(path, column, value):
    subitem = get_swt_tree_sub_item(waitForObject(":Function Fitting_Tree"), path, column)
    mouseClick(subitem)
    type(waitForObject(":Function Fitting_Text"), str(value))
    type(waitForObject(":Function Fitting_Text"), "<Return>")
# Get the field value of the specified path and column
# See setField for use of path/column argument
def getField(path, column):
    subitem = get_swt_tree_sub_item(waitForObject(":Function Fitting_Tree"), path, column)
    return subitem.text
