from _Engine import CacheManager
from _Engine import LanguageManager
from _Engine import LogManager
from _Engine import SaveManager
from _Engine import ServerManager
from _Engine import StateManager
from _Engine import SystemManager
from _Engine import TimeManager

from _Engine.Builders import *
from _Engine.Builtin import *
from _Engine.Errors import *
from _Engine.Objects import *
from _Engine.Plugins import *


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
        self.save = SaveManager.Save(self, *args, **kwargs)
        self.server = ServerManager.Server(self, *args, **kwargs)

        self.args = args
        self.kwargs = kwargs

        self.initDir("_Engine/Builders/")
        self.loadPlugins()
    
    def preload(self, name, asset):
        self.__setattr__(name, asset(self, *self.args, **self.kwargs))
    
    def initDir(self, dir):
        imported_modules = []
        current_directory = os.path.join(os.path.dirname(__file__), dir)

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

    def set(self, key, value):
        self.__setattr__(key, value)
    
    def get(self, key):
        return self.__getattribute__(key)