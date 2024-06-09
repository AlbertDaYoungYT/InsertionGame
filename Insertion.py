import configparser
import uuid
import json
import glob
import sys
import os


import _Engine as Engine

# Config Vars
c = configparser.ConfigParser()
c.read('Insertion.ini')

if c["DEFAULT"]["MachineID"] == "":
    c["DEFAULT"] = {"MachineID": uuid.uuid1().hex}
    with open('Insertion.ini', 'w') as configfile:
        c.write(configfile)

# Environment Vars
os.environ["INSERTION_HOME"] = os.path.dirname(os.path.realpath(__file__))

# Flags
devMode = True if "--dev-mode" in sys.argv else False
buildFlag = True if "--build" in sys.argv else False
purgeLogs = True if "--purge-logs" in sys.argv else False
checksumIgnore = True if "--ignore-checksum" in sys.argv else False

# Json Parsing
EngineJSON      = json.load(open("Data/Engine.json", "r"))
SettingsJSON    = json.load(open("Data/Settings.json", "r"))

# Pre Initialization Checks
# Checksum Check
if EngineJSON["checksum"] == None or checksumIgnore:
    EngineJSON["checksum"] = Engine.Builtin.Checksum.checksumDirectory("_Engine/")
else:
    if EngineJSON["checksum"] != Engine.Builtin.Checksum.checksumDirectory("_Engine/"): raise(Engine.Errors.EngineExceptions.ChecksumError("Checksum of Engine doesn't match"))


# Purge Checks
if purgeLogs: 
    files = glob.glob('Data/Logs/*.log')
    for f in files:
        os.remove(f)


engine = Engine.Engine(c["DEFAULT"]["MachineID"], c, engineJson=EngineJSON)
engine.log.getRoot().info("Engine Imported")

import platform
import time



# Game Engine Initialization
engine.log.getRoot().info("Game Engine Initialization Starting...")
EngineJSON["build"] += 1 if devMode else 0


while engine.engineRunning:
    try:
        try:
            while True:
                engine.update()
        except Exception as e:
            if e == KeyboardInterrupt:
                engine.log.getRoot().warning("Keyboard Interrupt Detected!")
                if engine.lockKeyboardInterrupts and engine.interruptCallback == None:
                    engine.log.getRoot().info("Ignoring Interrupt...")
                elif engine.interruptCallback != None:
                    try:
                        engine.interruptCallback(e)
                    except Exception as e:
                        engine.log.getRoot().error("Error while Handling Interrupt, choosing priority...")
                        if engine.interruptFallbackOption == 1:
                            engine.log.getRoot().info("Engine is Shutting Down...")
                            engine.stop()
                        elif engine.interruptFallbackOption == 2:
                            engine.log.getRoot().warning("Engine ignoring Interrupt Error.")
                        else:
                            engine.log.getRoot().info("No priority set, ignoring options and unpausing Engine...")
                    finally:
                        engine.log.getRoot().info("Interrupt Handled by Callback")

                else:
                    engine.log.getRoot().info("Engine lockKeyboardInterrupts property is disabled.")
                    engine.log.getRoot().info("Engine is Shutting Down...")
                    engine.stop()
            else:
                engine.log.getRoot().warning(f"Engine threw error: '{e.with_traceback(None)}'")
    except Exception as e:
        engine.log.getRoot().error(f"ENGINE EXITED WITH ERROR: '{e.with_traceback(None)}'")
        engine.stop()


open("Data/Engine.json", "w").write(json.dumps(EngineJSON))
open("Data/Settings.json", "w").write(json.dumps(SettingsJSON))