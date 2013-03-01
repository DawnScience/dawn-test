source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))

def testIsNumeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def main():
    
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Data Browsing (default)")
    
    #expand data tree and open metal mix
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    for child in children:
        if "metalmix.mca" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            continue
    
    mouseClick(waitForObjectItem(":Data_Table", "0/0"), 9, 7, 0, Button.Button1)
    
    #Change to measurement
    mouseClick(waitForObject(":XY plotting tools_ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Measurement"))
    
    #DRAW ONE
    tab = waitForObject(":Measurement_Table")
    #starts with one empty item
    test.verify(tab.getItemCount()==1,"table empty")
    #draw region
    c = waitForObject(":Plot_Composite")
    b = c.bounds

    test.log("Image at (%d, %d) is %d x %d" % (b.x,b.y, b.width, b.height))
    mouseDrag(c, b.x+b.width/3, b.y+b.height/3, int(b.width/1.7),b.height/3, 0, Button.Button1)
    snooze(1)
    
    test.verify(tab.getItemCount()==1,"one line in table")
    #check table entries
    test.verify(waitForObjectItem(":Measurement_Table", "0/0").text=="Measurement 1","Test cell 0")
    test.verify(waitForObjectItem(":Measurement_Table", "0/1").text=="Line","Test cell 1")
    test.verify(testIsNumeric(waitForObjectItem(":Measurement_Table", "0/2").text),"Test cell 2")
    test.verify(testIsNumeric(waitForObjectItem(":Measurement_Table", "0/3").text),"Test cell 3")
    test.verify(testIsNumeric(waitForObjectItem(":Measurement_Table", "0/4").text),"Test cell 4")
    val = waitForObjectItem(":Measurement_Table", "0/5").text
    test.verify("Start" in val, "Test cell 5/0")
    test.verify("Length" in val, "Test cell 5/1")
    test.verify("Angle" in val, "Test cell 5/2")
    
    #open in dedicated view
    mouseClick(waitForObject(":View Menu_ToolItem_3"), 9, 14, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open 'Measurement' in dedicated view"))
    
    test.verify(tab.getItemCount()==1,"one line in table")
    #check table
    test.verify(waitForObjectItem(":Measurement_Table", "0/0").text=="Measurement 1","Test cell 0")
    test.verify(waitForObjectItem(":Measurement_Table", "0/1").text=="Line","Test cell 1")
    test.verify(testIsNumeric(waitForObjectItem(":Measurement_Table", "0/2").text),"Test cell 2")
    test.verify(testIsNumeric(waitForObjectItem(":Measurement_Table", "0/3").text),"Test cell 3")
    test.verify(testIsNumeric(waitForObjectItem(":Measurement_Table", "0/4").text),"Test cell 4")
    val = waitForObjectItem(":Measurement_Table", "0/5").text
    test.verify("Start" in val, "Test cell 5/0")
    test.verify("Length" in val, "Test cell 5/1")
    test.verify("Angle" in val, "Test cell 5/2")
    #draw region
    c = waitForObject(":Plot_Composite")
    b = c.bounds
    
    test.log("Image at (%d, %d) is %d x %d" % (b.x,b.y, b.width, b.height))
    mouseDrag(c, b.x+b.width/2.1, b.y+b.height/3, int(b.width/3),b.height/5, 0, Button.Button1)
    snooze(1)
    #check table
    tab = waitForObject(":Measurement_Table")
    test.verify(tab.getItemCount() == 2, "two lines in table")

    closeOrDetachFromDAWN()