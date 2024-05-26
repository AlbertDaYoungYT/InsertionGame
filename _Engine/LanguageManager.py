import json

class Language:
    def __init__(self, _self):
        self.__init__(_self)
        self.lang_file = json.loads(open(f"./Content/Languages/{self.locale}.json", "r").read())
    
    def text(self, id):
        return self.lang_file[id]