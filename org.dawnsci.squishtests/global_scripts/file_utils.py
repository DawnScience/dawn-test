import os, glob, shutil

def deleteOldLogFiles(mask, workingDir=None):
    if workingDir != None:
        os.chdir(workingDir)
    
    logfiles = glob.glob(mask)
    for f in logfiles:
        if os.path.isdir(f):
            shutil.rmtree(f)
        else:
            os.remove(f)

def findLogFile(mask, maxiter, workingDir=None):
    if workingDir != None:
        os.chdir(workingDir)
    
    logfiles = []
    i = 0
    while len(logfiles)==0 and i < maxiter:
        snooze(1.0)
        logfiles = glob.glob(mask)
        i += 1
        print i
        
    for f in logfiles:
        if os.path.isfile(f):
            return f
    return None

def findFileInTree(workingDir, mask, dirMasks=None):
    #Search down through a list of directory masks
    fullPath = None
    if dirMasks != None and len(dirMasks) != 0:
        os.chdir(workingDir)
        dirObjs = glob.glob(dirMasks[0])
        for obj in dirObjs:
            if os.path.isdir(obj):
                subWorkDir = os.path.join(workingDir, obj)
                fullPath = findFileInTree(subWorkDir, mask, dirMasks=dirMasks[1:])
    
    #If we're in the right place, search for the file.
    os.chdir(workingDir)
    fileObjs = glob.glob(mask)
    for obj in fileObjs:
        if os.path.isfile(obj):
            filePath = os.path.join(workingDir, obj)
            return filePath
    
    #Return the fullpath of the file
    if fullPath != None:
        return fullPath
    else:
        return None

def createAndChangeToSquishtestsTempDirectory():
    # Create, set and change to the working directory
    import os, datetime
    wdir = "/dls/tmp/"+os.environ["USER"]+"/squishtests-"+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    try:
        os.makedirs(wdir, 0777)
    except:
        pass
    os.chdir(wdir)
    return wdir

def createDirectory(parentdir, namedir):
    # Create, set and change to the working directory
    wdir = parentdir+"/"+namedir
    try:
        os.makedirs(wdir, 0777)
    except:
        pass
