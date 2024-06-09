import platform
import logging
import sys
import wmi
import os


class System:
    
    computer = wmi.WMI()

    def __init__(self, _self, *args, **kwargs):
        self.parent = _self

        self.parent.log.getRoot().info(f"Running on '{self.getSystem()}:{self.getArch()}'")
        try:
            self.parent.log.getRoot().info(f"GPU: '{self.getGpu().name}'")
        except Exception as e:
            self.parent.log.getRoot().error("Could not fetch GPU")
    
    @classmethod
    def getSystem(cls):
        return platform.platform()
    
    @classmethod
    def getArch(cls):
        return platform.machine()
    
    @classmethod
    def getCpu(cls):
        return platform.processor()
    
    @classmethod
    def getGpu(cls):
        return cls.computer.Win32_VideoController()[0]