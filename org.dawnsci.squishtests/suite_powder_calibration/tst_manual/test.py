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
    
    wid = waitForObject(":X_TreeItem_2")
    xText = object.children(wid)[2].text
    test.verify ("1225.28" in xText, "check cbf x")
    wid = waitForObject(":Y_TreeItem_2")
    yText = object.children(wid)[2].text
    test.verify ("1223.32" in yText, "check cbf y")
    
    clickButton(waitForObject(":Diffraction Calibration Controls.Manual_Button"))

    snooze(0.5)
    
    clickButton(waitForObject(":Diffraction Calibration Controls_Button_3"))
    clickButton(waitForObject(":Diffraction Calibration Controls_Button_3"))
    clickButton(waitForObject(":Diffraction Calibration Controls_Button_4"))
    clickButton(waitForObject(":Diffraction Calibration Controls_Button_4"))

    wid1 = waitForObject(":X_TreeItem_2")
    xText1 = object.children(wid1)[2].text
    test.verify (not (xText1 in xText), "check cbf x")
    wid1 = waitForObject(":Y_TreeItem_2")
    yText1 = object.children(wid1)[2].text
    test.verify (not (yText1 in yText), "check cbf y")
    
    snooze(0.5)
    
    clickButton(waitForObject(":Diffraction Calibration Controls_Button_5"))
    clickButton(waitForObject(":Diffraction Calibration Controls_Button_5"))
    clickButton(waitForObject(":Diffraction Calibration Controls_Button_2"))
    clickButton(waitForObject(":Diffraction Calibration Controls_Button_2"))

    wid2 = waitForObject(":X_TreeItem_2")
    xText1 = object.children(wid2)[2].text
    test.verify (xText1 in xText, "check cbf x")
    wid2 = waitForObject(":Y_TreeItem_2")
    yText1 = object.children(wid2)[2].text
    test.verify (yText1 in yText, "check cbf y")
    
    clickButton(waitForObject(":Diffraction Calibration Controls.Find Rings_Button"))

    i = 0
    while object.exists(":Progress Information.Cancel_Button") and i < 20:
        snooze(5)
        i=i+1

    snooze(2)
    
    clickButton(waitForObject(":Run Calibration.Run Calibration_Button"))
    
    i = 0
    while object.exists(":Progress Information.Cancel_Button") and i < 20:
        snooze(5)
        i=i+1
    
    wid3 = waitForObject(":Distance_TreeItem")
    child = object.children(wid3)
    test.verify ("199" in child[2].text, "check calibrated distance")
    wid3 = waitForObject(":Wavelength_TreeItem")
    child = object.children(wid3)
    test.verify ("0.97" in child[2].text, "check calibrated wavelength ~0.97 it is: " + child[2].text)
    
    closeOrDetachFromDAWN()
