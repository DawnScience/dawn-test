source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "swt_treeitems.py"))

# Start Function fitting on metalmix.mca
def startFunctionFitting():
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Data Browsing (default)")
    
    #expand data tree and open metal mix
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    for child in children:
        if "metalmix.mca" in child.text:
            doubleClick(child)
            continue
    
    mouseClick(waitForObjectItem(":Data_Table", "0/0"))
    
    snooze(1)
    
    # start function fitting
    mouseClick(waitForObject(":XY plotting tools_ToolItem_2"))
    activateItem(waitForObjectItem(":Pop Up Menu", "Maths and Fitting"))
    activateItem(waitForObjectItem(":Maths and Fitting_Menu", "Function Fitting"))
    
    
def setFunctionFittingRegion(regionStart, regionLength):    
    mouseClick(waitForObject(":Configure Settings..._ToolItem_3"))
    clickTab(waitForObject(":Configure Graph Settings.Regions_TabItem"))
    mouseClick(waitForObjectItem(":Regions.Region Location_Table", "0/1"))
    type(waitForObject(":Regions_Spinner"), str(regionStart))
    mouseClick(waitForObjectItem(":Regions.Region Location_Table", "1/1"))
    type(waitForObject(":Regions_Spinner"), str(regionLength))
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
