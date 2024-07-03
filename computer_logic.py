from board import *

def movePlayer(player, roll):
    player.move(roll)

def computerDecisionToBuy(player):
    property = board[player.position]
    if property not in player.properties and property not in player.mortgaged_properties:
        if player.money >= property['price']:
            player.buyProperty()

def computerDecisionToMortgage(player):
    if player.properties:
        player.mortgageProperty()

def computerTurn(player):
    print(f"\n{player.token}'s turn.")
    dice1, dice2 = player.rollDice()
    movePlayer(player, dice1 + dice2)

    property = board[player.position]
    if property not in player.properties and property not in player.mortgaged_properties:
        if player.money >= property['price']:
            computerDecisionToBuy(player)

    computerDecisionToMortgage(player)
