source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))

def main():
    
    #Start using clean workspace
    startOrAttachToDAWN()
    # Open data browsing perspective 
    openPerspective("Powder Calibration")
    
    snooze(1)
    
    openExample("pow_M99S5")
    
    snooze(1)
    wid = waitForObject(":Distance_TreeItem")
    child = object.children(wid)
    test.verify ("200" in child[2].text, "check cbf distance")
    
    wid = waitForObject(":Wavelength_TreeItem")
    child = object.children(wid)
    test.verify ("0.9763" in child[2].text, "check cbf wavelength")
    
    mouseClick(waitForObjectItem(":Select calibrant:_Combo", "Cr2O3"))
#     clickButton(waitForObject(":Run Calibration.Finish with point calibration optimisation_Button"))

    clickButton(waitForObject(":Run Calibration.Run Calibration_Button"))
    
    i = 0
    while object.exists(":Progress Information.Cancel_Button") and i < 20:
        snooze(5)
        i=i+1
    
    wid = waitForObject(":Distance_TreeItem")
    child = object.children(wid)
    test.verify ("199" in child[2].text, "check calibrated distance")
    wid = waitForObject(":Wavelength_TreeItem")
    child = object.children(wid)
    test.verify ("0.9759" in child[2].text, "check calibrated wavelength")
    
    closeOrDetachFromDAWN()