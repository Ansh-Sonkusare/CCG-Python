import gvt
def print_p(a , b):
    print(repr(a))
    print()
    print(repr(b))

def main():
    a = str(input("Enter Player 1 name:"))
    b = str(input("Enter Player 2 name:"))

    p1 = gvt.Player(a,"Goats")
    p2 = gvt.Player(b,"Trolls")
    # print_p(p1,p2)

    print()
    


    while(True):

        # print(1)
        for p in [p1 , p2]:
            if p == p1:
                    e = p2
            else:
                    e=p1

            if(p1.is_lost()):
                print(f"{p1.get_name()} is defeated!! {p2.get_name()} Win!!")
                return
            if(p2.is_lost()):
                print(f"{p2.get_name()} is defeated!! {p1.get_name()} Win!!")
                return

            p.start_turn()

            print(repr(e))
            print(repr(p))

            i = input(f"{p.get_name()}>>>")
            i = (str.split(i))

            while(True):
                if p == p1:
                    e = p2
                else:
                    e=p1

                if(str.lower(i[0]) == "h"):
                    n = i[1]
                    print(n)
                    print(p.prn_h(n))
                    # print()

                elif(str.lower(i[0]) == "b"):
                    n = i[1]
                    print(n)
                    print(p.prn_b(n))
                    # print()
                elif(str.lower(i[0]) == "e"):

                    n = i[1]
                    print(e.prn_b(n))
                elif(str.lower(i[0]) == "p"):
                    n = i[1]
                    u = p.make_move(n)
                    if(u):
                        print(repr(e))
                        print(repr(p))


                elif(str.lower(i[0]) == "q"):
                    edm = p.end_turn()
                    e.be_damaged(edm)
                    break

                elif(str.lower(i[0]) == "i"):
                    print("H # - show a detailed string for the specified card in the player's hand. # is a number from 1-length.\n\
B # - show a detailed string for the specified card in the player's battalion. \n\
E # - show a detailed string for the specified card in the enemy player's battalion.\n\
P # - play the card from the player's hand. If the card is successfully played, print the detailed string representation for both players, otherwise print an error message.\n\
Q - end the player's turn. At this point, the player attacks the opposing player. If the opposing player is not defeated, play transitions to the opposing player's turn.\n\
I - displays a list of available commands.\n ")
                    print(repr(p))
            
                else:
                    print("wrong command")


                


                i = input(f"{p.get_name()}>>>")
                i = (str.split(i))


            
main()
