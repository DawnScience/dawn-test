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
    if (_platform == "linux"):
        chooseDirectory(waitForObject(":SWT"), "/scratch/workspace/suite_peema/tst_peema_stitch/workspace/data/examples/98950_UViewImage")
    elif(_platform == "win32"):
        chooseDirectory(waitForObject(":SWT"), "C:\\scratch\\workspace\\suite_peema\\tst_peema_stitch\\workspace\\data\\examples\\98950_UViewImage")

    snooze(2)
    mouseDrag(waitForObject(":Live Plot Control.Original Data_Scale"), 27, 27, 74, 15, Modifier.None, Button.Button1)
    #load dat file
    clickTab(waitForObject(":Peem Analysis Controls.Image Stitching_CTabItem"), 63, 14, 0, Button.Button1)
    clickButton(waitForObject(":Stitching/Mosaic prototype.Load_Button"))
    
    # wait for loading
    snooze(5)
    clickButton(waitForObject(":Image Stitching.Stitch_Button"))
    snooze(7)
    
    # check stitched image
    system = getPlottingSystem("Stitched")
    width = system.getTraces().iterator().next().getData().getShape().at(0)
    height = system.getTraces().iterator().next().getData().getShape().at(1)
    test.verify(width==1005.0, "width expected: 1395.0, Actual: "+ str(width))
    test.verify(height==1063.0, "height expected: 1369.0, Actual: "+ str(height))
    
    clickTab(waitForObject(":Stitched_CTabItem"), 37, 14, 0, Button.Button1)
    clickButton(waitForObject(":Image Stitching.Use feature association_Button"))
    
    clickButton(waitForObject(":Image Stitching.Stitch_Button"))
    
    snooze(15)
    system = getPlottingSystem("Stitched")
    width = system.getTraces().iterator().next().getData().getShape().at(0)
    height = system.getTraces().iterator().next().getData().getShape().at(1)
    test.verify(width==993.0, "width expected: 993.0, Actual: "+ str(width))
    test.verify(height==1028.0, "height expected: 1028.0, Actual: "+ str(height))
    
    #use background & feature association
    clickButton(waitForObject(":Image Stitching.Pseudo flat-field filter_Button"))
  
    clickButton(waitForObject(":Image Stitching.Stitch_Button"))
    snooze(21)
    system = getPlottingSystem("Stitched")
    width = system.getTraces().iterator().next().getData().getShape().at(0)
    height = system.getTraces().iterator().next().getData().getShape().at(1)
    if (_platform == "linux"):
        test.verify(width==998.0, "width expected: 998.0, Actual: "+ str(width))
        test.verify(height==1021.0, "height expected: 1021.0, Actual: "+ str(height))
    elif (_platform == "win32"):
        test.verify(width==980.0, "width expected: 998.0, Actual: "+ str(width))
        test.verify(height==1025.0, "height expected: 1021.0, Actual: "+ str(height))
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()

