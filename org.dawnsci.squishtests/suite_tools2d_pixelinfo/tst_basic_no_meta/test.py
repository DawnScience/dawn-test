source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))

def testIsNumeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# This test makes sure we can start and stop DAWN
def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    
    snooze(5)
    
    #openAndClearErrorLog()
    # On a test you may add test code here 
    openPerspective("Data Browsing (default)")
    
    openExample("0001.pgm")
    
    doubleClick(waitForObject(":Image tools used to profile and inspect images._ToolItem_2"), 26, 5, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Pixel Information"))
    
    tab = waitForObject(":Pixel Information_Table")
    test.verify(tab.getItemCount()==1,"1 row in table")
    
    c = waitForObject("{container=':image0001.pgm.Image_CTabItem' isvisible='true' occurrence='4' type='org.eclipse.swt.widgets.Composite'}")
    b = c.bounds
    
    mouseClick(c, b.x+b.width/8, b.y+b.height/3, 0, Button.Button1)
    snooze(1)
    mouseClick(c, b.x+b.width/4, b.y+b.height/5, 0, Button.Button1)
    snooze(1)
    mouseClick(c, b.x+b.width/5, b.y+b.height/2, 0, Button.Button1)
    snooze(1)
    mouseClick(c, b.x+b.width/6, b.y+b.height/4, 0, Button.Button1)
    snooze(1)
    
    test.verify(tab.getItemCount()==5,"5 rows in table")
    
    test.verify(waitForObjectItem(":Pixel Information_Table", "1/0").text == "Point 1")
    test.verify(testIsNumeric(waitForObjectItem(":Pixel Information_Table", "1/1").text))
    test.verify(testIsNumeric(waitForObjectItem(":Pixel Information_Table", "1/2").text))
    test.verify(testIsNumeric(waitForObjectItem(":Pixel Information_Table", "1/3").text))
    test.verify(not testIsNumeric(waitForObjectItem(":Pixel Information_Table", "1/4").text))
    test.verify(not testIsNumeric(waitForObjectItem(":Pixel Information_Table", "1/5").text))
    test.verify(not testIsNumeric(waitForObjectItem(":Pixel Information_Table", "1/6").text))
    test.verify(not testIsNumeric(waitForObjectItem(":Pixel Information_Table", "1/7").text))
    test.verify(not testIsNumeric(waitForObjectItem(":Pixel Information_Table", "1/8").text))
    
    mouseClick(waitForObjectItem(":Pixel Information_Table", "1/1"), 73, 5, 0, Button.Button1)
    mouseClick(waitForObject(":Delete selected region, if there is one._ToolItem"), 8, 14, 0, Button.Button1)
    
    test.verify(tab.getItemCount()==4,"4 rows in table")
    
    mouseClick(waitForObject(":Remove Region..._ToolItem_2"), 26, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Remove all regions..."))
    clickButton(waitForObject(":Please Confirm Delete All.OK_Button"))
    
    test.verify(tab.getItemCount()==1,"1 row in table")
    
    closeOrDetachFromDAWN()