source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))


def getTracePeakToPeak(system):
    ts=system.getTraces()
    t = ts.toArray().at(0)
    return t.data.peakToPeak().doubleValue()

def getXTraceFirst(system):
    ts=system.getTraces()
    t = ts.toArray().at(0)
    return t.xdata.get(0)

def getTraceShape(system):
    ts=system.getTraces()
    t = ts.toArray().at(0)
    return t.data.getShape()

def waitOnProgress():
    snooze(1)
    i = 0;
    while i < 20 and object.exists(":_ProgressBar"):
        snooze(1)
        i=i+1
    

def main():
    
    startOrAttachToDAWN()
    openPerspective("Data Browsing (default)")
    snooze(1)
    

    clickTab(waitForObject(":Data_CTabItem"), 42, 14, 0, Button.Button3)
    activateItem(waitForObjectItem(":Pop Up Menu", "Size"))
    activateItem(waitForObjectItem(":Size_Menu", "Left"))
    i = 0;
    while i < 20:
        type(waitForObject(":_Sash"), "<Left>")
        i=i+1
    
    openExample("pow_M99S5")
    
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem_3"), dawn_constants.TOOL_X, dawn_constants.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Science"))
    activateItem(waitForObjectItem(":Science_Menu", "Powder Integration"))

    system = getPlottingSystem("Powder Integration")
    
    ptp =getTracePeakToPeak(system)
    x0 = getXTraceFirst(system)
    
    test.verify( abs((ptp) - 1500) < 100 , "Peak to peak acceptable")
    test.verify( abs(x0 - 0.01) < 0.01 , "x0 acceptable")
    
    mouseClick(waitForObject(":Show Advanced Options_ToolItem"), 5, 5, 0, Button.Button1)
    

    clickButton(waitForObject(":Integration Options.Set Radial Range_Button"))
    mouseClick(waitForObject(":Integration Options.Min:_Text"), 25, 4, 0, Button.Button1)
    type(waitForObject(":Integration Options.Min:_Text"), "<Numpad 1>")
    type(waitForObject(":Integration Options.Min:_Text"), "<Numpad Decimal>")
    type(waitForObject(":Integration Options.Min:_Text"), "<Numpad 6>")
    
    mouseClick(waitForObject(":Integration Options.Max:_Text"), 51, 6, 0, Button.Button1)
    type(waitForObject(":Integration Options.Max:_Text"), "<Numpad 1>")
    type(waitForObject(":Integration Options.Max:_Text"), "<Numpad Decimal>")
    type(waitForObject(":Integration Options.Max:_Text"), "<Numpad 8>")
    
    mouseDrag(waitForObject(":Integration Options.Number of Bins X:_Text"), 74, 12, 45, 2, Modifier.None, Button.Button1)
    type(waitForObject(":Integration Options.Number of Bins X:_Text"), "<Ctrl+a>")
    type(waitForObject(":Integration Options.Number of Bins X:_Text"), "<Numpad 1>")
    type(waitForObject(":Integration Options.Number of Bins X:_Text"), "<Numpad 0>")
    type(waitForObject(":Integration Options.Number of Bins X:_Text"), "<Numpad 0>")
    type(waitForObject(":Integration Options.Number of Bins X:_Text"), "<Numpad Return>")
    
    waitOnProgress()
    
    ptp =getTracePeakToPeak(system)
    x0 = getXTraceFirst(system)
    
    test.verify( ptp < 40 , "Peak to peak acceptable")
    test.verify( x0 == 1.6, "x0 acceptable")
    
    mouseClick(waitForObject(":View Menu_ToolItem_3"), 14, 5, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Non pixel splitting"))
    activateItem(waitForObjectItem(":Non pixel splitting_Menu", "Pixel splitting"))
    
    waitOnProgress()
    
    ptp1 = getTracePeakToPeak(system)
    x0 = getXTraceFirst(system)
    
    test.verify( not (ptp1 == ptp) , "Peak to peak acceptable")
    test.verify( x0 == 1.6, "x0 acceptable")
    
    clickButton(waitForObject(":Integration Options.Set Radial Range_Button"))
    clickButton(waitForObject(":Integration Options.Reset_Button"))
    
    waitOnProgress()
    
    ptp = getTracePeakToPeak(system)
    x0 = getXTraceFirst(system)
    
    test.verify( abs(x0 - 0.01) < 0.01 , "x0 acceptable")
    test.verify( not (ptp1 == ptp) , "Peak to peak acceptable")
    
    mouseClick(waitForObject(":View Menu_ToolItem_3"), 8, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Pixel splitting"))
    activateItem(waitForObjectItem(":Non pixel splitting_Menu", "Non pixel splitting 2D"))
    
    waitOnProgress()
    
    sh = getTraceShape(system)
    test.verify( sh.at(0) == 1797 , "x acceptable")
    test.verify( sh.at(1) == 1797 , "y acceptable")
    
    mouseClick(waitForObject(":Integration Options.Number of Bins Y:_Text"), 156, 11, 0, Button.Button1)
    type(waitForObject(":Integration Options.Number of Bins X:_Text"), "<Ctrl+a>")
    type(waitForObject(":Integration Options.Number of Bins Y:_Text"), "<Numpad 3>")
    type(waitForObject(":Integration Options.Number of Bins Y:_Text"), "<Numpad 6>")
    type(waitForObject(":Integration Options.Number of Bins Y:_Text"), "<Numpad 0>")
    type(waitForObject(":Integration Options.Number of Bins Y:_Text"), "<Numpad Return>")
    

    mouseClick(waitForObject(":_ProgressBar"), 7, 6, 0, Button.Button1)

    waitOnProgress()
    
    ptp = getTracePeakToPeak(system)
    sh = getTraceShape(system)

    test.verify( sh.at(0) == 360 , "x acceptable")
    test.verify( sh.at(1) == 1797 , "y acceptable")
    
    mouseClick(waitForObject(":View Menu_ToolItem_3"), 8, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Non pixel splitting 2D"))
    activateItem(waitForObjectItem(":Non pixel splitting_Menu", "Pixel splitting 2D"))
    
    waitOnProgress()
    
    ptp1 = getTracePeakToPeak(system)
    test.verify( not (ptp1 == ptp) , "Peak to peak acceptable")
    
    mouseClick(waitForObject(":View Menu_ToolItem_3"), 14, 5, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Pixel splitting 2D"))
    activateItem(waitForObjectItem(":Non pixel splitting_Menu", "Non pixel splitting"))
    
    waitOnProgress()
    x0 = getXTraceFirst(system)
    
    mouseClick(waitForObject(":View Menu_ToolItem_3"), 17, 13, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Q"))
    activateItem(waitForObjectItem(":Q_Menu", "2θ"))
    snooze(2)
    x1 = getXTraceFirst(system)
    test.verify( not (x0 == x1) , "x0 value acceptable")
    
    ptp = getTracePeakToPeak(system)
    
    clickTab(waitForObject(":Powder Integration.Correction Options_CTabItem"), 73, 5, 0, Button.Button1)
    clickButton(waitForObject(":Correction Options.Apply Solid Angle Correction_Button"))
    waitOnProgress()
    ptp1 = getTracePeakToPeak(system)
    
    test.verify( not (ptp1 == ptp) , "Peak to peak acceptable")
    ptp = ptp1
    
    clickButton(waitForObject(":Correction Options.Apply Polarisation Correction_Button"))
    waitOnProgress()
    ptp1 = getTracePeakToPeak(system)
    test.verify( not (ptp1 == ptp) , "Peak to peak acceptable")
    ptp = ptp1
    
    clickButton(waitForObject(":Correction Options.Apply Detector Transmission Correction_Button"))
    mouseClick(waitForObject(":Correction Options.Tranmission Factor:_Text"), 101, 19, 0, Button.Button1)
    type(waitForObject(":Correction Options.Tranmission Factor:_Text"), "<Ctrl+a>")
    type(waitForObject(":Correction Options.Tranmission Factor:_Text"), "<Numpad 0>")
    type(waitForObject(":Correction Options.Tranmission Factor:_Text"), "<Numpad Decimal>")
    type(waitForObject(":Correction Options.Tranmission Factor:_Text"), "<Numpad 5>")
    type(waitForObject(":Correction Options.Tranmission Factor:_Text"), "<Numpad Return>")
    waitOnProgress()
    ptp1 = getTracePeakToPeak(system)
    test.verify( not (ptp1 == ptp) , "Peak to peak acceptable")
    snooze(1)
    

    
    