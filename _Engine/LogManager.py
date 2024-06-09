import logging
import sys
import os
from datetime import datetime

class Log:
    _root_logger = logging.getLogger("engine")
    _root_logger.setLevel(logging.INFO)
    _root_logger.propagate = False

    _module_logger = logging.getLogger(__name__)
    _module_logger.setLevel(logging.DEBUG)
    _module_logger.propagate = False

    def __init__(self, _self, *args, **kwargs):
        self.parent = _self
        
        log_directory = "./Data/Logs/"
        os.makedirs(log_directory, exist_ok=True)
        log_filename = os.path.join(log_directory, f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

        fh = logging.FileHandler(log_filename)
        fh.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(funcName)s():%(lineno)d: %(message)s"))
        Log._root_logger.addHandler(fh)
        Log._module_logger.addHandler(fh)
    
    @classmethod
    def getModule(cls):
        return cls._module_logger

    @classmethod
    def getRoot(cls):
        return cls._root_logger
