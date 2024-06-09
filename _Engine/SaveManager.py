import pickle
import os



class Save:
    def __init__(self, _self, *args, **kwargs):
        self.parent = _self

        self.monitored_state = None

        self.slot = "Engine"
        os.makedirs("./Data/Saves/", exist_ok=True)
        self.gameActive = False
        self.enableAutoSave = True if self.parent.config["Saves"]["enableautosave"] == "yes" else False
        self.autosaveInterval = int(self.parent.config["Saves"]["autosaveinterval"])

        self.parent.eventEngineShutdown.subscribe(self.manualSave)
    
    @classmethod
    def manualSave(cls, state):
        with open(f"./Data/Saves/{cls.slot}.save", "wb") as sv:
            pickle.dump(state, sv)
    
    @classmethod
    def loadSave(cls, slot):
        with open(f"./Data/Saves/{slot}.save", "rb") as sv:
            return pickle.load(sv)