import os, glob
import shutil

def deleteOldLogFiles(mask):
    logfiles = glob.glob(mask)
    for f in logfiles:
        if os.path.isdir(f):
            shutil.rmtree(f)
        else:
            os.remove(f)

def findLogFile(mask, maxiter):
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

def createAndChangeToSquishtestsTempDirectory():
    # Create, set and change to the working directory
    wdir = "/dls/tmp/squishtests"
    try:
        os.makedirs(wdir, 0777)
    except:
        pass
    os.chdir(wdir)