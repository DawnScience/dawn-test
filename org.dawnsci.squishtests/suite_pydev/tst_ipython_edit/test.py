source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_python_setup.py"))
source(findFile("scripts", "use_case_utils.py"))
import shutil
import tempfile
import os

def getTestDataAsTemp(filename):
    # should really be NamedTemporaryFile, not available with Delete=False in Python 2.4
    prefix, suffix = filename.rsplit('.', 2)
    handle, path = tempfile.mkstemp(suffix="." + suffix, prefix=prefix)
    os.close(handle)
    in_path = findFile("testdata", filename)
    in_path = os.path.abspath(in_path)
    shutil.copy(in_path, path)
    return path


def testEditTemp():
    waitForPrompt()
    # don't wait for a prompt, it does not arrive
    typeInConsole("%edit", wait=False)
    # give the editor time to open
    snooze(3)
    # We are using nativeType here to ensure that the %edit flow sets the focus properly
    # i.e. %edit should pop up an editor with focus and when we save and close
    # it should return to the console
    nativeType('print "Kichwa Was Here"') # code in editor
    nativeType("<Ctrl+s>") # save editor
    nativeType("<Ctrl+w>") # close editor
    nativeType("<Return>") # tell IPython we are done, this causes code to execute
    waitForPrompt()

    # now make sure that our code was run
    consoleText = waitForObject(":PyDev Console").text
    test.verify("IPython will make a temporary file named" in consoleText)
    test.verify("Executing edited code" in consoleText)
    test.verify("Kichwa Was Here" in consoleText)

    # and leave console clean state for next test
    typeReturnAndWaitForPrompt()

def testEditExisting():
    waitForPrompt()

    path = getTestDataAsTemp("edit_ipython_1.py")

    # don't wait for a prompt, it does not arrive
    typeInConsole("%edit '''" + path + "'''", wait=False)
    # give the editor time to open
    snooze(3)
    # We are using nativeType here to ensure that the %edit flow sets the focus properly
    # i.e. %edit should pop up an editor with focus and when we save and close
    # it should return to the console
    nativeType('print "Before Message"') # code in editor
    nativeType('<Return>') # code in editor
    nativeType("<Ctrl+s>") # save editor
    nativeType("<Ctrl+w>") # close editor
    nativeType("<Return>") # tell IPython we are done, this causes code to execute
    waitForPrompt()

    # now make sure that our code was run
    consoleText = waitForObject(":PyDev Console").text
    test.verify("Editing..." in consoleText)
    test.verify("Executing edited code" in consoleText)
    test.verify("Before Message\nKichwa Was Here Too" in consoleText)

    # and leave console clean state for next test
    typeReturnAndWaitForPrompt()

    # cleanup
    os.unlink(path)


def testEditLineNumber():
    waitForPrompt()
    path = getTestDataAsTemp("edit_ipython_2.py")

    # don't wait for a prompt, it does not arrive
    typeInConsole("%edit -n 2 '''" + path + "'''", wait=False)
    # give the editor time to open
    snooze(3)
    # We are using nativeType here to ensure that the %edit flow sets the focus properly
    # i.e. %edit should pop up an editor with focus and when we save and close
    # it should return to the console
    nativeType('print "Replaced Line 2"') # code in editor
    nativeType('<Return>') # code in editor
    nativeType("<Ctrl+s>") # save editor
    nativeType("<Ctrl+w>") # close editor
    nativeType("<Return>") # tell IPython we are done, this causes code to execute
    waitForPrompt()

    # now make sure that our code was run
    consoleText = waitForObject(":PyDev Console").text
    test.verify("Editing..." in consoleText)
    test.verify("Executing edited code" in consoleText)
    test.verify("Line 1\nReplaced Line 2\nLine 3" in consoleText)

    # and leave console clean state for next test
    typeReturnAndWaitForPrompt()

    # cleanup
    os.unlink(path)

def main():
    startOrAttachToDAWN()
    setupPython()

    openPerspective("Python")
    openPyDevConsole()

    testEditTemp()
    testEditExisting()
    testEditLineNumber()

    closeOrDetachFromDAWN()
