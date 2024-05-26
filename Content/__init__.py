from Content.Objects import *
from Content.Screens import *
from Content.Scripts import *

import threading
import blessed


class GameLoop(threading.Thread):

    def __init__(self, engine):
        threading.Thread.__init__(self)
        self.parent = engine
        self.term = blessed.Terminal()
    
    def run(self):
        