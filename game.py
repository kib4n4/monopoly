import random
from board import *
from player import *




dice1 = random.randint(1,6)
print(f"player rolled :{dice1}")
dice2 = random.randint(1,6)
print(f"player rolled :{dice2}")

steps_moved = dice1 + dice2 
print(f"steps moved :{steps_moved}")

#def move(player, roll):
#        # Move the player based on the dice roll and update position on the board.
#        player.position = (player.position + roll) % len(board)
#        print(f"{player.token} landed on {board[player.position]['name']}")


