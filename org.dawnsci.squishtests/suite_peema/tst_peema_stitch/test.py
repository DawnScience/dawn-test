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
    createDirectory("/scratch/workspace/suite_peema/tst_peema_stitch/workspace/data/examples", "98950_UViewImage")
    #Add peema test files to data project
    for x in range(1, 37):
        if (x < 10) :
            addExternalFile("ui0000000%d.tif" % (x), "suite_peema", "tst_peema_stitch", "data", "examples/98950_UViewImage")
        elif x > 9 :
            addExternalFile("ui000000%d.tif" % (x), "suite_peema", "tst_peema_stitch", "data", "examples/98950_UViewImage")
        addExternalFile("98950.dat", "suite_peema", "tst_peema_stitch", "data", "examples")
    #Open Peema perspective
    openPerspective("PEEMA")

    # load the peema file folder
    clickButton(waitForObject(":Images location_Button"))
    chooseDirectory(waitForObject(":SWT"), "/scratch/workspace/suite_peema/tst_peema_stitch/workspace/data/examples/98950_UViewImage")

    mouseDrag(waitForObject(":Live Plot Control.Original Data_Scale"), 27, 27, 74, 15, Modifier.None, Button.Button1)
    #load dat file
    clickButton(waitForObject(":Stitching/Mosaic prototype.Load_Button"))
    
    
    # wait for loading
    snooze(5)
    clickButton(waitForObject(":Stitching/Mosaic prototype.Stitch_Button"))
    snooze(3)
    
    # check stitched image
    system = getPlottingSystem("Stitched")
    width = system.getAxes().get(0).getUpper()
    test.verify(width==1369.0)
    
    clickTab(waitForObject(":Stitched_CTabItem"), 37, 14, 0, Button.Button1)
    clickButton(waitForObject(":Stitching/Mosaic prototype.Use feature association_Button"))
    
    clickButton(waitForObject(":Stitching/Mosaic prototype.Stitch_Button"))
    
    snooze(7)
    system = getPlottingSystem("Stitched")
    width = system.getAxes().get(0).getUpper()
    test.verify(width==1343.0)
    
    #use background & feature association
    clickButton(waitForObject(":Stitching/Mosaic prototype.Apply background subtraction_Button"))
    mouseDrag(waitForObject(":Stitching/Mosaic prototype.Apply background subtraction_Scale"), 26, 25, 11, 2, Modifier.None, Button.Button1)
  
    clickButton(waitForObject(":Stitching/Mosaic prototype.Stitch_Button"))
    snooze(20)
    system = getPlottingSystem("Stitched")
    width = system.getAxes().get(0).getUpper()
    test.verify(width==1344.0)

    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()

