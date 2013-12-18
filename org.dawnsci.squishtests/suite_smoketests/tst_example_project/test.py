source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_python_setup.py"))

def testNode(node):
    ''' Run whatever custom tests on the node you want here. Return True to iterate children '''
    try:
        nodeItemDataClassStr = str(node.item.data.getClass())
        # filter out nodes that aren't real files
        if nodeItemDataClassStr == "class org.eclipse.core.internal.resources.File":
            # Open the file
            # XXX Note specifying a coordinate here is a little wrong, a support
            # request has been sent to FrogLogic for how to best deal with double clicking
            # on an item that is partially visible  
            doubleClick(node, 5, 5, 0, Button.Button1)
            verifyAndClearErrorLog()
            activateItem(waitForObjectItem(":_Menu", "File"))
            activateItem(waitForObjectItem(":File_Menu", "Close All"))
            
            # Children of files cannot be other files, so stop iterating children
            return False
    except AttributeError:
        # If we got here it is due to node not having a resolvable class name
        pass
    return True

def iterateTestNode(node):

    ''' Recursively run testNode() on this node and all its children '''
    expand(node)
    children = object.children(node)
    runChildrenToo = testNode(node)
    if runChildrenToo:
        # Re-expand node in case the test collapsed it 
        expand(node)
        for child in children:
            iterateTestNode(waitForObject(child))

def main():
    startOrAttachToDAWN()
    #make sure all start up error produced

    setupEPDPython()

    snooze(2.0)
    # Clear the list of errors in the error log at startup    
    openAndClearErrorLog()

    # iterate over all the examples
    iterateTestNode(waitForObjectItem(":Project Explorer_Tree", "data"))

    snooze(1.0)
    
    closeOrDetachFromDAWN()
