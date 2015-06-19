source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "dawn_constants.py"))

# This test makes sure we can start and stop DAWN
def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    
    # On a test you may add test code here 
    #Open data browsing perspective
    openPerspective("Data Browsing (default)")
    
    openExample("001.img")
    snooze(1)
    
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 32, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Image Rotation"))
    mouseClick(waitForObject(":Image Rotation.Rotation angle_Spinner"), -2, 10, 0, Button.Button1)
    type(waitForObject(":Image Rotation.Rotation angle_Spinner"), "45")
    mouseClick(waitForObject(":Resize the Bounding Box and do not crop the resulting rotated image_ToolItem"), 11, 7, 0, Button.Button1)
    
    #check new dimensions
    snooze(1)
    system = getPlottingSystem("Image Rotation")
    data = system.getTraces().iterator().next().getData()
    test.verify(data.getRank()==2, "Image plotted: Success")
    shape = data.getShape()
    test.verify(shape.at(0)==2896, "Rotated Image new width is 2896")
    test.verify(shape.at(1)==2896, "Rotated Image new height is 2896")


    doubleClick(waitForObject(":Image Rotation.Rotation angle_Spinner"), 31, 10, 0, Button.Button1)
    type(waitForObject(":Image Rotation.Rotation angle_Spinner"), "90")

    snooze(2)
    system1 = getPlottingSystem("Image Rotation")
    data1 = system1.getTraces().iterator().next().getData()
    shape1 = data1.getShape()
    test.verify(shape1.at(0)==2048, "Rotated Image new width is 2048")
    test.verify(shape1.at(1)==2048, "Rotated Image new height is 2048")
    
    snooze(1)
    #test jexlexpression
    clickTab(waitForObject(":Data_CTabItem_2"), 31, 7, 0, Button.Button1)
    mouseClick(waitForObject(":Adds an expression which can be plotted. Must be function of other data sets._ToolItem"), 6, 10, 0, Button.Button1)
    type(waitForObject(":Data_Text"), "im:")
    type(waitForObject(":Data_Text"), "rotate(ADSC_Image, 45, false)")
    type(waitForObject(":Data_Text"), "<Return>")
    
    #check new dimension
    snooze(2.5)
    system2 = getPlottingSystem("ref-testscale_1_001.img")
    data2 = system2.getTraces().iterator().next().getData()
    shape2 = data2.getShape()
    
    test.verify(shape2.at(0)==2896, "Rotated Image Width is 2896")
    test.verify(shape2.at(1)==2896, "Rotated Image Height is 2896")
    
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
