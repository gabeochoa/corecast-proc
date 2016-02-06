
import os
import sys
import hashlib

def filehash(filepath, blocksize=4096):
    """ Return the hash hexdigest for the file `filepath', processing the file
    by chunk of `blocksize'.
    :type filepath: str
    :param filepath: Path to file
    :type blocksize: int
    :param blocksize: Size of the chunk when processing the file
    """
    sha = hashlib.sha256()
    with open(filepath, 'rb') as fp:
        while 1:
            data = fp.read(blocksize)
            if data:
                sha.update(data)
            else:
                break
    return sha.hexdigest()

from datetime import datetime
def backupfile(fn):
    if os.path.exists(fn):
        newfn = str(datetime.utcnow()) + fn
        if not os.path.exists(newfn):
            

def processNewFile(fn):
    print("Processing " + fn)

def main():
        old = open('oldfiles.config', 'r').read().split("\n")
        backupfile("SIH.xml")
        f = open('SIH.xml', 'r').read()
        i=0
	allfiles = os.listdir("audio")
	for filename in allfiles:
		fn = os.getcwd() +'/audio/' + filename
		size = (os.path.getsize(fn))
		newhash = filehash(fn)
                if newhash != old[i]:
                    #print("not same")
                    #print(filename)
                    processNewFile(filename)
                i+=1
main()
