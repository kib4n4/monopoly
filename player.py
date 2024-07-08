# player.py
import random
from board import *
from cards import draw_card, handle_card, chance_cards, community_chest_cards

class Player:
    def __init__(self, name, token=None, properties=None, is_computer=False):
        self.name = name
        self.token = token if token is not None else self.tokenSelection()
        self.money = 1500
        self.properties = properties if properties is not None else []
        self.mortgaged_properties = []
        self.position = 0
        self.is_computer = is_computer
        self.in_jail = False
        self.jail_turns = 0
        self.get_out_of_jail_free = False

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

    def rollDice(self):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"Hey, you rolled {die1} and {die2}")
        print(f"You rolled a total of {die1 + die2}")
        return die1, die2

    def move(self, roll, players):
        self.position = (self.position + roll) % len(board)
        current_square = board[self.position]

        if current_square['name'] == "Chance" and current_square['price']==0:
            chance_card = draw_card(chance_cards)
            handle_card(self, chance_card, players)
        elif current_square['name'] == "Community Chest" and current_square['price']==0:
            community_chest_card = draw_card(community_chest_cards)
            handle_card(self, community_chest_card, players)
        else:
            print(f"{self.name} moved to square {current_square['square']}: {current_square['name']} (${current_square.get('price', 'N/A')})")

            if 'price' in current_square:
                if current_square not in self.properties and current_square not in self.mortgaged_properties:
                    # Handle unowned property
                    print(f"{self.token}, you landed on an unowned property: {current_square['name']}.")
                elif current_square in self.properties:
                    # Handle owned property
                    print(f"{self.token}, you landed on your own property: {current_square['name']}.")
                elif current_square in self.mortgaged_properties:
                    # Handle mortgaged property
                    print(f"{self.token}, you landed on a mortgaged property: {current_square['name']}.")

    def buyProperty(self):
        property = board[self.position]
        if property not in self.properties and property not in self.mortgaged_properties:
            if self.money >= property['price']:
                self.properties.append(property)
                print(f"{self.token} bought {property['name']} for ${property['price']}")
                self.money -= property['price']
                print(f"Your balance is: {self.money}")
            else:
                print(f"{self.token} does not have enough money to buy {property['name']}")
        else:
            print(f"{property['name']} is already owned.")

    def mortgageProperty(self):
        if not self.properties:
            print(f"{self.token}, you do not own any properties.")
            return
        
        print(f"{self.token}, you own the following properties:")
        for i, property in enumerate(self.properties, 1):
            print(f"{i}. {property['name']}")

        choice = int(input("Enter the number of the property you want to mortgage (0 to cancel): "))
        
        if choice == 0:
            return

        if 1 <= choice <= len(self.properties):
            property_to_mortgage = self.properties[choice - 1]
            mortgage_value = property_to_mortgage['price'] // 2

            self.money += mortgage_value
            self.mortgaged_properties.append(property_to_mortgage)
            self.properties.remove(property_to_mortgage)
            property_to_mortgage['is_mortgaged'] = True

            print(f"{self.token} mortgaged {property_to_mortgage['name']} for ${mortgage_value}")
        else:
            print("Invalid choice.")
