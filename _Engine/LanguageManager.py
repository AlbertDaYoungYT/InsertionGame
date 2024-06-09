import locale
import json

class Language:

    lang_file = json.loads(open(f"./Content/Languages/{locale.getdefaultlocale()[0]}.json", "r").read())

    def __init__(self, _self, *args, **kwargs):
        self.parent = _self
    
    @classmethod
    def text(cls, id):
        return cls.lang_file[id]