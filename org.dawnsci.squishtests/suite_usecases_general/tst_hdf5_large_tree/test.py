source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))

# This test makes sure we can start and stop DAWN
def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    
    # On a test you may add test code here 
    #Open data browsing perspective
    openPerspective("Data Browsing") 
    openExternalFile("XPDSi7x7_2010-07-08_23-00-50.nxs")
    
    counter = 0;
    
    while (not object.exists(":Data_Table_2")):
        if counter < 50:
            snooze(2)
            counter += 1
        else:
            test.fatal("file open timed out")
            closeOrDetachFromDAWN()
            return
        
    snooze(5)
    mouseClick(waitForObjectItem(":Data_Table_2", "0/0"), 9, 15, 0, Button.Button1)
    snooze(5) 
    mouseClick(waitForObjectItem(":Data_Table_2", "1/0"), 10, 15, 0, Button.Button1)
    snooze(5) 
    mouseClick(waitForObjectItem(":Data_Table_2", "2/0"), 7, 11, 0, Button.Button1)
    snooze(5) 
    mouseClick(waitForObjectItem(":Data_Table_2", "3/0"), 8, 10, 0, Button.Button1)
    snooze(5) 
    mouseClick(waitForObjectItem(":Data_Table_2", "9/0"), 6, 13, 0, Button.Button1)
    snooze(5) 
    mouseClick(waitForObjectItem(":Data_Table_2", "81/0"), 5, 13, 0, Button.Button1)
    snooze(5) 

    system = getPlottingSystem("XPDSi7x7_2010-07-08_23-00-50.nxs")
    test.verify(system.getTraces().iterator().next().getData().getRank()==2, "Check image plotted")

    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()


