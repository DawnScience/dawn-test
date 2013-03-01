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
    openExternalFile("tln_1_0001.cbf.zip")
    snooze(1) 

    system = getPlottingSystem("XPDSi7x7_2010-07-08_23-00-50.nxs")
    snooze(2)

    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()