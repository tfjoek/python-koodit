#T1
import random
n = int(input("Kuinka monta arpakuutiota? "))
summa = 0
for i in range(n):
    heitto = random.randint(1, 6)
    summa += heitt
print("Heittojen summa:", summa)

#T2
luvut = []
while True:
    syote = input("Anna luku): ")
    if syote == "":
        break
    luvut.append(int(syote))
luvut.sort(reverse=True)
print("Viisi suurinta lukua:", luvut[:5])

#T3
luku = int(input("Anna kokonaisluku: "))
if luku < 2:
    print(f"luku {luku} ei ole alkuluku.")
else:
    on_alkuluku = True
    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            on_alkuluku = False
            break
    if on_alkuluku:
        print(f"Luku {luku} on alkuluku.")
    else:
        print(f"Luku {luku} ei ole alkuluku.")

#T4
kaupungit = []
for i in range(5):
    kaupunki = input(f"Anna kaupungin nimi {i + 1}: ")
    kaupungit.append(kaupunki)
print("Annoit kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)

