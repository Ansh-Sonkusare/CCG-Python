import random
import goatils

COMMON = 1
UNCOMMON = 2
RARE = 3
LEGENDARY = 4

RESET = "\u001b[0m"
WHITE = "\u001b[38;5;7m"
LIGHT_GREEN = "\u001b[38;5;10m"
BLUE = "\u001b[38;5;26m"
ORANGE = "\u001b[38;5;130m"
GREEN = "\u001b[38;5;28m"
RED = "\u001b[38;5;9m"
YELLOW = "\u001b[38;5;11m"

RARITY_STRINGS = {
    COMMON : WHITE + "C", 
    UNCOMMON : LIGHT_GREEN + "U", 
    RARE : BLUE + "R", 
    LEGENDARY : ORANGE + "L"}

class Card:
    __slots__ = ["__name", "__cost","__rarity","__fraction","__attack_power","__health"]
    
    # below are constructor
    def __init__(self,name, cost, rarity, fraction, attack_power, health):
        self.__name= name
        self.__rarity= rarity
        self.__cost = cost
        self.__fraction = fraction
        self.__attack_power = attack_power
        self.__health = health

    # accessor below:
    def get_name(self):
        return self.__name
    def get_cost(self):
        return self.__cost
    def get_rarity(self):
        return self.__rarity
    def get_faction(self):
        return self.__fraction
    def get_attack_power(self):
        return self.__attack_power
    def get_health(self):
        return self.__health
    
    # __repr__
    # \ means line continuation
    def __str__(self):
        # return " "
        return"[" +self.__fraction[0] +self.__name[0] + " " + "{:02d}".format(self.__cost) + " " + "{:02d}".format(self.__attack_power)  + " " + "{:02d}".format(self.__health) +"]"

    def __repr__(self):
       
        output = str(self.__name) \
            + "\nRarity: "+ str(self.__rarity) \
            + "\nFaction: "+ str(self.__fraction) \
            +"\nResource Cost: "+str(self.__cost) \
            +"\nHealth Points: "+ str(self.__health) \
            +"\nAttack power: " + str(self.__attack_power)
        return output

    # __str__

    # method:
    def damage(self,amount):
        
        r = amount-self.__health
        self.__health-=amount
        return max(r , 0)
       
    
    def is_conscious(self):
        return self.__health > 0

    # __eq__
    def __eq__(self,other):
        if type(self)== type(other):
            return self.__rarity == other.__rarity \
                and self.__fraction == other.__fraction \
                and self.__cost == other.__cost\
                and self.__attack_power == other.__attack_power
        else:
            return False

    # __lt__ sort
    def __lt__(self,other):
        if self.__cost != other.__cost:
            return self.__cost < other.__cost
        else:
            return self.__name < other.__name

    # make a card:
GOATS= "Goats"
TROLLS = "Trolls"

TROLL_NAMES = ["troll","oidsgvosoh"]

def make_card(faction, rarity):
    name = ""
    if faction == GOATS:
        name = goatils.make_goat_name()
    else:
        randex = random.randrange(len(TROLL_NAMES))
        name = TROLL_NAMES[randex]
    
    total = 0
    cost = 0
    r =''
    if rarity == COMMON:
        r = "C"
        total = 8
        cost = random.randint(1,3)
    elif rarity == UNCOMMON:
        r = "U"
        total = 12
        cost = random.randint(2,5)
    elif rarity == RARE:
        r = "R"
        total = 16
        cost = random.randint(4,7)
    elif rarity== LEGENDARY:
        r = "L"
        total = 24
        cost = 10
    else:
        raise ValueError("invalid"+ str(rarity))
    
    health = random.randint(1,total)
    attack_power = total - health
    return Card (name, cost, r, faction, attack_power, health)

