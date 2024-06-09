import threading
import queue
import time
import uuid


class Time:
    def __init__(self, _self, *args, **kwargs):
        self.parent = _self
        self.stopwatches = {}
    
    @classmethod
    def startStopwatch(self):
        id = uuid.uuid1().hex
        self.stopwatches[id] = time.time()
        return id
    
    @classmethod
    def lapStopwatch(self, id):
        t = time.time() - self.stopwatches[id]
        self.stopwatches[id] = time.time()
        return t
    
    @classmethod
    def stopStopwatch(self, id):
        t = time.time() - self.stopwatches[id]
        del self.stopwatches[id]
        return t
    
    @classmethod
    def schedule(self, end, callback):
        return threading.Timer(end, callback)