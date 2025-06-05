from classes.player_manager import Player
from classes.save_manager import SaveManager, SaveFile
from classes.input_manager import ResponseValidator
from classes.save_manager import saveNameValidator, saveExists

from classes.games.blackjack import BlackJack
from classes.games.roulette import Roulette

games = [BlackJack, Roulette]
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
    clearScreen()
    print(f"\nWelcome back, {gamePlayer.name}!")
    print(f"You have {gamePlayer.bank}$ in chips remaining.")
    print("\nAvailable Games:")
    print("0. Exit")
    print("1. Player Statistics")
    print("2. Save Manager")
    for i, game in enumerate(games, start=1):
        print(f"{i+2}. {game.__name__}")
    
    choice = ResponseValidator("Select a game to play (0 to exit):\n> ").intValidate(min_value=0, max_value=len(games)+2)
    if choice == 0:
        print("Exiting the game. Goodbye!")
        break
    elif choice == 1:
        clearScreen()
        print(f"Player Statistics for {gamePlayer.name.title()}")
        print(gamePlayer.readableStats())
        input(("\n"*3) + "... Press \"Enter\" to continue ...")
    elif choice == 2:
        clearScreen()
        print("[Save Manager] Welcome to the save manager!")
        print("1. Save current player")
        print("2. Create new save")
        print("3. Exit Save Manager")
        
        save_choice = ResponseValidator("Select an option:\n> ").intValidate(min_value=1, max_value=3)
        if save_choice == 1:
            SaveManager(gamePlayer.name).save(gamePlayer)
        elif save_choice == 2:
            SaveManager(gamePlayer.name).save(gamePlayer)
            clearScreen()
            gamePlayer = newSaveFunc()
            SaveManager(gamePlayer.name).save(gamePlayer)
        elif save_choice == 3:
            continue
    elif 2 <= choice <= len(games)+2:
        selected_game = games[choice - 3]
        clearScreen()
        print(f"Starting {selected_game.__name__}...")
        selected_game(gamePlayer)
    else:
        print("Invalid choice, please try again.")
    SaveManager(gamePlayer.name).save(gamePlayer)


