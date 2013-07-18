def check_slider_position(slider, position, tollerence):
    range = slider.getMaximum()-slider.getMinimum()
    pos   = slider.getSelection()-slider.getMinimum()

    proportion = float(pos)/float(range)
    print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", position, proportion, range, pos
    test.verify((abs(position - proportion) < tollerence), "Slider not in expected position, expected %f and got %f" %(position, proportion))


def slide_to_propotion(slider, proportion):
    # get the bounds of the slider 
    bounds = slider.bounds
    width = bounds.width-30 # minus the width of the slider gizmo
    
    range = slider.getMaximum()-slider.getMinimum()
    start_position = slider.getSelection()-slider.getMinimum()
    
    scale = float(width)/float(range)
    
    end_position = width*proportion
    end_position = end_position - start_position*scale+15
    
    mouseDrag(slider, start_position*scale+15, 5, end_position, 5, Modifier.None, Button.Button1)
    
    # then check the position to make sure we are in the right place
    #check_slider_position(slider,proportion,0.1)
    
    
