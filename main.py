from classes.player_manager import Player
from classes.save_manager import SaveManager, SaveFile
from classes.input_manager import ResponseValidator
from classes.save_manager import saveNameValidator, saveExists

from classes.games.blackjack import BlackJack

from functions.save_functions import loadFromSaveFunc, newSaveFunc
from functions.utils import clearScreen

import os
import time


clearScreen()
print("Welcome to the game!")
gamePlayer, loadFromSave = loadFromSaveFunc()
if not loadFromSave:
    gamePlayer = newSaveFunc()
    SaveManager(gamePlayer.name).save(gamePlayer)

while True:
    BlackJack(gamePlayer)
    SaveManager(gamePlayer.name).save(gamePlayer)
    print(gamePlayer.statistics)
    print(gamePlayer.bank)


