source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "file_utils.py"))
source(findFile("scripts", "dawn_constants.py"))

from sys import platform as _platform
import platform
import os.path

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

    clickButton(waitForObject(":Images location_Button"))
    if (_platform == "linux" or _platform == "linux2"):
        chooseDirectory(waitForObject(":SWT"), "/scratch/workspace/suite_peema/tst_peema_dichroism/workspace/data/examples/peema")
    elif(_platform == "win32"):
        chooseDirectory(waitForObject(":SWT"), "C:\\scratch\\workspace\\suite_peema\\tst_peema_dichroism\\workspace\\data\\examples\\peema")

    #Play with slider...
    setValue(waitForObject(":Live Plot Control.Original Data_Scale"), 1)
    snooze(1)
    setValue(waitForObject(":Live Plot Control.Original Data_Scale"), 17)
    snooze(1)
    setValue(waitForObject(":Live Plot Control.Original Data_Scale"), 8)
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
    #    vals = dawn_constants
    clickButton(waitForObject(":Image Alignment.Align_Button"))
    mouseDrag(waitForObject(":Image Alignment.\rSelect a region of interest common to all images in the stack and press OK.\r_Scale"), 17, 22, 25, -11, Modifier.None, Button.Button1)
    clickButton(waitForObject(":Image Alignment.OK_Button"))
    snooze(2) # While aligning..
    
    mouseDrag(waitForObject(":Live Plot Control.Original Data_Scale"), 19, 23, -4, 15, Modifier.None, Button.Button1)
    
    clickTab(waitForObject(":Shifts_CTabItem"), 38, 16, 0, Button.Button1)
    system = getPlottingSystem("Shifts")
    test.verify(system.getTraces().size()==1)
    
    snooze(1)
    #test saving
    clickButton(waitForObject(":Peem Analysis View.Use default save directory_Button"))
    clickButton(waitForObject(":Output location.Save_Button"))
    
    snooze(2)
    #check if file exist
    if (_platform == "linux" or _platform == "linux2"):
        exist = os.path.isfile("/scratch/workspace/suite_peema/tst_peema_dichroism/workspace/data/examples/processing/dawn/d_peema.jpg")
    elif (_platform == "win32"):
        exist = os.path.exists("C:\\scratch\\workspace\\suite_peema\\tst_peema_dichroism\\workspace\\data\\examples\\processing\\dawn\\d_peema.jpg")

    test.verify(exist == True)
    if (_platform == "linux" or _platform == "linux2"):
        exist = os.path.isfile("/scratch/workspace/suite_peema/tst_peema_dichroism/workspace/data/examples/processing/dawn/d_peema.tif")
    elif (_platform == "win32"):
        exist = os.path.exists("C:\\scratch\\workspace\\suite_peema\\tst_peema_dichroism\\workspace\\data\\examples\\processing\\dawn\\d_peema.tif")

    test.verify(exist == True)

    snooze(2.1)
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()

