# cards.py
import random

chance_cards = [
    "Advance to GO", "Go to Jail", "Pay Poor Tax of $15", "Your building and loan matures. Collect $150",
    "You have won a crossword competition. Collect $100", "Bank pays you dividend of $50", "Get out of Jail Free",
    "Advance to Illinois Ave", "Advance to St. Charles Place", "Take a ride on the Reading Railroad",
    "Advance to Boardwalk", "Advance to the nearest Utility", "Advance to the nearest Railroad",
    "You are assessed for street repairs: $40 per house, $115 per hotel", "Pay each player $50", "Collect $150"
]

community_chest_cards = [
    "Advance to GO", "Bank error in your favor. Collect $200", "Doctor's fees. Pay $50", "From sale of stock you get $50",
    "Get out of Jail Free", "Go to Jail", "Grand Opera Night. Collect $50 from every player",
    "Holiday Fund matures. Receive $100", "Income tax refund. Collect $20", "It is your birthday. Collect $10 from each player",
    "Life insurance matures. Collect $100", "Pay hospital fees of $100", "Pay school fees of $150",
    "Receive $25 consultancy fee", "You have won second prize in a beauty contest. Collect $10", "You inherit $100"
]

def draw_card(cards):
    selected_card = random.choice(cards)
    print(f"You drew a '{selected_card}' card.")
    return selected_card

def handle_card(player, card, players):
    if card == "Advance to GO":
        player.position = 0
        player.money += 200
        print(f"{player.name} advanced to GO and collected $200.")
    elif card == "Go to Jail":
        player.position = 10
        player.in_jail = True
        player.jail_turns = 0
        print(f"{player.name} is sent to jail.")
    elif card == "Pay Poor Tax of $15":
        player.money -= 15
        print(f"{player.name} paid $15 Poor Tax.")
    elif card == "Your building and loan matures. Collect $150":
        player.money += 150
        print(f"{player.name} collected $150 from building and loan maturing.")
    elif card == "You have won a crossword competition. Collect $100":
        player.money += 100
        print(f"{player.name} collected $100 for winning a crossword competition.")
    elif card == "Bank pays you dividend of $50":
        player.money += 50
        print(f"{player.name} collected $50 bank dividend.")
    elif card == "Get out of Jail Free":
        player.get_out_of_jail_free = True
        print(f"{player.name} received a 'Get out of Jail Free' card.")
    elif card == "Advance to Illinois Ave":
        player.position = 24
        print(f"{player.name} advanced to Illinois Ave.")
    elif card == "Advance to St. Charles Place":
        player.position = 11
        print(f"{player.name} advanced to St. Charles Place.")
    elif card == "Take a ride on the Reading Railroad":
        player.position = 5
        print(f"{player.name} advanced to Reading Railroad.")
    elif card == "Advance to Boardwalk":
        player.position = 38
        print(f"{player.name} advanced to Boardwalk.")
    elif card == "Advance to the nearest Utility":
        if player.position < 12 or player.position > 28:
            player.position = 12
        else:
            player.position = 28
        print(f"{player.name} advanced to the nearest Utility.")
    elif card == "Advance to the nearest Railroad":
        if player.position < 5 or player.position > 35:
            player.position = 5
        elif player.position < 15:
            player.position = 15
        elif player.position < 25:
            player.position = 25
        else:
            player.position = 35
        print(f"{player.name} advanced to the nearest Railroad.")
    elif card == "You are assessed for street repairs: $40 per house, $115 per hotel":
        total_cost = sum(player.houses.values()) * 40 + sum(player.hotels.values()) * 115
        player.money -= total_cost
        print(f"{player.name} paid ${total_cost} for street repairs.")
    elif card == "Pay each player $50":
        for p in players:
            if p != player:
                player.money -= 50
                p.money += 50
        print(f"{player.name} paid each player $50.")
    elif card == "Collect $150":
        player.money += 150
        print(f"{player.name} collected $150.")
