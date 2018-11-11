# Olvassuk be a számokat 0 végjelig, majd írjuk ki ezek összegét, darabszámát és átlagát!

n = int(input("szám: "))
osszeg = n
db = 1

while n != 0:
    n = int(input("szám: "))
    if n != 0:
        osszeg += n
        db += 1

atlag = osszeg / db
print("\nA számok összege:\t" + str(osszeg) + "\nA számok száma:\t" + str(db) + "\nA számok átlaga:\t" + str(atlag))
