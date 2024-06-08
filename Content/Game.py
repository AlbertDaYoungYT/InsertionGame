
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

    
    def preload(self, map, k, i):
        loads = self.register[k][i]
        return self.parent.cache.write(map, loads)
    
    def load(self, map):
        return self.parent.cache.read(map)
    
    def update(self):
        pass