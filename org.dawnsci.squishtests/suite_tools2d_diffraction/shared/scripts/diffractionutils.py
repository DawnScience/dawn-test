def getBeamCentreFromTable(tree):
    first = tree.getItems()
    
    x = ""
    y = ""
    
    for i in range(first.length):
        node = first.at(i)
        if ("Detector" in node.getText()):
            second = node.getItems()
    
            for i in range(second.length):
                node2 = second.at(i)
        
                if ("Beam Centre" in node2.getText()):
                    third = node2.getItems()
                    x = third.at(0)
                    x = object.children(third.at(0))[2].getText()
                    y = object.children(third.at(1))[2].getText()
                    
                    return x,y
    
    test.fail("failed to get beam centre from table")         
    return x,y