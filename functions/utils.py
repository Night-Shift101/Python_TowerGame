import os
import time

def clearScreen(delay=0):
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')