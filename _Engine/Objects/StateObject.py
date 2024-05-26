def __init__(self, _self=None):
    self.parent = _self

def add(self, state, initial_value):
    setattr(self, state, initial_value)

def update(self, state, value):
    setattr(self, state, value)