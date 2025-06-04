from classes.enemy_manager import Enemy
from classes.player_manager import Player
from classes.floor_manager import Floor
from classes.save_manager import SaveManager
from classes.save_manager import saveNameValidator
from classes.save_manager import saveExists

from classes.input_manager import ResponseValidator

print("Welcome to the game!")
loadFromSave = ResponseValidator("Would you like to load from a save? (yes/no)\n> ").yesNoValidate(yesReturnValue=True, noReturnValue=False)
if loadFromSave:
    saveName: str = None
    while not saveExists(saveName):
        saveName = ResponseValidator("Enter the name of your character save file. (Do not include .dat)\n> ").strValidate(allow_special_chars=False, max_word_length=1)

