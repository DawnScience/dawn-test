source(findFile("scripts", "dawn_global_startup.py"))

import os
from datetime import datetime

def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    
    # On a test you may add test code here 
    #Open data browsing perspective
    # openPerspective("Data Browsing (default)")

    testtime("thermolysin.mccd", 15, 64, 12)
    testtime("5.tif", 15, 31, 17)
        
    
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()


def testtime(name, time,x,y):
    
    path = findFile("testdata", name);
    path = os.path.abspath(path)
    activateItem(waitForObjectItem(":_Menu", "File"))
    activateItem(waitForObjectItem(":File_Menu", "Open File..."))
    
    start = datetime.now()
    chooseFile(waitForObject(":SWT"), path)
    clickTab(waitForObject(":"+name+"_CTabItem"), x, y, 0, Button.Button1)
    end = datetime.now()

    diff = (end-start).seconds
    test.verify(diff<=time, "Image time to open ("+str(diff)+"s) less than "+str(time)+"s") 
    return
