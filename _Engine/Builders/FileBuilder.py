from pathlib import Path
import sys
import os

HOME = os.environ["INSERTION_HOME"]
USER = str(Path.home())


def run():
    if not os.path.exists(os.path.join(HOME, "Data/")): os.mkdir(os.path.join(HOME, "Data/"))
    if not os.path.exists(os.path.join(HOME, "Content/")): os.mkdir(os.path.join(HOME, "Content/"))
    if not os.path.exists(os.path.join(HOME, "DLCs/")): os.mkdir(os.path.join(HOME, "DLCs/"))
    if not os.path.exists(os.path.join(HOME, "Languages/")): os.mkdir(os.path.join(HOME, "Languages/"))
    if not os.path.exists(os.path.join(HOME, "Screens/")): os.mkdir(os.path.join(HOME, "Screens/"))


#    if not os.path.exists(os.path.join(USER, "AppData/Local/Insertion/")): os.mkdir(os.path.join(HOME, "AppData/Local/Insertion/"))
#    if not os.path.exists(os.path.join(USER, "AppData/Local/Insertion/Saves")): os.mkdir(os.path.join(HOME, "AppData/Local/Insertion/Saves"))
    
