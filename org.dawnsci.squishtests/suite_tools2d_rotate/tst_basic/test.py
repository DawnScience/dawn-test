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
    openPerspective("Data Browsing")
    
    openExample(".cbf")
    snooze(1)
    
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 32, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Image Rotation"))
    snooze(1)
    mouseClick(waitForObject(":Image Rotation.Rotation angle_Spinner"), -2, 10, 0, Button.Button1)
    type(waitForObject(":Image Rotation.Rotation angle_Spinner"), "45")
    mouseClick(waitForObject(":Resize the Bounding Box and do not crop the resulting rotated image_ToolItem"), 11, 7, 0, Button.Button1)
    
    #check new dimensions
    snooze(1)
    system = getPlottingSystem("Image Rotation")
    data = system.getTraces().iterator().next().getData()
    test.verify(data.getRank()==2, "Image plotted: Success")
    shape = data.getShape()
    test.verify(shape.at(0)==3528, "Rotated Image new width is 3528")
    test.verify(shape.at(1)==3528, "Rotated Image new height is 3528")


    doubleClick(waitForObject(":Image Rotation.Rotation angle_Spinner"), 31, 10, 0, Button.Button1)
    type(waitForObject(":Image Rotation.Rotation angle_Spinner"), "90")

    snooze(2)
    system1 = getPlottingSystem("Image Rotation")
    data1 = system1.getTraces().iterator().next().getData()
    shape1 = data1.getShape()
    test.verify(shape1.at(0)==2463, "Rotated Image new width is 2463")
    test.verify(shape1.at(1)==2527, "Rotated Image new height is 2527")
    
    snooze(1)
    #test jexlexpression
    clickTab(waitForObject(":Data_CTabItem_2"), 31, 7, 0, Button.Button1)


    mouseClick(waitForObject(":Adds an expression which can be plotted. Must be function of other data sets._ToolItem_2"), 19, 16, 0, Button.Button1)
#     mouseClick(waitForObject(":Adds an expression which can be plotted. Must be function of other data sets._ToolItem"), 6, 10, 0, Button.Button1)

    type(waitForObject(":Data_Text"), "im:rotate(image_01, 45, false)")
    
    #check new dimension

    mouseClick(waitForObjectItem(":Data_Table_3", "0/1"), 118, 7, 0, Button.Button1)

    snooze(2.5)
    system2 = getPlottingSystem("pow_M99S5_1_0001.cbf")
    data2 = system2.getTraces().iterator().next().getData()
    shape2 = data2.getShape()
    
    test.verify(shape2.at(0)==3528, "Rotated Image Width is 3528")
    test.verify(shape2.at(1)==3528, "Rotated Image Height is 3528")
    
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
