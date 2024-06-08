import platform
import logging
import sys
import os


class System:

    def __init__(self, _self, *args, **kwargs):
        self.parent = _self

        logging.info(f"Running on '{self.getSystem()}:{self.getArch()}'")
    
    def getSystem(self):
        return platform.system()
    
    def getArch(self):
        return platform.uname()[-2]