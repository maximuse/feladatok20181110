# Kérjük be, hogy a héten mennyi kalóriát fogyasztottunk az egyes napokon! Ezután írjuk ki az összes
# kalóriafogyasztásunkat, valamint a napi átlag kalóriafogyasztást, illetve, hogy hányadik napon fogyasztottuk a
# legtöbb és a legkevesebb kalóriát!

bevittKaloria = []
napokSzama = 7
osszeg = 0
legtobbIndex = 0
legkevesebbIndex = 0

for i in range(napokSzama):
    n = int(input(str(i+1) + ". nap: "))
    bevittKaloria.insert(i, n)
    osszeg += n

legtobb = bevittKaloria[0]
legkevesebb = bevittKaloria[0]

for j in bevittKaloria:
    if j >= legtobb:
        legtobbIndex = bevittKaloria.index(j)
        legtobb = j

    if j <= legkevesebb:
        legkevesebbIndex = bevittKaloria.index(j)
        legkevesebb = j

print("\nÖsszes kalóriafogyasztás: " + str(osszeg))
print("Napi átlag kalóriafogyasztást: " + str(osszeg / napokSzama))
print("A legtöbb kalóriát (" + str(bevittKaloria[legtobbIndex]) + ") a(z) " + str(legtobbIndex + 1) + ". napon fogyasztotta.")
print("A legkevesebb kalóriát (" + str(bevittKaloria[legkevesebbIndex]) + ") a(z) " + str(legkevesebbIndex + 1) + ". napon fogyasztotta.")
