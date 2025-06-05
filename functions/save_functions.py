from classes.player_manager import Player
from classes.save_manager import SaveManager, SaveFile
from classes.input_manager import ResponseValidator
from classes.save_manager import saveNameValidator, saveExists

from functions.utils import clearScreen

import os
import time
    
def loadFromSaveFunc():
    gamePlayer = None
    loadFromSave = False
    loadFromSave = ResponseValidator("Would you like to load from a save? (yes/no)\n> ").yesNoValidate(yesReturnValue=True, noReturnValue=False)
    clearScreen()
    if loadFromSave:
        saveName: str = None
        while not saveExists(saveName):
            saveName = ResponseValidator("[Save Manager] Enter the name on your save file. (Do not include .dat | \"exit\" to quit)\n> ").strValidate(allow_special_chars=True, max_word_length=1)
            if saveName.lower() == "exit":
                loadFromSave = False
                clearScreen()
                print("[Save Manager] Exiting save menu, creating new save")
                clearScreen(delay=1.4)
                break
        if loadFromSave:
            localSave = SaveManager(saveName).pull()
            if not isinstance(localSave, SaveFile):
                clearScreen()
                loadFromSave = False
                print("[Save Manager] Error, file locataed but we ran into an issue, unable to load save file.")
                clearScreen(1.4)
            else:
                try:
                    gamePlayer = localSave.player_manager
                except Exception as e:
                    clearScreen()
                    gamePlayer = None
                    loadFromSave = False
                    print(f"[Save Manager] Error, unable to load save file, error: {e}")
                    clearScreen(3)

                if not isinstance(gamePlayer, Player):
                    gamePlayer = None
                    loadFromSave = False
                    clearScreen()
                    print("[Save Manager] Error, unable to locate a portion of the save file, creating new save.")
                    clearScreen(1)
    else:
        clearScreen()
        print("[Save Manager] No save file selected, creating new save.")
    return gamePlayer, loadFromSave

def newSaveFunc():
    saveName: str = None
    while not saveNameValidator(saveName):
        if saveName is not None:
            print("[Save Manager] Save name is invalid or already exists, please try again.")
        saveName = ResponseValidator("[Save Manager] Enter your name. \n> ").strValidate(allow_special_chars=False, max_word_length=1)
    gamePlayer = Player(saveName)
    return gamePlayer