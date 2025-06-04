from classes.enemy_manager import Enemy
from classes.player_manager import Player
from classes.floor_manager import Floor
from classes.save_manager import SaveManager
from classes.save_manager import saveNameValidator
from classes.input_manager import ResponseValidator

print("Welcome to the game!")
ResponseValidator("What should we call you?\n> ").strValidate(min_word_length=1,max_word_length=1,allowNumbers=False)

