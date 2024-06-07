import threading
import pickle
import time
import json
import os



class Save(threading.Thread):
    def __init__(self, _self):
        threading.Thread.__init__(self)
        self.parent = _self

        self.monitored_state = None

        self.slot = "Slot1"
        os.makedirs("./Data/Saves/", exist_ok=True)
        self.gameActive = False
        self.enableAutoSave = True if self.parent.config["Saves"]["enableautosave"] == "yes" else False
        self.autosaveInterval = int(self.parent.config["Saves"]["autosaveinterval"])
    
    def manualSave(self, state):
        with open(f"./Data/Saves/{self.slot}.save", "wb") as sv:
            pickle.dump(state, sv)
    
    def loadSave(self, slot):
        with open(f"./Data/Saves/{slot}.save", "rb") as sv:
            return pickle.load(sv)
    
    def run(self):
        while True:
            if self.gameActive and self.monitored_state != None:
                time.sleep(self.autosaveInterval)
                self.manualSave(self.monitored_state)