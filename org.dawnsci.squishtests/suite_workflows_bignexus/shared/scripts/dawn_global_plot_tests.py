def check_plotted_trace_name_yval(configObj,name,ymax,ymin):
    #configObj from conOb = waitForObject(":Configure Settings..._ToolItem") configure
    #settings tool item
    snooze(1)
    mouseClick(configObj, 11, 14, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Axes_TabItem"))

    mouseClick(waitForObjectItem(":Select Axis_Combo", "(Y-Axis)"), 0, 0, 0, Button.NoButton)
    snooze(1)#added snooze since these boxes may be disabled so need to use find rather than wait for
    widget = findObject(":Change Settings.Maximum_Text")
    test.verify(widget.text == ymax,"Check Y Axis Maximum Expected: " + ymax + " Actual: "+ widget.text)
    widget= findObject("{leftWidget=':Change Settings.Minimum: _Label' type='org.eclipse.swt.widgets.Text'}")
    test.verify(widget.text == ymin,"Check Y Axis Minimum Expected: " + ymin + " Actual: "+ widget.text)
    
    clickTab(waitForObject(":Configure Graph Settings.Traces_TabItem"))
    widget = waitForObject(":Select Trace_Combo")
    test.verify(widget.text == name, "Check Trace Name Expected: " + name + " Actual: "+ widget.text)
    
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    
def check_plotted_traces_names(configObj, nameList):
    
    mouseClick(configObj)
    clickTab(waitForObject(":Configure Graph Settings.Traces_TabItem"))
    wid = waitForObject(":Select Trace_Combo")
    chil = object.children(wid)
    
    test.verify(len(chil)==len(nameList), "Combo List length Expected: " +str(len(nameList)) +"Actual: "+ str(len(chil)))
    
    for i in range(len(chil)):
        test.verify(chil[i].text == nameList[i], "Trace names Expected: " + nameList[i] + " Actual: "+ chil[i].text)
    
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    