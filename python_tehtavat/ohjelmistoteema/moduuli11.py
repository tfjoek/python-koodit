class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matkamittari = 0

    def aseta_nopeus(self, nopeus):
        if 0 <= nopeus <= self.huippunopeus:
            self.nopeus = nopeus
        else:
            print("Nopeus ei voi ylittää huippunopeutta tai olla negatiivinen.")

    def aja(self, tuntia):
        self.matkamittari += self.nopeus * tuntia

    def tulosta_tiedot(self):
        print(f'Rekisteritunnus: {self.rekisteritunnus}, Huippunopeus: {self.huippunopeus} km/h, Matkamittari: {self.matkamittari:.2f} km')


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Akkukapasiteetti: {self.akkukapasiteetti} kWh')


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Bensatankin koko: {self.bensatankin_koko} l')


# Pääohjelma
if __name__ == "__main__":
    sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    sahkoauto.aseta_nopeus(150)
    polttomoottoriauto.aseta_nopeus(120)
    sahkoauto.aja(3)
    polttomoottoriauto.aja(3)

    sahkoauto.tulosta_tiedot()
    print()  # Tyhjää riviä erottamaan autot
    polttomoottoriauto.tulosta_tiedot()
