
from dataclasses import dataclass
import queue

class Game:

    class Callbacks:

        def SaveCallback(args):
            return None


    def __init__(self, _self):
        self.parent = _self

        self.register = {}
        self.queue = queue.Queue()

    
    def preload(self, k):
        loads = self.register["Worlds"][k]
        return self.parent.cache.write(k, loads)
    
    def load(self, k):
        return self.parent.cache.read(k)
    
    def update(self):
