import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit

auto = Auto("ABC-123", 142)
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
auto.kiihdyta(-200)

autot = [Auto(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]

while all(auto.kuljettu_matka < 10000 for auto in autot):
    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje(1)

print(f"{'Rekisteritunnus':<15}{'Huippunopeus':<15}{'Nopeus':<10}{'Kuljettu matka':<15}")
print("-" * 55)
for auto in autot:
    print(f"{auto.rekisteritunnus:<15}{auto.huippunopeus:<15}{auto.nopeus:<10}{auto.kuljettu_matka:<15}")
