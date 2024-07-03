from board import *

def movePlayer(player, roll):
    #Move the player on the board based on the dice roll.
    player.move(roll)

def computerDecisionToBuy(player):
    #Make a decision for the computer player to buy a property if possible.
    property = board[player.position]
    if property not in player.properties and property not in player.mortgaged_properties:
        if player.money >= property['price']:
            player.buyProperty()

def computerDecisionToMortgage(player):
    #Make a decision for the computer player to mortgage a property if owned.
    if player.properties:
        player.mortgageProperty()

def computerTurn(player):
    #Execute a turn for the computer player.
    print(f"\n{player.token}'s turn.")
    dice1, dice2 = player.rollDice()
    movePlayer(player, dice1 + dice2)

    # Check if the current property can be bought
    property = board[player.position]
    if property not in player.properties and property not in player.mortgaged_properties:
        if player.money >= property['price']:
            computerDecisionToBuy(player)

    # Check if the computer should mortgage a property
    computerDecisionToMortgage(player)