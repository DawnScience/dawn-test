source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_global_python_setup.py"))
source(findFile("scripts", "dawn_global_ui_controls.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))
source(findFile("scripts", "plotting_test.py"))
    
def main():
    
    #Start using clean workspace, open Python perspective with 
    #space for the console and setup python; switch on py4j automatically
    startOrAttachToDAWN(vmArgs='-DPREF_PY4J_ACTIVE=true')
    openPerspective("Data Browsing")
    setupPython()
    
    #Open a python console
    openPyDevConsole()
    
    # Press the record macro button
    mouseClick(waitForFirstSwtToolItem('Record Macro'), 6, 12, 0, Button.Button1)
    
    # Open a data file
    openExample("pow_M99S5_1_0001.cbf")
    
    #Need to give time for the macro to run through
    snooze(60)
    # Check that macro commands are there
    got = waitForObject(":PyDev Console").text
    test.verify("import numpy" in got, "Unable to find numpy command in macro recorded!")
    test.verify('ps = dnp.plot.getPlottingSystem("pow_M99S5_1_0001.cbf")' in got, "The correct plotting system was not in the macro")
    
    

    doubleClick(waitForFirstSwtToolItem("Configure Settings..."), 13, 5, 0, Button.Button1)
    #Need to give time for the configure settings box to appear
    snooze(5)
    
    mouseClick(waitForObject(":Graph.Title: _Text"), 82, 13, 0, Button.Button1)
    type(waitForObject(":Graph.Title: _Text"), "<Backspace>")
    type(waitForObject(":Graph.Title: _Text"), "<Backspace>")
    type(waitForObject(":Graph.Title: _Text"), "<Backspace>")
    type(waitForObject(":Graph.Title: _Text"), "<Backspace>")
    type(waitForObject(":Graph.Title: _Text"), "<Backspace>")
    type(waitForObject(":Graph.Title: _Text"), "<Backspace>")
    type(waitForObject(":Graph.Title: _Text"), "<Backspace>")
    type(waitForObject(":Graph.Title: _Text"), "<Backspace>")
    type(waitForObject(":Graph.Title: _Text"), "Fred")
    clickButton(waitForObject(":Configure Graph Settings.Apply_Button"))
    
    clickTab(waitForObject(":Configure Graph Settings.Image Traces_TabItem"))
    mouseClick(waitForObject(":Histogramming.Minimum Intensity_Text"), 38, 14, 0, Button.Button1)
    type(waitForObject(":Histogramming.Minimum Intensity_Text"), "<Backspace>")
    type(waitForObject(":Histogramming.Minimum Intensity_Text"), "<Backspace>")
    type(waitForObject(":Histogramming.Minimum Intensity_Text"), "5")
    mouseClick(waitForObject(":Histogramming.Maximum Intensity_Text"), 39, 17, 0, Button.Button1)
    type(waitForObject(":Histogramming.Maximum Intensity_Text"), "<Backspace>")
    type(waitForObject(":Histogramming.Maximum Intensity_Text"), "<Backspace>")
    type(waitForObject(":Histogramming.Maximum Intensity_Text"), "<Backspace>")
    type(waitForObject(":Histogramming.Maximum Intensity_Text"), "150")
    clickButton(waitForObject(":Configure Graph Settings.Apply_Button"))
    #Wait for graph settings to be updated.
    snooze(5)
    
    # Wait for commands to filter down.
    mouseClick(waitForObject(":Invalid Bounds.Lower cut_Text"), 61, 9, 0, Button.Button1)
    type(waitForObject(":Invalid Bounds.Lower cut_Text"), "<Backspace>")
    type(waitForObject(":Invalid Bounds.Lower cut_Text"), "<Backspace>")
    type(waitForObject(":Invalid Bounds.Lower cut_Text"), "5")
    mouseClick(waitForObject(":Invalid Bounds.Upper cut_Text"), 58, 11, 0, Button.Button1)
    type(waitForObject(":Invalid Bounds.Upper cut_Text"), "<Backspace>")
    type(waitForObject(":Invalid Bounds.Upper cut_Text"), "10000")
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    
    #Need to give time for the macro to run through
    snooze(45)
    got = waitForObject(":PyDev Console").text
    test.verify('ps.setTitle(\'Fred\')' in got,          "Changing the title not echoed in macro")
    test.verify('trace_image01.setMin(' in got,          "setMin not echoed in macro")
    test.verify('trace_image01.setMax(' in got,          "setMax not echoed in macro")
    test.verify('dnp.plot.createHistogramBound(' in got, "createHistogramBound not echoed in macro")
    test.verify('trace_image01.setMinCut(' in got,       "setMinCut not echoed in macro")
    test.verify('trace_image01.setMaxCut(' in got,       "setMaxCut not echoed in macro")
    
    closeOrDetachFromDAWN()
