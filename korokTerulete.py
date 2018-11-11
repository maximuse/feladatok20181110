# A felhasználó adott sugarú körök kerületére kíváncsi. Amikor ő beüt egy sugarat, mi kiírjuk a kör kerületét. Ha már nem
# kíváncsi több eredményre, akkor a kör sugaránál nullát (végjelet)kell ütnie!

import math

r = int(input("sugár: "))
print("A(z) " + str(r) + " sugarú kör területe " + str(pow(r, 2) * math.pi) + "\n")

while r != 0:
    r = int(input("sugár: "))
    if r != 0:
        print("A(z) " + str(r) + " sugarú kör területe " + str(pow(r, 2) * math.pi) + "\n")
