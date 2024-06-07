import configparser
import platform
import logging
import uuid
import time
import json
import glob
import sys
import os

# Json Parsing
EngineJSON      = json.load(open("Data/Engine.json", "r"))
SettingsJSON    = json.load(open("Data/Settings.json", "r"))

# Environment Vars
os.environ["INSERTION_HOME"] = os.path.dirname(os.path.realpath(__file__))

# Flags
devMode = True if "--dev-mode" in sys.argv else False
buildFlag = True if "--build" in sys.argv else False
purgeLogs = True if "--purge-logs" in sys.argv else False
checksumIgnore = True if "--ignore-checksum" in sys.argv else False



import _Engine as Engine



# Config Vars
c = configparser.ConfigParser()
c.read('Insertion.ini')

if c["DEFAULT"]["MachineID"] == "":
    c["DEFAULT"] = {"MachineID": uuid.uuid1().hex}
    with open('Insertion.ini', 'w') as configfile:
        c.write(configfile)


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



# Game Engine Initialization
try:
    engine = Engine.Engine(c["DEFAULT"]["MachineID"], c)
except Exception as e:
    logging.error("ENGINE EXITED WITH ERROR:\n"+str(e.with_traceback(None)))
    open("Data/Engine.json", "w").write(json.dumps(EngineJSON))
    open("Data/Settings.json", "w").write(json.dumps(SettingsJSON))