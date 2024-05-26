from _Engine.Objects import StateObject


"""class States:
    STORY_STATE: int = 0
    
    PLAYER_ID: str = ""
    PLAYER_LEVEL: int = 1
    PLAYER_ACHIEVEMENTS: list = []
    PLAYER_BALANCE: int = 0
    PLAYER_CHARACTER_ID: int = 1
    PLAYER_CHARACTER_COSMETIC: list = []
    PLAYER_CHARACTER_INVENTORY: dict = {}
    
    PLAYER_SHIP_ID: str = ""
    PLAYER_SHIP_TYPE: int = 0
    PLAYER_SHIP_LEVEL: int = 1
    PLAYER_SHIP_COSMETIC: list = []
    PLAYER_SHIP_INVENTORY: dict = {}

    UNLOCKED_CRAFTABLES: list = []
    UNLOCKED_SHIPS: list = []
    UNLOCKED_COSMETICS: list = []
    UNLOCKED_CHARACTERS: list = []
"""

class State:

    def __init__(self, _self):
        self.__init__(_self)
    
    def new(self):
        return StateObject().__init__()
    
    def load(self, state):
        return StateObject(state)