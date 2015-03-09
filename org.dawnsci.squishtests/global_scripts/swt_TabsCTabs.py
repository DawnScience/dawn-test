import time
#Adapted from: http://kb.froglogic.com/display/KB/Example+-+Getting+CTabItem+by+text+or+tooltip+text+%28Java,+SWT%29

def waitForFirstSwtCTabItem(item_text=None, item_tooltiptext=None, timeoutMSec=20000):
    if item_text is None and item_tooltiptext is None:
        raise LookupError("ERROR: Must specify item_text or item_tooltiptext!")
 
    # Keep searching until we timeout
    end = time.time() + timeoutMSec / 1000.0
    
    while time.time() < end:
        # At least wait for any ToolBar instance; you still may
        # need to snooze() before calling this function
        waitForObject("{isvisible='true' type='org.eclipse.swt.custom.CTabFolder'}")
        
        i = 0
        while True:
            n = "{isvisible='true' type='org.eclipse.swt.custom.CTabFolder' occurrence='" + str(i) + "'}" 
            if not object.exists(n):
                break
            o = findObject(n)
            children = object.children(o)
            for c in children:
                # Ignore everything except instances of
                # com.froglogic.squish.swt.CTabProxy
                if c["class"] != "com.froglogic.squish.swt.CTabProxy":
                    continue
                item = c.item
                
                # Ignore null items
                if isNull(item):
                    continue
                
                # Ignore items that are not being shown
                # or whose parent is not visible
                if not item.showing or not item.parent.visible:
                    continue
                
                #Ignore items that don't have the label we're looking for
                if item_text is not None and item_text != item.text:
                    continue
                if item_tooltiptext is not None and item_tooltiptext != item.tooltiptext:
                    continue
                
                return c
            i += 1
    raise LookupError('ERROR: Could not find CTabItem with text "' + str(item_text) + '" and tooltiptext "' + str(item_tooltiptext) + '"')