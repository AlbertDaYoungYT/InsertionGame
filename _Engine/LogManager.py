import logging


class Log:

    def __init__(self, _self):
        self.__init__(_self)
        self.root_logger = logging.getLogger()
        self.root_logger.setLevel(logging.INFO)

        self.module_logger = logging.getLogger(__name__)
        self.module_logger.setLevel(logging.DEBUG)
        
        fh = logging.FileHandler("./Data/Logs/%(asctime)s.log")
        fh.setFormatter(logging.Formatter("%(asctime)s [pid %(process)d] %(levelname)s %(module)s.%(funcName)s():%(lineno)d - %(name)s: %(message)s"))
        self.root_logger.addHandler(fh)
        self.module_logger.addHandler(fh)
    
    def getModule(self):
        return self.module_logger

    def getRoot(self):
        return self.root_logger