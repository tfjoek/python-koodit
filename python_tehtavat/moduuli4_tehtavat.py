#T1
luku = 1

while luku <= 1000:
    if luku % 3 == 0:
        print(luku)
    luku += 1

#T2
while True:
    tuumat = float(input("Anna tuumien määrä: "))
    if tuumat < 0:
        break
    sentit = tuumat * 2.54
    print(f"{tuumat} tuumaa on {sentit} senttimetriä")

#T3
luvut = []
while True:
    luku3 = input("Anna luku: ")
    if luku3 == "":
        break
    luvut.append(float(luku3))

if luvut:
    pienin = min(luvut)
    suurin = max(luvut)
    print(f"Pienin luku on {pienin}")
    print(f"Suurin luku on {suurin}")
else:
    print("Lukua ei syötetty")

#T4
import random
oikea = random.randint(1, 10)
while True:
    arvaus = int(input("Arvaa luku väliltä 1-10: "))
    
    if arvaus < oikea:
        print("Liian pieni arvaus")
    elif arvaus > oikea:
        print("Liian suuri arvaus")
    else:
        print("Oikein!")
        break

#T5
oikeatunnus = "python"
oikeasalasana = "rules"
yritykset = 0
while yritykset < 5:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")

    if tunnus == oikeatunnus and salasana == oikeasalasana:
        print("Tervetuloa")
        break
    else:
        yritykset += 1

if yritykset == 5:
    print("Pääsy evätty")

#T6, tää aika vaikee en tiiä ees tajuksinks kokonaan
N = int(input("Arvottavien pisteen määrä: "))
n = 0
for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    if x**2 + y**2 < 1:
        n += 1

pi_arvio = 4 * n / N
print(f"Piin likiarvo on: {pi_arvio}")