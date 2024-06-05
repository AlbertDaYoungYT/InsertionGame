import configparser
import platform
import logging
import uuid
import time
import json
import sys
import os

import _Engine as Engine

c = configparser.ConfigParser()
c.read('Insertion.ini')

if c["DEFAULT"]["MachineID"] == "":
    c["DEFAULT"] = {"MachineID": uuid.uuid1().hex}
    with open('Insertion.ini', 'w') as configfile:
        c.write(configfile)


os.environ["INSERTION_HOME"] = os.path.dirname(os.path.realpath(__file__))
buildFlag = True if sys.argv[-1] == "--build" else False


engine = Engine.Engine(c["DEFAULT"]["MachineID"], c)
