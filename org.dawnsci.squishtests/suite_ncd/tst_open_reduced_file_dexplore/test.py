source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))

def main():
    
    startOrAttachToDAWN()
    openPerspective("DExplore")
    
    openExternalFile("results_i22-107001_Pilatus2M_120713_183001.nxs")
    #There may be black magic at work here...
    #Test references original data which seems (but may not) be included in the sample
    #file being opened. It seems to work as of March 2015, so it's been uncommented.    
    snooze(2)
    
    system = getPlottingSystem("Dataset Plot")
    
    nxsTree = waitForTreeWithItem("entry1")
    expand(waitForObjectItem(nxsTree, "entry1"))
    snooze(2)
    expand(waitForObjectItem(nxsTree, "Pilatus2M"))
    snooze(2)
    doubleClick(waitForObjectItem(nxsTree, "data"), 17, 8, 0, Button.Button1)
    
    snooze(1) #This is important for the next line to work!
    shape = system.getTraces().toArray().at(0).getData().getShape()
    test.verify(shape.length == 2, "This should be a 2D plot")
    test.verify(shape.at(0) == 1679, "Image X shape should be 1679")
    test.verify(shape.at(1) == 1475, "Image Y shape should be 1475")
    
    expand(waitForObjectItem(nxsTree, "Pilatus2M__result"))
    
    doubleClick(waitForObjectItem(nxsTree, "data_1"), 19, 14, 0, Button.Button1)
    snooze(1)
    shape = system.getTraces().toArray().at(0).getData().getShape()
    test.verify((shape.length == 1) and (shape.at(0) == 1414), "This should be a 1D plot with X shape 1414")
    
    mouseClick(waitForObject(":Data axes selection_CTabFolderChevron"), 8, 4, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "2D image"))
    mouseClick(waitForObjectItem(":2D image.y-axis_Combo", "dim:2"), 0, 0, 0, Button.NoButton)
    snooze(1)
    shape = system.getTraces().toArray().at(0).getData().getShape()
    test.verify(shape.length == 2, "This should be a 2D plot")
    test.verify(shape.at(0) == 6, "Image X shape should be 6")
    test.verify(shape.at(1) == 1414, "Image Y shape should be 1414")
    
    mouseClick(waitForObjectItem(":2D image.y-axis_Combo", "dim:1"), 0, 0, 0, Button.NoButton)
    snooze(1)
    shape = system.getTraces().toArray().at(0).getData().getShape()
    test.verify(shape.length == 2, "This should be a 2D plot")
    test.verify(shape.at(0) == 7, "Image X shape should be 7")
    test.verify(shape.at(1) == 1414, "Image Y shape should be 1414")
    
    mouseClick(waitForObjectItem(":2D image.y-axis_Combo", "dim:3"), 0, 0, 0, Button.NoButton)
    snooze(1)
    shape = system.getTraces().toArray().at(0).getData().getShape()
    test.verify(shape.length == 2, "This should be a 2D plot")
    test.verify(shape.at(0) == 1414, "Image X shape should be 1414")
    test.verify(shape.at(1) == 1, "Image Y shape should be 1")

    
    mouseClick(waitForObject(":Data axes selection_CTabFolderChevron"), 5, 7, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "1D plot"))
    snooze(1)
    shape = system.getTraces().toArray().at(0).getData().getShape()
    test.verify((shape.length == 1) and (shape.at(0) == 1414), "This is a 1D plot with X shape 1414")
    test.verify(system.getTraces().toArray().at(0).getXData().getName() =="q")
    
    mouseClick(waitForObject(":_Twistie"), 2, 3, 0, Button.Button1)
    setValue(waitForObject(":_Slider"), 1)
    setValue(waitForObject(":_Slider"), 2)
    setValue(waitForObject(":_Slider"), 3)
    setValue(waitForObject(":_Slider"), 4)
    setValue(waitForObject(":_Slider"), 5)
    setValue(waitForObject(":_Slider"), 6)
    setValue(waitForObject(":_Slider_2"), 1)
    setValue(waitForObject(":_Slider_2"), 2)
    setValue(waitForObject(":_Slider_2"), 3)
    setValue(waitForObject(":_Slider_2"), 4)
    setValue(waitForObject(":_Slider_2"), 5)

    closeOrDetachFromDAWN()
