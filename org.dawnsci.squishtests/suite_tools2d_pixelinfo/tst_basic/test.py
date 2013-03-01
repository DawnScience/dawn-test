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
    
    # On a test you may add test code here 
    openPerspective("Data Browsing (default)")
    
    openExample("001.img")
    
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 29, 5, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Pixel Information"))
    
    tab = waitForObject(":Pixel Information_Table")
    test.verify(tab.getItemCount()==1,"1 row in table")
    
    c = waitForObject("{container=':ref-testscale_1_001.img.Image_CTabItem' isvisible='true' occurrence='4' type='org.eclipse.swt.widgets.Composite'}")
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
    test.verify(testIsNumeric(waitForObjectItem(":Pixel Information_Table", "1/4").text))
    test.verify(testIsNumeric(waitForObjectItem(":Pixel Information_Table", "1/5").text))
    test.verify(testIsNumeric(waitForObjectItem(":Pixel Information_Table", "1/6").text))
    test.verify(testIsNumeric(waitForObjectItem(":Pixel Information_Table", "1/7").text))
    test.verify(testIsNumeric(waitForObjectItem(":Pixel Information_Table", "1/8").text))
    
    mouseClick(waitForObjectItem(":Pixel Information_Table", "1/1"), 73, 5, 0, Button.Button1)
    mouseClick(waitForObject(":Delete selected region, if there is one._ToolItem"), 8, 14, 0, Button.Button1)
    
    test.verify(tab.getItemCount()==4,"4 rows in table")
    
    mouseClick(waitForObject(":Remove Region..._ToolItem"), 25, 5, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Remove all regions..."))
    clickButton(waitForObject(":Please Confirm Delete All.OK_Button"))
    
    test.verify(tab.getItemCount() == 1, "1 row in table")
    
    mouseClick(c, b.x+b.width/8, b.y+b.height/3, 0, Button.Button1)
    snooze(1)
    
    test.verify(tab.getItemCount() == 2, "2 row in table")
    
    mouseClick(waitForObject(":View Menu_ToolItem"), 10, 8, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open 'Pixel Information' in dedicated view"))
    
    test.verify(tab.getItemCount() == 2 or tab.getItemCount() == 3, "2 row in table")
    
    mouseClick(waitForObject(":View Menu_ToolItem"), 16, 7, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Open cheat sheet for 'Pixel Information'"))
    

    closeOrDetachFromDAWN()