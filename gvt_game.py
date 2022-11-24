import gvt

def main():
    # a = str(input("Enter Player 1 name:"))
    # b = str(input("Enter Player 2 name:"))

    p1 = gvt.Player("Bruce","Goats")
    p2 = gvt.Player("Bobby","Trolls")
    print(repr(p1))
    print()
    print(repr(p2))

    print()

    while(True):
        for p in [p1 , p2]:
            p.start_turn()

            i = input(f"{p.get_name()}>>>")
            i = (str.split(i))

            while(i[0] != "q"):
                if p == p1:
                    e = p2
                else:
                    e=p1

                if(str.lower(i[0]) == "h"):
                    n = i[1]
                    print(n)
                    print(p.prn_h(n))
                    # print()

                i = input(f"{p.get_name()}>>>")
                i = (str.split(i))


            
main()
