import pickle
from os import walk
import os

def saveNameValidator(name: str = None):
    if not name:
        return False
    files = []
    name = str(name)
    for (dirpath, dirnames, filenames) in walk('saves/'):
        files.extend(filenames)
        break
    if name.lower()+".dat" in files:
        return False
    else:
        return True
def saveExists(name: str = None):
    if not name:
        return False
    files = []
    name = str(name)
    for (dirpath, dirnames, filenames) in walk('saves/'):
        files.extend(filenames)
        break
    if name.lower()+".dat" in files:
        return True
    else:
        return False
class SaveFile:
    def __init__(self, floor_manager, player_manager, enemy_manager):
        if floor_manager is None or player_manager is None or enemy_manager is None:
            raise ValueError("Floor, Player, and Enemy managers must not be None.")
            del(self)
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
                print(self.saveFile)
                if not isinstance(self.saveFile, SaveFile):
                     print("Invalid save file format")
                     return None
                elif self.saveFile is None:
                    print(f"Save file {self.saveId}.dat is empty or corrupted.")
                    return None
                else:
                    return self.saveFile
        except:
            print(f"Save file {self.saveId}.dat is empty or corrupted.")
            
            
    def save(self, player, floor, enemies):
        self.saveFile = SaveFile(floor, player, enemies)
        try:
            with open(f'saves/{self.saveId}.dat', 'wb') as f:
                pickle.dump(self.saveFile, f)
        except Exception as e:
            print(f"Error saving file: {e}")



    

