source(findFile("scripts", "utilities.py"))

def main():
    startOrAttachToDAWN()
    
    # Install EPD to the default location
    # On a clean machine setupEPDPython will defer
    # to setupPython(installEPD=True)
    # On a machine where EPD is already installed
    # it will simply be selected
    setupEPDPython() 
    
    closeOrDetachFromDAWN()

