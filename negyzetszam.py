# Hány darab négyzetszám van 1000-ig? Írd is ki a négyzetszámokat!

import math

mettol = 1
meddig = 1000
db = 0
szam = 0
szamok = ""

while szam < meddig:
    szam = int(math.pow(mettol, 2))
    if szam < meddig:
        szamok += str(szam) + " "
        mettol += 1
        db += 1

print(str(meddig) + "-ig " + str(db) + " db négyzetszám van: " + szamok)
