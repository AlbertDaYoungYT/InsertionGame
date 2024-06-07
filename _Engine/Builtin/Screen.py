import blessed

class Screen(object):
    def __init__(self):
        self.terminal = blessed.Terminal()
    
        self.display_chain = []

    
    def update(self):
        pass


class StartLoading:

    def __init__(self):
        self.terminal = blessed.Terminal()
    
        self.display_chain = [
            []
        ]
    
    def draw(self):
        