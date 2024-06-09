
import queue

class Game:

    def __init__(self, _self):
        self.parent = _self

        self.queue = queue.Queue()

    
    def preload(self, map, k, i):
        loads = self.register[k][i]
        return self.parent.cache.write(map, loads)
    
    def load(self, map):
        return self.parent.cache.read(map)
    
    def update(self):
        pass