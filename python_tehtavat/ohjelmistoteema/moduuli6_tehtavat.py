#T1
import random
def heitä_noppa():
    return random.randint(1,6)

def pääohjelma1():
    silmäluku = 0
    while silmäluku != 6:
        silmäluku = heitä_noppa()
        print(f"Nopan silmäluku: {silmäluku}")
pääohjelma1()

#T2
import random

def heitä_noppa(tahkot):
    return random.randint(1, tahkot)

def pääohjelma2():
    tahkojen_määrä = int(input("Anna nopan tahkojen määrä: "))
    silmäluku = 0
    while silmäluku != tahkojen_määrä:
        silmäluku = heitä_noppa(tahkojen_määrä)
        print(f"Nopan silmäluku: {silmäluku}")

pääohjelma2()

#T3
def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

def pääohjelma3():
    while True:
        gallonat = float(input("Anna bensiinin määrä gallonoina (negatiivinen luku lopettaa): "))
        if gallonat < 0:
            break
        litrat = gallonat_litroiksi(gallonat)
        print(f"{gallonat} gallonaa on {litrat:.2f} litraa.")

pääohjelma3()

#T4
def laske_summa(luvut):
    return sum(luvut)

def pääohjelma4():
    luvut = [1, 2, 3, 4, 5, 6, 7 , 9, 10]
    summa = laske_summa(luvut)
    print(f"Listan {luvut} summa on: {summa}")

pääohjelma4()

#T5

def poista_parittomat(luvut):
    return [luku for luku in luvut if luku % 2 == 0]

def pääohjelma5():
    alkuperäinen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    karsittu_lista = poista_parittomat(alkuperäinen_lista)
    
    print(f"Alkuperäinn lista: {alkuperäinen_lista}")
    print(f"Parilliset luvut lista: {karsittu_lista}")

pääohjelma5()

#T6
import math

def yksikkohinta(halkaisija, hinta):
    return hinta / (math.pi * (halkaisija / 2) ** 2)

halkaisija1 = float(input("Anna ekan pizzan halkaisija: "))
hinta1 = float(input("Anna ekan pizzan hinta: "))

halkaisija2 = float(input("Anna tokan pizzan halkaisija: "))
hinta2 = float(input("Anna tokan pizzan hinta: "))

yksikkohinta1 = yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = yksikkohinta(halkaisija2, hinta2)

print(f"ekan pizza yksikköhinta: {yksikkohinta1:.2f} euroa/neliömetri")
print(f"toka pizzan yksikköhinta: {yksikkohinta2:.2f} euroa/neliömetri")
if yksikkohinta1 < yksikkohinta2:
    print("eka pizza on edullisempi.")
elif yksikkohinta1 > yksikkohinta2:
    print("toka pizza on edullisempi.")
else:
    print("Yhtä edullisia.")
