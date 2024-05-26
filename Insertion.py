import configparser
import platform
import logging
import uuid
import time
import json

import _Engine as Engine

c = configparser.ConfigParser()
c.read('Insertion.ini')

if c["DEFAULT"]["MachineID"] == "":
    c["DEFAULT"] = {"MachineID": uuid.uuid1().hex}
    with open('Insertion.ini', 'w') as configfile:
        c.write(configfile)



engine = Engine.Engine(c["DEFAULT"]["MachineID"], c)
