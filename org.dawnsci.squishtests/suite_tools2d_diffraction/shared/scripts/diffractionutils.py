def getBeamCentreFromTable():
    expand(waitForObjectItem(":Diffraction_Tree_2", "Detector"))
    expand(waitForObjectItem(":Diffraction_Tree_2", "Beam Centre"))
    centre = waitForObjectItem(":Diffraction_Tree_2", "Beam Centre").getItems()
    x = centre.at(0)
    x = object.children(centre.at(0))[2].getText()
    y = object.children(centre.at(1))[2].getText()      
    return x,y