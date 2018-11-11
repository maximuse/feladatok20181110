# Kérdezzük meg a felhasználótól, hogy minek a területét szeretné kiszámítani: négyzetét, téglalapét vagy körét? Kérjük
# be a szükséges adatokat és írjuk ki az eredményt! Ezután újra kínáljuk fel a lehetőségeket! Tegyük lehetővé azt is,
# hogy a felhasználó kiszálljon a programból!

import math


def printMenu():
    print("1 - Négyzet területe\n2 - Téglalap területe\n3 - Kör területe\n0 - Kilépés\n")


printMenu()
n = int(input("menüpont száma: "))

while n != 0:
    if n == -1:
        printMenu()
        n = int(input("menüpont száma: "))

    if n != 0:
        if n == 1:
            a = int(input("a: "))
            print("A(z) " + str(a) + " egység oldalú négyzet területe " + str(math.pow(a, 2)) + "\n\n")
            n = -1
        elif n == 2:
            a = int(input("a: "))
            b = int(input("b: "))
            print("A(z) " + str(a) + " és " + str(b) + " egység oldalú téglalap területe " + str(a * b) + "\n\n")
            n = -1
        elif n == 3:
            r = int(input("r: "))
            print("A(z) " + str(r) + " egység sugarú kör területe " + str(math.pow(r, 2) * math.pi) + "\n\n")
            n = -1
        else:
            print("Hiba! Nincs ilyen számű menüpont!\n\n")
            n = -1
