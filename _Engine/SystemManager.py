import platform
import logging
import sys
import wmi
import os


class System:

    def __init__(self, _self, *args, **kwargs):
        self.parent = _self
        self.computer = wmi.WMI()

        self.parent.log.getRoot().info(f"Running on '{self.getSystem()}:{self.getArch()}'")
        self.parent.log.getRoot().info(f"GPU: '{self.getGpu().name}'")
    
    def getSystem(self):
        return platform.platform()
    
    def getArch(self):
        return platform.machine()
    
    def getCpu(self):
        return platform.processor()
    
    def getGpu(self):
        return self.computer.Win32_VideoController()[0]