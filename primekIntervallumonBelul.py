# Adott két szám között hány darab prímszám van? Írjuk is ki őket!


def is_prime(n):
    if n == 1:
        return False

    if n == 2:
        return True

    for i in range(2, n, 1):
        if n % i == 0:
            return False

    return True


a = int(input("mettől: "))
b = int(input("meddig: "))
db = 0
primek = ""

print("\nA(z) " + str(a) + " és a(z) " + str(b) + " között ", end='')

while a <= b:
    if is_prime(a):
        # print(str(a) + " ", end='')
        primek += str(a) + " "
        db += 1
    a += 1

print(str(db) + " db prímszám ( " + primek + ") van.")
