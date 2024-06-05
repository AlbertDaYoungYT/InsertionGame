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
import sys
import os


class Engine:

    def __init__(self, id, config, *args, **kwargs):
        self.id = id
        self.config = config

        self.locale = locale.getdefaultlocale()[0]

        self.log = LogManager.Log(self, *args, **kwargs)
        self.system = SystemManager.System(self, *args, **kwargs)
        self.language = LanguageManager.Language(self, *args, **kwargs)
        self.cache = CacheManager.Cache(self, *args, **kwargs)
        self.time = TimeManager.Time(self, *args, **kwargs)
        self.state = StateManager.State(self, *args, **kwargs)
        self.content = ContentManager.Content(self, *args, **kwargs)
        self.save = SaveManager.Save(self, *args, **kwargs)
        self.server = ServerManager.Server(self, *args, **kwargs)

        self.init("./Builders/")
        self.loadPlugins()
    
    def init(self, dir):
        imported_modules = []
        current_directory = os.path.join(os.path.dirname(__file__), "./Plugins/")

        for filename in os.listdir(current_directory):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]
                importlib.import_module(f".{module_name}", package=__name__)
                imported_modules.append(module_name)

        for module in imported_modules:
            if hasattr(module, 'run') and callable(getattr(module, 'run')):
                module.run(self)

    
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
