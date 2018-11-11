# Kérj be egy határszámot, majd írd ki eddig a számig az összes prímszámot!


def is_prime(n):
    if n == 1:
        return False

    if n == 2:
        return True

    for i in range(2, n, 1):
        if n % i == 0:
            return False

    return True


szam = int(input("szam: "))
i = 1

while i <= szam:
    if is_prime(i):
        print(str(i) + " ", end='')
    i += 1
