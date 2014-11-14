source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))

#For some reason these files end up with different labels for some of their objects.
extraLabelNeeded = {'filter_example.moml':'_2', 
                    'gda_scan_example.moml':'_2', 
                    'plot_fit_example.moml':'_2'}

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
        #Ensure widget has no starting value
        widget = None
        
        doubleClick(child, 5, 5, 0, Button.Button1)
        #This file asks for the python interpreter (which isn't configured) so we dispel the message.
        name = child.text.split(" ")[0]
        if "python_pydev_numpy_example1.moml" in name:
            snooze(1)
            clickButton(waitForObject(":Python not configured.Don't ask again_Button"))
        
        if name in extraLabelNeeded:
            extra=extraLabelNeeded[name]
        else:
            extra=""
        
        try:
            widget = waitForObject(":"+name+".Edit_CTabItem"+extra, 3000)
            clickTab(widget)
            if widget:
                test.passes("Selected Edit tab of "+name)
        except:
            test.fail("Cannot select the Edit tab of "+name)
        
        #Reset the widget
        cWidget = None
        # text contains decorators.
        try:
            
            cWidget = waitForObject(":"+name+"_CTabCloseBox"+extra, 3000)
            mouseClick(cWidget)
            if cWidget:
                test.passes("Closed "+name)
        except:
            test.fail("Cannot select and close "+name)
   
    
    #Fail on jenkins, not reproduced on ws266. Add sleep in hope of fixing
    snooze(10)
    
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()
