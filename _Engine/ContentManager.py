import importlib


class Content:

    def __init__(self, _self):
        self.__init__(_self)

        self.content_hierarchy = []
        importlib.import_module("Content.DLCs")