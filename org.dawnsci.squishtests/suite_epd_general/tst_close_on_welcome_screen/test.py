source(findFile("scripts", "utilities.py"))

# This test makes sure we can close the DAWN even while the
# welcome screen is open.
# At the time of writing this test is XFAIL because
# the Intro Logo Animation seems to interfere with the
# normal SWT event loop. As a result, even if you press
# the close window, the confirm exit doesn't come up
# until the welcome window is close
# On further examination this looks related to the intro
# logo animation putting in thousands of asyncExec messages
# that sit in the queue waiting to run. 
def main():
    startOrAttachToDAWNOnly()
    
    # make sure we have the welcome window
    waitForObject(":Welcome_CTabItem")
    
    # Wait for a few seconds (This allows async message queue to build up a bit)
    snooze(3.0)
    
    # Now with the welcome open, close DAWN
    closeWindow(":Workbench Window")
    
    # Wait for the confirm exit, it won't appear
    # and this is the XFAIL
    waitForObject(":Confirm Exit.OK_Button")
    
    # Once the code is fixed, this should be reachable
    clickButton(waitForObject(":Confirm Exit.OK_Button"))

