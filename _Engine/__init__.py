from _Engine import CacheManager
from _Engine import ContentManager
from _Engine import LanguageManager
from _Engine import LogManager
from _Engine import SaveManager
from _Engine import ServerManager
from _Engine import StateManager
from _Engine import SystemManager
from _Engine import TimeManager


import importlib
import threading
import locale
import os


class Engine:

    def __init__(self, id, config):
        self.id = id
        self.config = config

        self.locale = locale.getdefaultlocale()[0]

        self.log = LogManager.Log(self)
        self.system = SystemManager.System(self)
        self.language = LanguageManager.Language(self)
        self.cache = CacheManager.Cache(self)
        self.time = TimeManager.Time(self)
        self.state = StateManager.State(self)
        self.content = ContentManager.Content(self)
        self.save = SaveManager.Save(self)
        self.server = ServerManager.Server(self)

        self.loadPlugins()
    
    def loadPlugins(self):
        imported_modules = []
        current_directory = os.path.join(os.path.dirname(__file__), "./Plugins/")

        for filename in os.listdir(current_directory):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]
                importlib.import_module(f".{module_name}", package=__name__)
                imported_modules.append(module_name)

        for module in imported_modules:
            if hasattr(module, 'load') and callable(getattr(module, 'load')):
                module.load(self)
