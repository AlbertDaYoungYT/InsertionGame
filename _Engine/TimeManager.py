import threading
import time
import uuid


class Time:
    def __init__(self, _self, *args, **kwargs):
        self.parent = _self
        self.stopwatches = {}
    
    def startStopwatch(self):
        id = uuid.uuid1().hex
        self.stopwatches[id] = time.time()
        return id
    
    def lapStopwatch(self, id):
        t = time.time() - self.stopwatches[id]
        self.stopwatches[id] = time.time()
        return t
    
    def stopStopwatch(self, id):
        t = time.time() - self.stopwatches[id]
        del self.stopwatches[id]
        return t
    
    def createTimer(self, end, callback):
        return threading.Timer(end, callback)