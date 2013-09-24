source(findFile("scripts", "mx_pipelines_utils.py"))
source(findFile("scripts", "file_utils.py"))

def main():

    # This test should only run on Linux x86_64
    # use platform instead of os since os fails on windows
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
    deleteOldLogFiles("EDApplicationSCXDAPFastDPSingle*")

#   Create a data project in the Project Explorer:
    clickTab(waitForObject(":Project Explorer_CTabItem_2"), 80, 15, 0, Button.Button1)
    activateItem(waitForObjectItem(":_Menu", "File"))
    activateItem(waitForObjectItem(":File_Menu_2", "New"))
    activateItem(waitForObjectItem(":New_Menu_2", "Other..."))
    expand(waitForObjectItem(":New_Tree", "Data"))
    mouseClick(waitForObjectItem(":New_Tree", "Data Project"), 23, 7, 0, Button.Button1)
    clickButton(waitForObject(":New.Next >_Button"))
    mouseClick(waitForObject(":Directory:_Text"), 68, 14, 0, Button.Button1)
    type(waitForObject(":Directory:_Text"), "/dls/sci-scratch/ExampleData/MXPipelines")
    clickButton(waitForObject(":Browse..._Button"))
    chooseDirectory(waitForObject(":SWT"), "/dls/sci-scratch/ExampleData/MXPipelines")
    clickButton(waitForObject(":Finish_Button"))
    
    snooze(1.0)
    
    # Drill down to the files, select them and then click the "run" button
    expand(waitForObjectItem(":Project Explorer_Tree_4", "Data"))
    snooze(1.0)
    expand(waitForObjectItem(":Project Explorer_Tree_4", "data_1"))
    snooze(1.0)
    expand(waitForObjectItem(":Project Explorer_Tree_4", "diva-demo"))
    clickTab(waitForObject(":MX Data Processing_CTabItem"), 63, 15, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Project Explorer_Tree_4", "thau2__O0__K0__P0__1__0001.cbf  2.4 MB  24/10/11 05:16 PM"), 88, 12, 0, Button.Button1)
    clickButton(waitForObject(":Controls.Run Data Processing On Selected Sweep_Button_2"))

    snooze(10.0)

    # Find the log file produced when running the pipeline
    logfile = findLogFile("EDApplicationSCXDAPFastDPSingle*", 100)
    test.verify(logfile != None, "Existence of log file")

    # Verify that the pipeline succeeded by checking the log file for certain key phrases 
    checkLogFile(wdir + '/' + logfile, 'Fast_DP successful', 500)
 
    closeOrDetachFromDAWN()
