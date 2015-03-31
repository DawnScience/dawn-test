''' Module to provide interactions with SWT widgets in one place. Similar
    to the methods provided by other swt_* modules (ctabitems, tableitems...)
    Sourced by dawn_global_ui_controls.
    '''

def waitForSwtTextWithLabel(labelText, timeoutMSec=20000):
    
    # Keep searching until we timeout
    end = time.time() + timeoutMSec / 1000.0
    
    while time.time() < end:
        waitForObject("{isvisible='true' type='org.eclipse.swt.widgets.Text'}")
#        snooze(2) #May or may not be needed...
        
        i = 0
        while True:
            #Get a Text object
            n = "{isvisible='true' type='org.eclipse.swt.widgets.Text' occurrence='" + str(i) + "'}"
            if not object.exists(n):
                break
            textField = findObject(n)
            
            #Get the children of the composite in which the Text resides
            container = object.parent(textField)
            children = object.children(container)
            
            #Find the label associated with the Text and check if it is the right one
            for child in children:
                if child['class'] != 'org.eclipse.swt.widgets.Label':
                     continue
                 
                if child.text == labelText:
                    return textField
                
            i += 1
    
    raise LookupError('ERROR: Could not find SWT.Text with label "' + str(labelText) + '"')

def waitForSwtGroupWithLabel(labelText):
    
    '''Tool to get the group container object.
       WARNING: This will probably not work on squish-5.1 or higher!
       '''
    groupObj = waitForObject("{caption='"+labelText+"' parent.visible='true' type='org.eclipse.swt.widgets.Group'}")
    snooze(2)
    return groupObj
