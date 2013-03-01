source(findFile("scripts", "mx_pipelines_utils.py"))

def main():
    
    # This test should only run on Linux x86_64
    import platform, sys
    if platform.uname()[0] != 'Linux' or platform.uname()[4] != 'x86_64':
        return
    
    # Start Dawn, open correct perspective, set a reasonable port
    startOrAttachToDAWN()
    openPerspective("MX Pipelines")
    setPort(8081)

    # Create, set and change to the working directory
    wdir = "/dls/tmp/squishtests"
    try:
        os.makedirs(wdir, 0777)
    except:
        pass
    setDirectories(wdir) 
    os.chdir(wdir)
    
    # Delete old log files
    deleteOldLogFiles("EDApplicationDimplev0*")
    
    # Go to Dimple tab
    clickTab(waitForObject(":Dimple_CTabItem"), 15, 9, 0, Button.Button1)

    copyToClipboard("/dls/sci-scratch/ExampleData/MXPipelines/dls.thaumatin.pdb")    
    # ... and paste into PDB field
    mouseClick(waitForObject(":Dimple Input Parameters.PDB file_Text_2"), 135, 11, 0, Button.Button1)
    type(waitForObject(":Dimple Input Parameters.PDB file_Text_2"), "<Ctrl+v>")

    copyToClipboard("/dls/sci-scratch/ExampleData/MXPipelines/fast_dp.mtz")    
    # ... and paste into MTZ field
    mouseClick(waitForObject(":Dimple Input Parameters.MTZ file_Text_2"), 92, 13, 0, Button.Button1)
    type(waitForObject(":Dimple Input Parameters.MTZ file_Text_2"), "<Ctrl+v>")

    clickButton(waitForObject(":Dimple Input Parameters.Get MTZ column headers_Button_2"))

    # Click button to run pipeline
    widget = findObject(":Run pipeline.Run pipeline with given parameters_Button_2")
    while not widget.enabled:
        snooze(1.0) 

    clickButton(widget)

    snooze(15.0)

    # Find the log file produced when running the pipeline
    logfile = findLogFile("EDApplicationDimplev0*", 100)
    test.verify(logfile != None, "Existence of log file")
    
    # Verify that the pipeline succeeded by checking the log file for certain key phrases 
    checkLogFile(wdir + '/' + logfile, 'Dimplev0 successful', 500)

    # The End  
    closeOrDetachFromDAWN()
