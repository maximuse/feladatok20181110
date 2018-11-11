# Készítsünk egy menüt! Három dologból lehet választani: egyik funkció, másik funkció és kilépés. Jelenítsük meg a
# választási lehetőségeket: <E>gyik / <M>ásik / <V>ége ? Az Egyik, illetve a Másik funkció választására ismételten
# jelenjen meg egy-egy szöveg, a Vége választására pedig legyen vége a programnak.


def printMenu():
    print("<E>gyik / <M>ásik / <V>ége\n")
    return input("menüpont betűje: ")


m = printMenu()

while True:
    if m == "-1":
        m = printMenu()

    if (m != 'v') or (m != 'V'):
        if (m == 'e') or (m == 'E'):
            print("Egyik menü szövege...\n\n")
            m = "-1"
        elif (m == 'm') or (m == 'M'):
            print("Másik menü szövege...\n\n")
            m = "-1"
        elif (m == 'v') or (m == 'V'):
            exit()
        else:
            print("Hiba! Nincs ilyen menüpont!\n\n")
            m = "-1"
