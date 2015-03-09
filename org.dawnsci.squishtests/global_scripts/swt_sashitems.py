import time
#Based on swt_toolitems 

def waitForFirstSwtSashItem(timeoutMSec=20000):
    '''Search through the Sash objects in the view for one which has the focus. 
    Return that object.
    Continues searching for up to 20secs. Raises error if none found.'''
    # Keep searching until we timeout
    end = time.time() + timeoutMSec / 1000.0
    
    while time.time() < end:
        # At least wait for any Sash instance; you still may
        # need to snooze() before calling this function
        waitForObject("{isvisible='true' type='org.eclipse.swt.widgets.Sash'}")
        snooze(2)
        
        i = 0
        while True:
            n = "{isvisible='true' type='org.eclipse.swt.widgets.Sash' occurrence='" + str(i) + "'}"
            if not object.exists(n):
                break
            o = findObject(n)
            if o.focuscontrol == 1:
                return o
            i += 1
    raise LookupError('ERROR: Could not find a Sash which has the focus.')