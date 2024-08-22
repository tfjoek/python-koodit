#  Kirjoita ohjelma, joka tervehtii sinua omalla nimelläsi.

print("Hei, Venni Limnell!")

#  Kirjoita ohjelma, joka kysyy nimesi ja sen jälkeen tervehtii sinua omalla nimelläsi.

name = input("Mikä nimesi on?")
print("Kiva tavata " + name + "!")

#  Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.

radius = float(input("Anna ympyrän säde:"))
print(3.14159 * radius ** 2)


#  Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
#  Ohjelma tulostaa suorakulmion piirin ja pinta-alan.

x = float(input("Anna suorakulmion kanta: "))
y = float(input("ja korkeus: "))
print(2 * (x + y), x * y)


#Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))
print(f"Summa: {luku1 + luku2 + luku3}, Tulo: {luku1 * luku2 * luku3}, Keskiarvo: {(luku1 + luku2 + luku3) / 3}")



#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

l = float(input("Leiviskät: "))
n = float(input("Naulat: "))
lu = float(input("Luodit: "))

grammat = l * 8516 + n * 425.6 + lu * 13.3
kg = int(grammat // 1000)
g = grammat % 1000

print(f"{kg} kg ja {g:.2f} g")

#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia

import random
kolmenumeroinen = "".join(str(random.randint(0, 9)) for _ in range(3))
nelinumeroinen = "".join(str(random.randint(1, 6)) for _ in range(4))

print(f"Kolmenumeroinen koodi: {kolmenumeroinen}, Nelinumeroinen koodi: {nelinumeroinen}")

