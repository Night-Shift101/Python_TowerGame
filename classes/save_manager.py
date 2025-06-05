import pickle
from os import walk
import os
import time

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
        print("[Save Manager] Save not found")
        return False
class SaveFile:
    def __init__(self, player_manager):
        if  player_manager is None:
            print("[Save Manager] Error, one or more managers are None, unable to load/create save file.")
            del self
            return
        self.player_manager = player_manager
        pass
    def returnData(self):
        return self.player_manager

class SaveManager:
    def __init__(self, saveId):
        self.saveId = saveId.lower()
        self.saveFile = None

    
    def pull(self):   
        try:
            with open(f'saves/{self.saveId}.dat', 'rb') as f:
                self.saveFile = pickle.load(f)
                if not isinstance(self.saveFile, SaveFile):
                     print("Invalid save file format")
                     return None
                elif self.saveFile is None:
                    print(f"Save file {self.saveId}.dat is empty or corrupted.")
                    return None
                else:
                    return self.saveFile
        except Exception as e:
            print(f"Error loading save file: {e}")
            print(f"Save file {self.saveId}.dat is empty or corrupted.")
            
            
    def save(self, player):
        self.saveFile = SaveFile(player)
        try:
            with open(f'saves/{self.saveId}.dat', 'wb') as f:
                pickle.dump(self.saveFile, f)
                print(f'[Save Manager] \"saves/{self.saveId}.dat\" was saved successfully.')
                time.sleep(3)
        except Exception as e:
            print(f"Error saving file: {e}")
            time.sleep(3)




    

