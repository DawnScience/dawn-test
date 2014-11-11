source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_python_setup.py"))

# We test that GUI integration is working, however Squish can't
# test an externally launched GUI, so instead we use the
# GUI event loop to generate messages on stdout we can see
# and test for

def main():
    startOrAttachToDAWN()
    setupPython()

    openPyDevConsole()
    
    # First, run with no GUI Event loop working
    typeInConsole("import sys")
    typeInConsole("import wx")
    typeInConsole("app = wx.App(redirect=False, clearSigInt=False)")
    typeInConsole("timer = wx.Timer()")
    typeInConsole("app.Bind(wx.EVT_TIMER, lambda e: sys.stdout.write('in event\\n'), timer)")
    typeInConsole("timer.Start(100, True)")
    
    # now run for a few seconds and make sure that we don't
    # see 'in event'
    snooze(3)
    typeReturnAndWaitForPrompt()

    test.verify('in event\n' not in waitForObject(":PyDev Console", 15000).text, 'verify event not run')
    
    # Now turn on event loop and make sure we get the expected
    # output
    typeInConsole("%gui wx")
    snooze(3)
    typeReturnAndWaitForPrompt()
    test.verify('in event\n' in waitForObject(":PyDev Console", 15000).text, 'verify event run')
    
    closeOrDetachFromDAWN()
