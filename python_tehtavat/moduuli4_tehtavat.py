#T1
import random
lukumaara = int(input("Kuinka monta arpakuutiota heität? "))
summa = 0
for i in range(lukumaara):
    heitto = random.randint(1, 6)
    summa += heitto
print(f"Arpakuutioiden silmälukujen määrä on {summa}")
#T2
luvut = []
while True:
    syote = input("Anna luku) ")
    if syote == "": 
        break
    
    try:
        luku = int(syote)
        luvut.append(luku)
    except ValueError:
        print("Ei luku")
luvut.sort(reverse=True)

print("Viisi suurinta lukua ovat:")
for luku in luvut[:5]: 
    print(luku)

#T3

