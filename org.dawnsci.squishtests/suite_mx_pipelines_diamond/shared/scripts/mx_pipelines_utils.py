source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))
#source(findFile("scripts", "dawn_global_plot_tests.py"))

import platform, sys, os, glob
import shutil

def setPort(port):
    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Preferences"))
    expand(waitForObjectItem(":Preferences_Tree", "DAWN"))
    mouseClick(waitForObjectItem(":Preferences_Tree", "Web services"), 26, 12, 0, Button.Button1)
    setValue(waitForObject(":Localhost web service ports range (only one port will be used)_Spinner"), port)
    clickButton(waitForObject(":Preferences.OK_Button"))

def setDirectories(wdir):
    # Type in path in feedback field, copy to clipboard
    activateItem(waitForObjectItem(":_Menu", "Help"))
    activateItem(waitForObjectItem(":Help_Menu_2", "Leave Feedback"))
    mouseClick(waitForObject(":Feedback.Comment_Text_2"), 204, 53, 0, Button.Button1)
    type(waitForObject(":Feedback.Comment_Text_2"), wdir)
    type(waitForObject(":Feedback.Comment_Text_2"), "<Ctrl+a>")
    type(waitForObject(":Feedback.Comment_Text_2"), "<Ctrl+c>")
    
    mouseClick(waitForObject(":Localhost web service directories.Working directory_Text_2"), -172, 9, 0, Button.Button1)
    type(waitForObject(":Localhost web service directories.Working directory_Text_2"), "<Ctrl+a>")
    type(waitForObject(":Localhost web service directories.Working directory_Text_2"), "<Ctrl+v>")
    mouseClick(waitForObject(":Localhost web service directories.Result directory_Text_2"), -265, 12, 0, Button.Button1)
    type(waitForObject(":Localhost web service directories.Result directory_Text_2"), "<Ctrl+a>")
    type(waitForObject(":Localhost web service directories.Result directory_Text_2"), "<Ctrl+v>")

# Check the log file first for "EDNA Bottle status" line which indicates the pipeline has finished. 
# Then search for the success message
def checkLogFile(filename, success, maxiter=1000):
    i = -1
    x = 0
    print filename
    while i == -1 and x < maxiter:
        snooze(1.0)
        fsize = os.path.getsize(filename)
        if fsize < 1000:
            seeklen = fsize
        else:
            seeklen = 1000

        f = file(filename, 'rb')
        f.seek(-seeklen, 2) # 2 is the value of os.SEEK_END
        tail = str(f.read(seeklen))
        f.close()
        i = tail.find("EDNA Bottle status")
        x += 1
        print i

    test.verify(i >= 0, "Pipeline finished")
    j = tail.find(success) # 'MXv1 characterisation successful'
    test.verify(j >= 0, "Pipeline succeeded")
    if j >= 0:
        return True
    return False

def copyToClipboard(text):
    activateItem(waitForObjectItem(":_Menu", "Help"))
    activateItem(waitForObjectItem(":Help_Menu_2", "Leave Feedback"))
    mouseClick(waitForObject(":Feedback.Comment_Text_2"), 80, 29, 0, Button.Button1)
    type(waitForObject(":Feedback.Comment_Text_2"), "<Ctrl+a>")
    type(waitForObject(":Feedback.Comment_Text_2"), "<Ctrl+x>")
    type(waitForObject(":Feedback.Comment_Text_2"), text)
    type(waitForObject(":Feedback.Comment_Text_2"), "<Ctrl+a>")
    type(waitForObject(":Feedback.Comment_Text_2"), "<Ctrl+c>")
