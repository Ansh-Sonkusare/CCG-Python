import gvt

def main():
    # a = str(input("Enter Player 1 name:"))
    # b = str(input("Enter Player 2 name:"))

    p1 = gvt.Player("a","Goats")
    p2 = gvt.Player("b","Trolls")
    print(repr(p1))
    print()
    print(repr(p2))

    print()

    p1.start_turn()

main()
