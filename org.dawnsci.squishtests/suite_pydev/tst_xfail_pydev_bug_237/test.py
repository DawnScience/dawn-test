source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_python_setup.py"))
source(findFile("scripts", "use_case_utils.py"))

# Test for https://sw-brainwy.rhcloud.com/tracker/PyDev/237

def main():
    startOrAttachToDAWN()
    setupEPDPython()

    openPerspective("Python")
    openPyDevConsole()

    typeReturnAndWaitForPrompt()

    # Move cursor outside of editable area
    type(waitForObject(":PyDev Console"), "<Home>")
    typeInConsole("1011+2345")
    consoleText = waitForObject(":PyDev Console").text
    test.xverify("1011+2345" in consoleText, "Expected to fail until Bug 237 is resolved")

    # Move cursor outside of editable area
    typeReturnAndWaitForPrompt()
    type(waitForObject(":PyDev Console"), "<Home>")
    typeInConsole("import sys")
    consoleText = waitForObject(":PyDev Console").text
    test.verify("import sys" in consoleText, "This passes because the first character is alpha")

    # leave cursor in valid location
    typeReturnAndWaitForPrompt()
    typeInConsole("3496+1931")
    consoleText = waitForObject(":PyDev Console").text
    test.verify("3496+1931" in consoleText)

    closeOrDetachFromDAWN()

