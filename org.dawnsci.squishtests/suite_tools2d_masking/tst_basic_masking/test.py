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
    openPerspective("Data Browsing (default)")


    openExternalFile("ref-testscale_1_001.img")
    mouseClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 25, 8, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Masking"))
    
    snooze(1)
    clickButton(waitForObject(":Masking 'ref-testscale_1_001.img'.Enable lower mask    _Button"))
    clickButton(waitForObject(":Masking 'ref-testscale_1_001.img'.Enable upper mask    _Button"))
    
    system = getPlottingSystem("ref-testscale_1_001.img")
    test.verify(system.getTraces().size()==1)
    test.passes("One trace plotted") 

    imageTrace = system.getTraces().iterator().next()
    imageData  = imageTrace.getData()
    test.verify(imageData!=None)
    
    maskData  = imageTrace.getMask()
    test.verify(maskData!=None)


    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()