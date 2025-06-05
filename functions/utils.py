import os
import time

def clearScreen(delay=0):
    time.sleep(delay+3)
    os.system('cls' if os.name == 'nt' else 'clear')