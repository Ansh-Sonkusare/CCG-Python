import gvt

def main():
    card1= gvt.Card("A",10,"B","D",20,30)
    card2= gvt.Card("C",10,"F","G",20,50)
    card3= gvt.Card("E",10,"L","H",20,40)

    # accessor printing
    print(card1.get_health())

    # below prints <gvt.Card object at 0x000001969AC480E0>
    print(card1)
    print(repr(card1))

    print(card1)
    card1.damage(5)
    print(card1)
    print(card1.is_conscious())

    print(card2)
    card2.damage(35)
    print(card2)
    print(card2.is_conscious())

    print(card1)
    print(card2)
    print(card3)

    print("card 1 is ", card1)
    print("card 2 is ", card2)
    print("card 3 is", card3)
    print(card1==card2)
    print(card2 == card3)

    hand = []
    hand.append(card1)
    hand.append(card2)
    hand.append(card3)
    print("costs same")
    for card in hand:
        print(card)
    hand.sort()
    for card in hand:
        print(card)
    
    card4=gvt.Card("TT",20,"A","B",70,100)
    card5=gvt.Card("TR",30,"C","A",40,100)
    card6=gvt.Card("TF",40,"D","E",10,100)
    
    player1= gvt.Player("Buttercup",16,5,10,24,8)
    player1.discards(5)
    print(player1)
    print("Discarded: " , player1.get_discarded(8))
    print("battalion: ",card4,card5,card6)
    
    hands=[]
    hands.append(card4)
    for card in hands:
        hands.sort()
        print("hand: ",card)
    
    
main()