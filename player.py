class Player:
    def __init__(self, name: str):
        self.name = name
        self.position = 0
        self.money = 1500
        self.properties = []
        self.houses = 0
        self.hotels = 0
        self.mortgaged_properties = []
        self.is_bankrupt = False
        self.in_jail = False
        self.jail_turns = 0
        self.consecutive_doubles = 0
        self.get_out_of_jail_free = False