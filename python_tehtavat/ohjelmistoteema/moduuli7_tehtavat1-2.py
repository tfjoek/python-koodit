#T1
vuodenajat = {
    "talvi": (12, 1, 2), "kevät": (3, 4, 5), "kesä": (6, 7, 8), "syksy": (9, 10, 11)
}

kuukausi = int(input("Anna kuukauden numero 1-12: "))

if 1 <= kuukausi <= 12:
    for vuodenaika, kuukaudet in vuodenajat.items():
        if kuukausi in kuukaudet:
            print(f"{kuukausi} vastaa vuodenaikaa {vuodenaika.capitalize()}")
else:
    print("error")

#T2
nimilista = set()
while True:
    nimi = input("Anna nimi, tyhjä lopettaa: ")
    if nimi == "":
        break

    if nimi in nimilista:
        print("Nimi jo annettu")
    else:
        nimilista.add(nimi)

print("Annetut nimet:")
for nimi in nimilista:
    print(nimi)
