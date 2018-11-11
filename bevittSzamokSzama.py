# Kérjünk be számokat a felhasználótól 0 végjelig. Írjuk ki a bevitt számok számát!

n = int(input("szám: "))
db = 1

while n != 0:
    n = int(input("szám: "))
    if n != 0:
        db += 1

print("\n" + str(db) + " számot írt be")
