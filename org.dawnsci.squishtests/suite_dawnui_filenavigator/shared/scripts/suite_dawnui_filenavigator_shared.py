def openLabelDecorationsPref():
    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Preferences"))
    expand(waitForObjectItem(":Preferences_Tree", "General"))
    expand(waitForObjectItem(":Preferences_Tree", "Appearance"))
    mouseClick(waitForObjectItem(":Preferences_Tree", "Label Decorations"))

def decDATFileScanCommand():
    mouseClick(waitForObject(":DAT file Scan Command Decorator_ItemCheckbox"))

def decFileMetaData():
    mouseClick(waitForObject(":File Meta Data Decorator_ItemCheckbox"))

def decHDFTreeElement():
    mouseClick(waitForObject(":HDF5 tree element Decorator_ItemCheckbox"))
    #mouseClick(waitForObject(":HDF5 tree element Decorator_ItemCheckbox"), 11, 13, 0, Button.Button1)

def prefDone():
    clickButton(waitForObject(":Preferences.OK_Button"))


def toggleDATFileMDDecorators():
    openLabelDecorationsPref()
    decDATFileScanCommand()
    decFileMetaData()
    prefDone()

def toggleHDFFileMDDecorators():
    openLabelDecorationsPref()
    decFileMetaData()
    decHDFTreeElement()
    prefDone()

def toggleFileMDDecorator():
    openLabelDecorationsPref()
    decFileMetaData()
    prefDone()
