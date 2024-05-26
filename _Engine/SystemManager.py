import platform
import sys
import os


class System:

    def __init__(self, _self):
        self.parent = _self

        self.addon_location = "./Content/Addons/"
        self.dlc_location = "./Content/DLCs/"
        self.language_location = "./Content/Languages/"

        self.cache_location = "./Data/Cache/"
        self.log_location = "./Data/Logs/"
        self.save_location = "./Data/Saves/"

    
    def getSystem(self):
        return platform.system()
    
    def getArch(self):
        return platform.uname()[-2]