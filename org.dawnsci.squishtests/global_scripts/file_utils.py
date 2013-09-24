import os, glob
import shutil

def deleteOldLogFiles(mask):
    logfiles = glob.glob(mask)
    for f in logfiles:
        if os.path.isdir(f):
            shutil.rmtree(f)
        else:
            os.remove(f)
