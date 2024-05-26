from _Engine import CacheManager
from _Engine import ContentManager
from _Engine import LanguageManager
from _Engine import LogManager
from _Engine import SaveManager
from _Engine import ServerManager
from _Engine import StateManager
from _Engine import SystemManager
from _Engine import TimeManager


import threading
import locale


class Engine(threading.Thread):

    def __init__(self, id, config):
        threading.Thread.__init__(self)
        self.id = id
        self.config = config

        self.locale = locale.getdefaultlocale()[0]
    
    
    def run(self) -> None:
        self.log = LogManager.Log(self)
        self.system = SystemManager.System(self)
        self.language = LanguageManager.Language(self)
        self.cache = CacheManager.Cache(self)
        self.time = TimeManager.Time(self)
        self.state = StateManager.State(self)
        self.content = ContentManager.Content(self)
        self.save = SaveManager.Save(self)
        self.server = ServerManager.Server(self)