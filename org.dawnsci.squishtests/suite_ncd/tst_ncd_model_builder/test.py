source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))

def main():
    startOrAttachToDAWN()
    openPerspective("NCD Model Builder Perspective")

    clickTab(waitForObject(":File Navigator_CTabItem"), 57, 14, 0, Button.Button1)
    expand(waitForObjectItem(":File Navigator_Tree", "dls"))
    expand(waitForObjectItem(":File Navigator_Tree", "b21"))
    expand(waitForObjectItem(":File Navigator_Tree", "data_1"))
    expand(waitForObjectItem(":File Navigator_Tree", "2013"))
    expand(waitForObjectItem(":File Navigator_Tree", "cm5947-3"))
    expand(waitForObjectItem(":File Navigator_Tree", "processing"))
    mouseClick(waitForObjectItem(":File Navigator_Tree", "results__b21-2672__detector__040713__102411.nxs"), 40, 8, 0, Button.Button1)
    dragAndDrop(waitForObject(":results_b21-2672_detector_040713_102411.nxs.04/07/2013 10:24_TreeSubItem"), 69, 11, ":Data parameters.Data file_Text", 120, 10, DnD.DropLink)
    clickButton(waitForObject(":Data parameters.Run NCD model building_Button"))
    snooze(130)
    closeOrDetachFromDAWN()
