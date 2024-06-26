import random
print(input("press enter to roll dice"))

dice1= random.randint(1,6)
print(f'dice 1 rolled a:{dice1}')
dice2=random.randint(1,6)
print(f'dice 2 rolled a:{dice2}')
steps_moved= dice1 + dice2

print(f"dice rolled:{steps_moved}")