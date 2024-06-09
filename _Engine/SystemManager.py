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
        try:
            self.parent.log.getRoot().info(f"GPU: '{self.getGpu().name}'")
        except Exception as e:
            self.parent.log.getRoot().error("Could not fetch GPU")
    
    @classmethod
    def getSystem(self):
        return platform.platform()
    
    @classmethod
    def getArch(self):
        return platform.machine()
    
    @classmethod
    def getCpu(self):
        return platform.processor()
    
    @classmethod
    def getGpu(self):
        return self.computer.Win32_VideoController()[0]