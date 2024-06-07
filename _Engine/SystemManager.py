import platform
import sys
import os


class System:

    def __init__(self, _self):
        self.parent = _self
        
    
    def getSystem(self):
        return platform.system()
    
    def getArch(self):
        return platform.uname()[-2]