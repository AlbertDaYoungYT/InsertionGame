import blessed



class Intro:
    def __init__(self, term):
        self.parent = None
        self.term = term

        self.frameCounter = 0
        self.length = None
    
    def setParent(self, _self):
        self.parent = _self

    def show(self):
        
    def update(self):