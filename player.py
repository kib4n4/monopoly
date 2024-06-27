class Player:
    def __init__ (self, name, token=None, properties=None):
        self.name = name
        #self.token = token
        self.token = token if token is not None else self.tokenSelection()
        self.money = 1500
        #self.properties = properties
        self.properties = properties if properties is not None else [] 
        #if property is not not None, the self.properties is assigned value of properties
        #if property is None, self.properties is assigned an empty list.
        self.mortgaged_properties = []
        self.jail_turns = 0
        self.consecutive_doubles = 0
        self.get_out_of_jail_free = False
        self.position =0