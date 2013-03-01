source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))

import os
from datetime import datetime

def main():
    
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    openPerspective("Workflow")
    createProject("workflows")
    
    expand(waitForObjectItem(":Project Explorer_Tree", "workflows"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    for child in children:
        doubleClick(child, 5, 5, 0, Button.Button1)
        name = child.text.split(" ")[0]
        
        try:
            widget = waitForObject(":"+name+".Edit_CTabItem", 3000)
            clickTab(widget)
        except:
            test.log("Cannot select the info tab of "+name)

        # text contains decorators.
        try:
            
            widget = waitForObject(":"+name+"_CTabCloseBox", 1000)
            mouseClick(widget)
        except:
            test.log("Cannot select and close "+name)
   
    
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
