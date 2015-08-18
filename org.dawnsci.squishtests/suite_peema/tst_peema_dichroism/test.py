source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "file_utils.py"))
source(findFile("scripts", "dawn_constants.py"))

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
    chooseDirectory(waitForObject(":SWT"), "/scratch/workspace/suite_peema/tst_peema_dichroism/workspace/data/examples/peema")

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
    mouseClick(waitForObjectItem(":Alignment_Combo", "With ROI"), 0, 0, 0, Button.NoButton)
    snooze(2) # While fit..
    
    clickButton(waitForObject(":Peem Analysis View.Align_Button"))
    clickTab(waitForObject(":Shifts_CTabItem"), 38, 16, 0, Button.Button1)
    
    system = getPlottingSystem("Shifts")
    test.verify(system.getTraces().size()==1)
    
    snooze(1)
    #test align with hessian transform buttons
    mouseClick(waitForObjectItem(":Alignment_Combo", "Affine transform"), 0, 0, 0, Button.NoButton)

#    mouseClick(waitForObjectItem(":Peem Analysis View.Add Region_Combo", "Affine transform"), 0, 0, 0, Button.NoButton)
    clickButton(waitForObject(":Peem Analysis View.Align_Button"))
    snooze(3.5)
    #test saving
    clickButton(waitForObject(":Peem Analysis View.Use default save directory_Button"))
    clickButton(waitForObject(":Output location.Save_Button"))
    clickButton(waitForObject(":File saved.OK_Button"))
    #check if file exist
    exist = os.path.isfile("/scratch/workspace/suite_peema/tst_peema_dichroism/workspace/data/examples/peema/processing/d_peema.jpg")
    test.verify(exist == True)
    exist = os.path.isfile("/scratch/workspace/suite_peema/tst_peema_dichroism/workspace/data/examples/peema/processing/d_peema.tif")
    test.verify(exist == True)

    snooze(2.1)
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()

