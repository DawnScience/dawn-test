source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))
source(findFile("scripts", "dawn_constants.py"))

def main():
    startOrAttachToDAWN(copy_configuration_and_p2=True)

    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Preferences"))
    doubleClick(waitForObjectItem(":Preferences_Tree", "Install/Update"))
    mouseClick(waitForObjectItem(":Preferences_Tree", "Available Software Sites"))
    table = waitForObject(":Preferences_Table")
    availableSites = table.getItems()
    # This test does not verify the entries in the available sites, but rather tests that
    # there is at least 1 and then it logs all the update sites listed.
    test.verify(availableSites.length >= 1, "There is at least one update site listed")
    for i in xrange(availableSites.length):
        site = availableSites.at(i)
        test.log("Update site %d: %s - %s" % (i, site.getText(0), site.getText(1)))

    closeOrDetachFromDAWN()
