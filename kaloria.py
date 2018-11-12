# Kérjük be, hogy a héten mennyi kalóriát fogyasztottunk az egyes napokon! Ezután írjuk ki az összes
# kalóriafogyasztásunkat, valamint a napi átlag kalóriafogyasztást, illetve, hogy hányadik napon fogyasztottuk a
# legtöbb és a legkevesebb kalóriát!

napiBevittKaloria = []
napokSzama = 7
osszeg = 0
legtobbIndex = 0
legkevesebbIndex = 0

for i in range(napokSzama):
    n = int(input(str(i+1) + ". nap: "))
    napiBevittKaloria.insert(i, n)
    osszeg += n

legtobb = napiBevittKaloria[0]
legkevesebb = napiBevittKaloria[0]

for j in napiBevittKaloria:
    if j >= legtobb:
        legtobb = j
        legtobbIndex = napiBevittKaloria.index(j)

    if j <= legkevesebb:
        legkevesebb = j
        legkevesebbIndex = napiBevittKaloria.index(j)

print("\nÖsszes kalóriafogyasztás: " + str(osszeg))
print("Napi átlag kalóriafogyasztást: " + str(osszeg / napokSzama))
print("A legtöbb kalóriát (" + str(napiBevittKaloria[legtobbIndex]) + ") a(z) " + str(legtobbIndex+1) + ". napon fogyasztotta.")
print("A legkevesebb kalóriát (" + str(napiBevittKaloria[legkevesebbIndex]) + ") a(z) " + str(legkevesebbIndex+1) + ". napon fogyasztotta.")
