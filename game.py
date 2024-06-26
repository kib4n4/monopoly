import random
from board import *
from player import *
def rollDice():

    input("press enter to roll the die")

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

print(f"player rolled :{dice1}")
print(f"player rolled :{dice2}")
steps_moved = dice1 + dice2 
print(f"steps moved :{steps_moved}")



def move(self,player, roll):
        # Move the player based on the dice roll and update position on the board.
        self.position = (self.position + roll) % len(board)
        player.properties.append =[]
        player.properties.append = board[self.position]
        
        print(f"{self.token} landed on {board[self.position]['name']}")



