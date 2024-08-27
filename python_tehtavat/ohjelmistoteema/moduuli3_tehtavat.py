#  Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. 
#  Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, 
#  montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm

kuha = float(input("Anna kuhan pituus (cm): "))
alaraja = 37.0
if kuha < alaraja:
    puuttuu = alaraja - kuha
    print(f"Kuha on alamittainen. Laske se takaisin järveen. Se on {puuttuu} cm liian lyhyt.")
else:
    print("Kuha on hyvä voit pitää sen.")

#  Kirjoita ohjelma, joka kysyy käyttäjältä laivan 
#  hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen
#  kuvauksen alla olevan luettelon mukaisesti. 

hyttiluokka = input("Anna hyttiluokka (LUX, A, B tai C): ").upper()
if hyttiluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")

#  Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen
#  ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa,
#  onko hemoglobiiniarvo alhainen, normaali vai korkea.

sukupuoli = input("Anna biologinen sukupuolesi: ").lower()
hemoglobiini = int(input("Anna hemoglobiiniarvosi (g/1): "))
if sukupuoli == "mies":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 117 <= hemoglobiini <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")
elif sukupuoli == "nainen":
    if hemoglobiini < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 134 <= hemoglobiini <= 195:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")
else:
    print("Anna biologinen sukupuolesi oikein.")


#  Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.

vuosi = int(input("Anna vuosiluku: "))
if vuosi % 400 == 0:
    print(f"{vuosi} on karkausvuosi.")
elif vuosi % 100 == 0:
    print(f"{vuosi} ei ole karkausvuosi.")
elif vuosi % 4 == 0:
    print(f"{vuosi} on karkausvuosi.")
else:
    print(f"{vuosi} ei ole karkausvuosi.")







