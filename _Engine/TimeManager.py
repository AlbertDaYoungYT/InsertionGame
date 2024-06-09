import threading
import queue
import time
import uuid


class Time:
    def __init__(self, _self, *args, **kwargs):
        self.parent = _self
        self.stopwatches = {}
    
    @classmethod
    def startStopwatch(cls):
        id = uuid.uuid1().hex
        cls.stopwatches[id] = time.time()
        return id
    
    @classmethod
    def lapStopwatch(cls, id):
        t = time.time() - cls.stopwatches[id]
        cls.stopwatches[id] = time.time()
        return t
    
    @classmethod
    def stopStopwatch(cls, id):
        t = time.time() - cls.stopwatches[id]
        del cls.stopwatches[id]
        return t
    
    @classmethod
    def schedule(cls, end, callback):
        return threading.Timer(end, callback)