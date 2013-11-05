# Adapted from:
# http://kb.froglogic.com/display/KB/Example+-+Finding+children+by+type,+occurrence+and+property+values
#/**
# * Find and return object with properties matching those
# * specified in propertiesObject.
# *
# * "obj" can be any container or child object.
# * When passing a child only the children of that child
# * are searched.
# *
# * The return value is an array with the found object
# * at index 0, and all its parents (if any), starting
# * with the closest parent. For example:
# *
# *   [aTableCellObject, aTableRowObject, aTableObject]
# *
# * Example calls:
# *
# *   o = waitForObject("{...}");
# *   path = findChildPath(o, {"text": "Kimberly"});
# *   path = findChildPath(o, {"row": "0"});
# *   path = findChildPath(o, {"row": "0", "column": "0"});
# *
# * propertiesObj can also contain "occurrence". The first
# * occurrence of an object has an occurrence value of 0.
# *
# * propertiesObj can also contain "type", just like in
# * real names. (But Squish wrapper types are not
# * supported, i.e.
# * com.froglogic.squish.swt.TreeItemProxy, etc.).
# */
def findChildPath(obj, propertiesObj):
    path = [obj];

    occurrenceCountDown = 0;
    if "occurrence" in propertiesObj:
        occurrenceCountDown = int(propertiesObj["occurrence"]);
    
    if findChildPath_impl(obj, propertiesObj, path, occurrenceCountDown):
        path.reverse()
        return path
    return None

def hasPropertiesAndValues(obj, propertiesObj):
    # If this is an item proxied by a Squish object,
    # check the actual item instead
    if (("class" in obj)
        and ("item" in obj)
        and (obj.item != null)
        and (obj["class"].indexOf("com.froglogic.") != -1)):
        obj = obj.item

    for propertyName in propertiesObj:
        # Ignore the occurrence property here (a special check
        # for that (based on our own occurrence counting) is in
        # findChildPath_impl())
        if (propertyName == "occurrence"):
            continue

        propertyValue = propertiesObj[propertyName];

        # Allow searching for "type" too, for consistency
        # with real name properties
        if (propertyName == "type"):
            if (classOrTypeName(obj) == propertyValue):
                continue
            return False

        if (not (propertyName in obj)):
            return False

        if (obj[propertyName] != propertyValue):
            return False

    return True;

def findChildPath_impl(obj, propertiesObj, path, occurrenceCountDown):
    children = object.children(obj)
    for i in xrange(children.length):
        c = children[i]
        if not hasPropertiesAndValues(c, propertiesObj):
            path.push(c)
            if (findChildPath_impl(c, propertiesObj, path, occurrenceCountDown)):
                return True

            path.pop()
            continue

        if ([occurrenceCountDown] <= 0):
            path.push(c)
            return True
  
        occurrenceCountDown[0] = occurrenceCountDown[0] - 1
        if findChildPath_impl(c, propertiesObj, path, occurrenceCountDown):
            return true

    return False

def classOrTypeName(obj):
    if ("class" in obj):
        return obj["class"]
    return typeName(obj)
