source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "file_utils.py"))
source(findFile("scripts", "dawn_constants.py"))

import platform

# UI test to check that an hdf5 file can be opened and its tree can be expanded 
def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()

    #create peema folder in data/examples
    createDirectory("/scratch/workspace/suite_peema/tst_peema_dichroism/workspace/data/examples", "peema")
    #Add peema test files to data project
    for x in range(1, 21):
        if (x < 10) :
            addExternalFile("ui0000000%d.png" % (x), "suite_peema", "tst_peema_dichroism", "data", "examples/peema")
        else :
            addExternalFile("ui000000%d.png" % (x), "suite_peema", "tst_peema_dichroism", "data", "examples/peema")

    #Open Peema perspective
    openPerspective("PEEMA")

    # load the peema file folder
    type(waitForObject(":Images location_Text"), "/scratch/workspace/suite_peema/tst_peema_dichroism/workspace/data/examples/peema")
    type(waitForObject(":Images location_Text"), "<Return>")
    if platform.uname()[0] == 'Linux':
        # On linux, the hard-coded path above auto-completes, so you need to press return twice
        #    the first selects the (only) matching auto-complete option, the second activates it
        # On windows, the auto-complete never matches (since the path does not start with C:\), so only one return is required
        snooze(1)
        type(waitForObject(":Images location_Text"), "<Return>")

    #Play with slider...
    setValue(waitForObject(":Image Playback_Slider"), 19)
    snooze(1)
    setValue(waitForObject(":Image Playback_Slider"), 15)
    snooze(1)

    #run the dichroism process
    clickButton(waitForObject(":Peem Analysis View.Dichroism_Button"))
    
    snooze(4)
    clickButton(waitForObject(":View.Diff_Button"))
    clickButton(waitForObject(":View.Abs_Button"))
    clickButton(waitForObject(":View.+_Button"))

    system = getPlottingSystem("Positive")
    test.verify(system.getTraces().size()==1)
    
    snooze(2)
    #Run the align process after having created a region of interest
    vals = dawn_constants
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), vals.TOOL_X, vals.TOOL_Y, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Profile"))
    activateItem(waitForObjectItem(":Profile_Menu", "Box Profile"))
    system = getPlottingSystem("Live Plot")
    c = system.getPlotComposite()
    b = c.bounds
    mouseDrag(c, b.x+b.width/8, b.y+b.height/3, int(b.width/4),b.height/3, 0, Button.Button1)
    snooze(2) # While fit..
    
    clickButton(waitForObject(":Peem Analysis View.Align_Button"))
    clickTab(waitForObject(":Shifts_CTabItem"), 38, 16, 0, Button.Button1)
    
    system = getPlottingSystem("Shifts")
    test.verify(system.getTraces().size()==1)
    
    snooze(1)
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()

