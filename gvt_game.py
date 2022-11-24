import gvt
def print_p(a , b):
    print(repr(a))
    print()
    print(repr(b))

def main():
    # a = str(input("Enter Player 1 name:"))
    # b = str(input("Enter Player 2 name:"))

    p1 = gvt.Player("Bruce","Goats")
    p2 = gvt.Player("Bobby","Trolls")
    print_p(p1,p2)

    print()

    while(True):
        for p in [p1 , p2]:
            p.start_turn()

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

                if(str.lower(i[0]) == "b"):
                    n = i[1]
                    print(n)
                    print(p.prn_b(n))
                    # print()
                if(str.lower(i[0]) == "e"):

                    n = i[1]
                    print(e.prn_b(n))
                if(str.lower(i[0]) == "p"):
                    n = i[1]
                    u = p.make_move(n)
                    if(u):
                        print_p(p1,p2)


                if(str.lower(i[0]) == "q"):
                    p.end_turn()
                    break


                i = input(f"{p.get_name()}>>>")
                i = (str.split(i))


            
main()
