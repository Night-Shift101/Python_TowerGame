from classes.player_manager import Player
from classes.save_manager import SaveManager, SaveFile
from classes.input_manager import ResponseValidator
from classes.save_manager import saveNameValidator, saveExists

numberOfSaves = 5
coruptionPrecent = 0.2  # 20% chance of corruption
for i in range(numberOfSaves):
    saveName = f"testSave{i+1}"
    if saveNameValidator(saveName):
        print(f"Creating save file: {saveName}.dat")
        gamePlayer = Player(f"test_save_{i+1}")
        
        # Simulate potential corruption
        if i < numberOfSaves * coruptionPrecent:
            
            print(f"Corrupting save file: {saveName}.dat")
            gamePlayer = None  # Keep player manager intact
        
        saveFile = SaveManager(saveName)
        saveFile.save(gamePlayer)
        
    else:
        print(f"Save name {saveName} is invalid or already exists.")