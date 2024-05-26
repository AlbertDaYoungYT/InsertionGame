import logging
import os
from datetime import datetime

class Log:
    def __init__(self, _self):
        self.parent = _self

        self.root_logger = logging.getLogger()
        self.root_logger.setLevel(logging.INFO)

        self.module_logger = logging.getLogger(__name__)
        self.module_logger.setLevel(logging.DEBUG)
        self.module_logger.propagate = False
        
        log_directory = "./Data/Logs/"
        os.makedirs(log_directory, exist_ok=True)
        log_filename = os.path.join(log_directory, f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

        if not self.root_logger.handlers:
            fh = logging.FileHandler(log_filename)
            fh.setFormatter(logging.Formatter("%(asctime)s [pid %(process)d] %(levelname)s %(module)s.%(funcName)s():%(lineno)d - %(name)s: %(message)s"))
            self.root_logger.addHandler(fh)
            self.module_logger.addHandler(fh)
    
    def getModule(self):
        return self.module_logger

    def getRoot(self):
        return self.root_logger