def make_deck(faction):
    deck=[]
    for i in range(20):
        deck.append(make_card(faction,COMMON))
    for i in range(10):
        deck.append(make_card(faction,UNCOMMON))
    for i in range(8):
        deck.append(make_card(faction,RARE))
    for i in range(2):
        deck.append(make_card(faction,LEGENDARY))
    
    random.shuffle(deck)
    return deck 

class Player:

    slots = ["__name", "__score", "__resource_points", "__max_resource_points", "__deck", "__hand", "__battalion", "__discarded"]

    def __init__(self, name,faction):

        self.__name = name

        self.__score = 20
        self.__prev_p = 0
        self.__max_resource_points = 0

        self.__resource_points = min(0,self.__max_resource_points)
        self.__tdm = 0
        self.__deck = make_deck(faction)

        self.__hand = []
        self.__plays = 0
        self.__battalion = []

        self.__discarded = 0

        for _ in range(5):

            self.__hand.append(self.__deck.pop())

        self.__hand.sort()
        
    def discards(self,amount):
        if amount <= self.__resource_points:
            self.__resource_points-=amount
            
            return 0
        else:
            current = self.__resource_points
            self.__resource_points = 0
            return amount - current   
    
    def get_discarded(self,amount):
        return amount
    def get_name(self):
        return self.__name
    # "[" +self.__name[0] +self.__score[0] + " " + "{:02d}".format(self.__max_resource_points) + " " + "{:02d}".format(self.__resource_points)  + " " + "{:02d}".format(self.__deck) +" " + "{:02d}".format(self.__discarded)+"]"
    def prn_h(self,i):
        i = int(i)

        if(i > len(self.__hand)):
            return "Invalid Card"
        return(repr(self.__hand[i-1]))
    def prn_b(self,i):
        i = int(i)
        if(i > len(self.__battalion)):
            return "Invalid Card"
        return(repr(self.__battalion[i-1]))

        
    def start_turn(self):

        self.__max_resource_points += 1
        self.__max_resource_points = min(self.__max_resource_points , 10)

        if self.__resource_points < self.__max_resource_points:

            self.__resource_points += 1
        self.__hand.append(self.__deck.pop())
        self.__resource_points += self.__prev_p 
        self.__resource_points = min(self.__resource_points , self.__max_resource_points)


        # print(repr(self))
    def make_move(self, i):
        i = int(i)
        a = self.__hand[i-1]
        c = a.get_cost()
        if(self.__resource_points - c) >= 0:
            self.__resource_points -= c
            self.__prev_p += c
            self.__battalion.append(self.__hand.pop(i-1))
            self.__plays += 1
            return True
        else:
            print("invalid card")
    def end_turn(self):
        total_dmg = sum([i.get_attack_power() for i in self.__battalion])
        self.__tdm = total_dmg
        # print("DMGGGGGGGGGGGGGGGGGGGGGGG" , total_dmg)
        return self.__tdm

    def be_damaged(self , edm):
        h = False
        while(edm > 0 and len(self.__battalion) > 0):
            h = True
            i = self.__battalion.pop()
            edm = i.damage(edm)
            if(i.is_conscious() ):
                self.__battalion.append(i)
            else:
                self.__discarded +=1
        if(h and edm>0):
            self.__score -= edm

            

    def get_prev(self):
        return self.__prev_p
            

    

       
    def is_lost(self):
        if(self.__score <= 0 or ( len(self.__hand)== 0 and len(self.__deck) == 0)):
            return True 
        return False
     
    def __str__(self) -> str:
        return(f"Player: {self.__name}")
    
    def __repr__(self) -> str:
        h = ""
        for i in self.__hand:
            h += str(i) + " "
        b = ""
        for j in self.__battalion:
            b += str(j) + " "
   
   
        return (f"Player: {self.__name}\nScore: {self.__score}\nResource Points: {self.__resource_points}/{self.__max_resource_points}\nDeck: {len(self.__deck)}\nDiscared: {self.__discarded}\nBattalion: {b}\nHand: {h}")
        

