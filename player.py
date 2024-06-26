
import random
from board import *

class Player:
    def __init__ (self, name, token=None, properties=None):
        self.name = name
        #self.token = token
        self.token = token if token is not None else self.tokenSelection()
        self.money = 1500
        #self.properties = properties
        self.properties =  []
        #if property is not not None, the self.properties is assigned value of properties
        #if property is None, self.properties is assigned an empty list.
        self.mortgaged_properties = []
        self.jail_turns = 0
        self.consecutive_doubles = 0
        self.get_out_of_jail_free = False
        self.position=0

    # def tokenSelection(self):
    #     # an instance method for token selection.
    #     tokens = ["Thor", "strange", "IronMan", "Hawkeye",]
    #     print("Choose your token:")
    def tokenSelection(self):
        tokens = ["Thor", "Strange", "IronMan", "Hawkeye"]
        print("Choose your token:")
        for i, token in enumerate(tokens):
            print(f"{i + 1}. {token}")
        choice = int(input("Enter the number of your choice: ")) - 1
        while choice < 0 or choice >= len(tokens):
            print("Invalid choice. Please choose again.")
            choice = int(input("Enter the number of your choice: ")) - 1
        return tokens[choice]
        # return random.choice(tokens)
        #randomly chooses a token from the list of the tokens

    def rollDice(self):
        # Method to simulate rolling two six-sided dice.
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        moved1 = die1
        moved2 = die2
        movedTo = die1 + die2
        print(f"hey, you rolled {moved1} and {moved2}")
        print(f"You rolled a total of {movedTo}")
        return die1, die2

    def move(self, roll):
        # Move the player based on the dice roll and update position on the board.
        self.position = (self.position + roll) % len(board)
        print(f"{self.token} landed on {board[self.position]['name']}")

    def mortgaging(self, propertyName):
        # Method for mortgaging properties
        for property in self.properties:
            if property['name'] == propertyName:
                mortgageValue = property['price'] // 2
                #mortgaging a property, adds half the price of the property to the player's money
                self.money = self.money + mortgageValue
                self.mortgaged_properties.append(property)
                #adds the property to the mortgaged properties list
                self.properties.remove(property)
                #removes the property from the player's properties list
                property['mortgaged'] = True
                #sets the mortgaged status of the property to True
                print(f"{self.token} mortgaged {propertyName} for ${mortgageValue}")
                return
        print(f"{self.token} does not own {propertyName}")

def movePlayer(player, roll):
    player.move(roll)

# def mortgageProperty(player):
#     print(f"{player.token}, you own the following properties:{player.properties}")
#     for i, property in enumerate(player.properties, 1):
#         print(f"{i}. {property['name']}")

#     choice = int(input("Enter the number of the property you want to mortgage (0 to cancel): "))
#     if choice == 0:
#         return

    # # Adjust for 0-based index
    # selected_property = player.properties[choice - 1]['name']
    # player.mortgaging(selected_property)

def play_game():
    global player1, player2
    print("Player 1, please select your token.")
    player1 = Player("Player 1")
    remaining_tokens = ["Thor", "Strange", "IronMan", "Hawkeye"]
    remaining_tokens.remove(player1.token)
    player2 = Player("Computer", token=random.choice(remaining_tokens))
    #loops through the remaining tokens

    current_player = player1

    while True:
        print(f"\n{current_player.token}'s turn.")
        input("Press Enter to roll the dice.\n")
        dice1, dice2 = current_player.rollDice()
        movePlayer(current_player, dice1 + dice2)

        # print(f"\n{current_player.token}, do you want to mortgage a property?")
        # mortgage_option = input("Press 'y' to mortgage or 'n' to continue: ").lower()
        # if mortgage_option == 'y':
        #     mortgageProperty(current_player)

        current_player = player1 if current_player == player2 else player2

play_game()