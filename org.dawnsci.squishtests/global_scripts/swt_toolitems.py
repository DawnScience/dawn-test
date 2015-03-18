import time
# Adapted from http://kb.froglogic.com/display/KB/Article+-+Avoiding+problems+with+ToolItems+in+RCP+and+SWT+applications

def waitForFirstSwtToolItem(item_tooltiptext=None, item_text=None, timeoutMSec=20000):
    if item_text is None and item_tooltiptext is None:
        raise LookupError("ERROR: Must specify item_text or item_tooltiptext!")
 
    # Keep searching until we timeout
    end = time.time() + timeoutMSec / 1000.0
    
    while time.time() < end:
        # At least wait for any ToolBar instance; you still may
        # need to snooze() before calling this function
        waitForObject("{isvisible='true' type='org.eclipse.swt.widgets.ToolBar'}")
     
        i = 0
        while True:
            n = "{isvisible='true' type='org.eclipse.swt.widgets.ToolBar' occurrence='" + str(i) + "'}"
            if not object.exists(n):
                break
            o = findObject(n)
            children = object.children(o)
            for c in children:
                if item_text is not None and item_text != c.text:
                    continue
                if item_tooltiptext is not None and item_tooltiptext != c.tooltiptext:
                    continue                
                return c
            i += 1
    raise LookupError('ERROR: Could not find ToolItem with text "' + str(item_text) + '" and tooltiptext "' + str(item_tooltiptext) + '"')