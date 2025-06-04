from classes.enemy_manager import Enemy
from classes.player_manager import Player
from classes.floor_manager import Floor

enemy = Enemy("Goblin")
player = Player("Hero")
floor = Floor(1)
print(floor.floor_number, player.name, enemy.name)