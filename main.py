from classes.enemy_manager import Enemy
from classes.player_manager import Player
from classes.floor_manager import Floor
from classes.save_manager import SaveManager
from classes.save_manager import saveNameValidator
from classes.input_manager import ResponseValidator


save = SaveManager("save1")
floor, player, enemys = save.pull().returnData()
print(floor.floor_number)
print(player.name)
print(enemys.name)