from _Engine import CacheManager
from _Engine import LanguageManager
from _Engine import LogManager
from _Engine import SaveManager
from _Engine import ServerManager
from _Engine import StateManager
from _Engine import SystemManager
from _Engine import TimeManager

from _Engine.Event import Event

from _Engine.Builders import *
from _Engine.Builtin import *
from _Engine.Errors import *
from _Engine.Objects import *
from _Engine.Plugins import *


import importlib
import threading
import logging
import locale
import queue
import sys
import os


class Engine:

    def __init__(self, id, config, *args, **kwargs):
        self.id = id
        self.config = config

        self.locale = locale.getdefaultlocale()[0]

        self.log = LogManager.Log(self, *args, **kwargs)
        self.log.getRoot().info(f"Inception Engine {kwargs["engineJson"]['version']}.{kwargs["engineJson"]['build']} tag:{kwargs["engineJson"]['tag']} ")

        # Declare Event 
        self.eventEngineUpdate = Event("eventEngineUpdate")
        self.eventEnginePause = Event("eventEnginePause")
        self.eventEngineUnPause = Event("eventEngineUnPause")
        self.eventEngineShutdown = Event("eventEngineShutdown")
        self.eventEngineRaiseError = Event("eventEngineRaiseError")

        # Import Engine Managers
        self.system = SystemManager.System(self, *args, **kwargs)
        self.language = LanguageManager.Language(self, *args, **kwargs)
        self.cache = CacheManager.Cache(self, *args, **kwargs)
        self.time = TimeManager.Time(self, *args, **kwargs)
        self.state = StateManager.State(self, *args, **kwargs)
        self.save = SaveManager.Save(self, *args, **kwargs)
        self.server = ServerManager.Server(self, *args, **kwargs)



        self.args = args
        self.kwargs = kwargs

        self.initDir("Builders")
        self.loadPlugins()
        
        # Non Editable Engine Properties
        self.engineThreadQueue = queue.Queue()
        self.engineRunning = True
        self.engineTimeout = self.time.schedule(1, self.timeout)
        self.engineStep = 0
        self.firstRun = True
        self.currentScene = None

        # Editable Engine Properties
        self.interruptCallback = None
        self.lockKeyboardInterrupts = False
        self.interruptFallbackOption = 0 # 0: Nothing, 1: Exit, 2: Ignore

        # Engine Starts
        self.engineTimeout.start()
    
    def preload(self, name, asset):
        self.__setattr__(name, asset(self, *self.args, **self.kwargs))
    
    def initDir(self, dir):
        self.log.getRoot().info(f"Intiating Engine Directory '{dir}'...")
        imported_modules = []
        current_directory = os.path.join(os.path.dirname(__file__), dir)

        for filename in os.listdir(current_directory):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]
                importlib.import_module(f".{dir}.{module_name}", package=__name__)
                imported_modules.append(module_name)

        for module in imported_modules:
            if hasattr(module, 'run') and callable(getattr(module, 'run')):
                module.run(self)

    
    def loadPlugins(self):
        self.log.getRoot().info(f"Loading Engine Plugins...")
        imported_modules = []
        current_directory = os.path.join(os.path.dirname(__file__), "./Plugins/")

        for filename in os.listdir(current_directory):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]
                try:
                    importlib.import_module(f".Plugins.{module_name}", package=__name__)
                    imported_modules.append(module_name)
                except Exception as e:
                    self.log.getRoot().warning(f"Plugin '{module_name}' encountered an error while loading: '{e}'")

        for module in imported_modules:
            if hasattr(module, 'load') and callable(getattr(module, 'load')):
                module.load(self)

    def set(self, key, value):
        self.__setattr__(key, value)
    
    def get(self, key):
        return self.__getattribute__(key)
    
    def timeout(self):
        self.log.getRoot().warning("Engine Timeout Triggered!")
        self.engineRunning = False

    def stop(self):
        self.engineRunning = False
    

    def changeScene(self, scene):
        self.log.getRoot().info("Scene changing...")
        self.currentScene = scene
        self.currentScene.show()
    
    def update(self):
        self.engineStep += 1
        if self.firstRun: 
            self.firstRun = False
            self.log.getRoot().info("Engine is Running...")
        
        if self.currentScene != None:
            self.engineTimeout.cancel()
            self.currentScene.setParent(self)
            self.currentScene.update()
        
        if self.engineRunning == False: raise EngineExceptions.EngineRuntimeError("Engine Stopped in Runtime")


