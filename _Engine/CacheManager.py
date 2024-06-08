import pickle
import uuid


class Cache:
    def __init__(self, _self, *args, **kwargs):
        self.parent = _self

        self.cache_map = {}

    def write(self, key, value):
        id = uuid.uuid1().hex
        self.cache_map[key] = id
        fo = open(f"./Data/Cache/{id}", "w")
        pickle.dump(value, fo)
        return id
    
    def read(self, key):
        id = self.cache_map[key]
        fo = open(f"./Data/Cache/{id}", "r")
        return pickle.load(fo)