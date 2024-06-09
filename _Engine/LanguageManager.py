import json

class Language:
    def __init__(self, _self, *args, **kwargs):
        self.parent = _self
        self.lang_file = json.loads(open(f"./Content/Languages/{self.parent.locale}.json", "r").read())
    
    @classmethod
    def text(cls, id):
        return cls.lang_file[id]