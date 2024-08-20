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

#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.