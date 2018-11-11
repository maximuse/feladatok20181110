# Kérj be egy egész számot, és állapítsa meg, hogy hány 0 jegy szerepel benne!

n = input("szám: ")
db = 0

for i in n:
    if i == '0':
        db += 1

print("A " + str(n) + " " + str(db) + " db 0-t tartalmaz.")
