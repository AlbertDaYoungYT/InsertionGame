import pickle
import uuid


class Cache:
    def __init__(self, _self, *args, **kwargs):
        self.parent = _self

        self.cache_map = {}

    @classmethod
    def write(cls, key, value):
        id = uuid.uuid1().hex
        cls.cache_map[key] = id
        fo = open(f"./Data/Cache/{id}", "w")
        pickle.dump(value, fo)
        return id
    
    @classmethod
    def read(cls, key):
        id = cls.cache_map[key]
        fo = open(f"./Data/Cache/{id}", "r")
        return pickle.load(fo)