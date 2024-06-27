
# import random


# board = {
#     0:{"square": 0, "name": "GO","price": 0},
#     1:{"square": 1, "name": "Mediterranean Avenue", "price": 60, "rent": [2, 10, 30, 90, 160, 250]},
#     2:{"square": 2, "name": "Community Chest", "price": 0},
#     3:{"square": 3, "name": "Baltic Avenue", "price": 60, "rent": [4, 20, 60, 180, 320, 450]},
#     4:{"square": 4, "name": "Income Tax", "price": 0},
#     5:{"square": 5, "name": "Reading Railroad", "price": 200, "rent": [25, 50, 100, 200]},
#     6:{"square": 6, "name": "Oriental Avenue", "price": 100, "rent": [6, 30, 90, 270, 400, 550]},
#     7:{"square": 7, "name": "Chance", "price": 0},
#     8:{"square": 8, "name": "Vermont Avenue", "price": 100, "rent": [6, 30, 90, 270, 400, 550]},
#     9:{"square": 9, "name": "Connecticut Avenue", "price": 120, "rent": [8, 40, 100, 300, 450, 600]},
#     10:{"square": 10, "name": "Jail", "price": 0},
#     11:{"square": 11, "name": "St. Charles Place", "price": 140, "rent": [10, 50, 150, 450, 625, 750]},
#     12:{"square": 12, "name": "Electric Company", "price": 150, "rent": [4, 10]},
#     13:{"square": 13, "name": "Virginia Avenue", "price": 160, "rent": [12, 60, 180, 500, 700, 900]},
#     14:{"square": 14, "name": "Pennsylvania Railroad", "price": 200, "rent": [25, 50, 100, 200]},
#     15:{"square": 15, "name": "St. James Place", "price": 180, "rent": [14, 70, 200, 550, 750, 950]},
#     16:{"square": 16, "name": "Community Chest", "price": 0},
#     17:{"square": 17, "name": "Tennessee Avenue", "price": 180, "rent": [14, 70, 200, 550, 750, 950]},
#     18:{"square": 18, "name": "New York Avenue", "price": 200, "rent": [16, 80, 220, 600, 800, 1000]},
#     19:{"square": 19, "name": "Free Parking", "price": 0},
#     20:{"square": 20, "name": "Kentucky Avenue", "price": 220, "rent": [18, 90, 250, 700, 875, 1050]},
#     21:{"square": 21, "name": "Chance", "price": 0},
#     22:{"square": 22, "name": "Indiana Avenue", "price": 220, "rent": [18, 90, 250, 700, 875, 1050]},
#     23:{"square": 23, "name": "Illinois Avenue", "price": 240, "rent": [20, 100, 300, 750, 925, 1100]},
#     24:{"square": 24, "name": "B&O Railroad", "price": 200, "rent": [25, 50, 100, 200]},
#     25:{"square": 25, "name": "Atlantic Avenue", "price": 260, "rent": [22, 110, 330, 800, 975, 1150]},
#     26:{"square": 26, "name": "Ventnor Avenue", "price": 260, "rent": [22, 110, 330, 800, 975, 1150]},
#     27:{"square": 27, "name": "Water Works", "price": 150, "rent": [4, 10]},
#     28:{"square": 28, "name": "Marvin Gardens", "price": 280, "rent": [24, 120, 360, 850, 1025, 1200]},
#     29:{"square": 29, "name": "Go to Jail", "price": 0},
#     30:{"square": 30, "name": "Pacific Avenue", "price": 300, "rent": [26, 130, 390, 900, 1100, 1275]},
#     31:{"square": 31, "name": "North Carolina Avenue", "price": 300, "rent": [26, 130, 390, 900, 1100, 1275]},
#     32:{"square": 32, "name": "Community Chest", "price": 0},
#     33:{"square": 33, "name": "Pennsylvania Avenue", "price": 320, "rent": [28, 150, 450, 1000, 1200, 1400]},
#     34:{"square": 34, "name": "Short Line Railroad", "price": 200, "rent": [25, 50, 100, 200]},
#     35:{"square": 35, "name": "Chance", "price": 0},
#     36:{"square": 36, "name": "Park Place", "price": 350, "rent": [35, 175, 500, 1100, 1300, 1500]},
#     37:{"square": 37, "name": "Luxury Tax", "price": 0},
#     38:{"square": 38, "name": "Boardwalk", "price": 400, "rent": [50, 200, 600, 1400, 1700, 2000]}
# }

# dice1 = random.randint(1,6)
# dice2 = random.randint(1,6)

# print(f"player rolled :{dice1}")
# print(f"player rolled :{dice2}")
# steps_moved = dice1 + dice2 
# print(f"steps moved :{steps_moved}")

# player_position = 0    
# computer_position = 0



# # #player.position + move
# # #computer
# # #User
# # #player = user if computer else user 
# # #while true:

# # board = [{"square": 0, "name": "GO", "price": 0},]
# #new = {
# #    1:{"square": 0, "name": "GO", "price": 0},
# #   2:{"square": 1, "name": "Mediterranean Avenue", "price": 60, "rent": [2, 10, 30, 90, 160, 250]},
    
# #}

# def move(property):
#     if property in board:
#         return(
#             board[property]["square"],
#             board[property]["name"],
#             board[property]["price"],
#             board[property]["rent"]
#         )
#     else : 
#        return None
    
# property = int(input("enter key name "))

# # def move(steps_moved)
# #   steps_moved = dice1 + dice2
# #   for square in board:
# #     print(f"Square: {square['square']}")
# #     print(f"Name: {square['name']}")
# #     print(f"Price: {square['price']}")
# #     print(f"Rent: {square['rent']}")



# moved = move(property)
# if moved:
#     print("player moved;")
#     print("square:", moved[0])
#     print("name:", moved[0])
#     print("price:", moved[0])
#     print("rent:", moved[0])
# else :
#     # print("board with key", property, "not found")