from pathlib import Path
import sys
import os

HOME = os.environ["INSERTION_HOME"]
USER = str(Path.home())


def run():
    if not os.path.exists(os.path.join(HOME, "Data/")): os.mkdir(os.path.join(HOME, "Data/"))
    if not os.path.exists(os.path.join(HOME, "Data/Cache/")): os.mkdir(os.path.join(HOME, "Data/Cache/"))
    if not os.path.exists(os.path.join(HOME, "Data/Logs/")): os.mkdir(os.path.join(HOME, "Data/Logs/"))
    if not os.path.exists(os.path.join(HOME, "Data/Saves/")): os.mkdir(os.path.join(HOME, "Data/Saves/"))

    if not os.path.exists(os.path.join(HOME, "Content/")): os.mkdir(os.path.join(HOME, "Content/"))
    if not os.path.exists(os.path.join(HOME, "Content/DLCs/")): os.mkdir(os.path.join(HOME, "Content/DLCs/"))
    if not os.path.exists(os.path.join(HOME, "Content/Languages/")): os.mkdir(os.path.join(HOME, "Content/Languages/"))
    if not os.path.exists(os.path.join(HOME, "Content/Objects/")): os.mkdir(os.path.join(HOME, "Content/Objects/"))
    if not os.path.exists(os.path.join(HOME, "Content/Scenes/")): os.mkdir(os.path.join(HOME, "Content/Scenes/"))
    if not os.path.exists(os.path.join(HOME, "Content/Scripts/")): os.mkdir(os.path.join(HOME, "Content/Scripts/"))
    if not os.path.exists(os.path.join(HOME, "Content/Types/")): os.mkdir(os.path.join(HOME, "Content/Types/"))
    if not os.path.exists(os.path.join(HOME, "Content/Worlds/")): os.mkdir(os.path.join(HOME, "Content/Worlds/"))


#    if not os.path.exists(os.path.join(USER, "AppData/Local/Insertion/")): os.mkdir(os.path.join(HOME, "AppData/Local/Insertion/"))
#    if not os.path.exists(os.path.join(USER, "AppData/Local/Insertion/Saves")): os.mkdir(os.path.join(HOME, "AppData/Local/Insertion/Saves"))
    
