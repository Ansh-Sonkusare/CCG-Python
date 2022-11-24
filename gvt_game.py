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
            if p == p1:
                e = p2
            else:
                e=p1
            p.start_turn()
            i = input(f"{p.get_name()}>>>")
            print(str.strip(i))
            if(str.lower(i[0]) == "h"):
                n = i[2]
                print(p.prn_h(n))
main()
