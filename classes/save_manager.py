import pickle
from os import walk
import os

def saveNameValidator(name):
    files = []
    for (dirpath, dirnames, filenames) in walk('saves/'):
        files.extend(filenames)
        break
    if name.lower()+".dat" in files:
        return False
    else:
        return True

class SaveFile:
    def __init__(self, floor_manager, player_manager, enemy_manager):
        self.floor_manager = floor_manager
        self.player_manager = player_manager
        self.enemy_manager = enemy_manager
        pass
    def returnData(self):
        return self.floor_manager, self.player_manager, self.enemy_manager

class SaveManager:
    def __init__(self, saveId):
        self.saveId = saveId.lower()
        self.saveFile = None

    
    def pull(self):
        try:
            with open(f'saves/{self.saveId}.dat', 'rb') as f:
                self.saveFile = pickle.load(f)
                if not isinstance(self.saveFile, SaveFile):
                    raise ValueError("Invalid save file format")
                else:
                    return self.saveFile
        except FileNotFoundError:
            print(f"Save file {self.saveId}.dat not found.")
            
    def save(self, player, floor, enemies):
        self.saveFile = SaveFile(floor, player, enemies)
        try:
            with open(f'saves/{self.saveId}.dat', 'wb') as f:
                pickle.dump(self.saveFile, f)
        except Exception as e:
            print(f"Error saving file: {e}")



    

