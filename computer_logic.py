from board import *

def movePlayer(player, roll):
    player.move(roll)#call the move method 
                    #pass roll to move the player's token on the game board

def computerDecisionToBuy(player):
    property = board[player.position]
    #check that current player position is not owned or mortgaged
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
