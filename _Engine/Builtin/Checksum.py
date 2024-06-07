import hashlib
import os


def checksum(file: str):
    return hashlib.md5(file.encode()+open(file,'rb').read()).hexdigest()

def checksumDirectory(dir):
    list = []
    for filename in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, filename)):
            checksumDirectory(os.path.join(dir, filename))
        else:
            list.append(checksum(os.path.join(dir, filename)))
    
    return hashlib.md5(''.join(list).encode()).hexdigest()