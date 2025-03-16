class Osoba:
    def __init__(self, imie,nazwisko,wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko}."

class Pracownik(Osoba):
    def __init__(self, imie,nazwisko,wiek,stanowisko,pensja):
        Osoba.__init__(self, imie,nazwisko,wiek)
        self.stanowisko = stanowisko
        self.pensja = pensja

    def info_o_pracy(self):
        return f"Pracuję jako {self.stanowisko}, zarabiam {self.pensja} zł."


class Manager(Pracownik):
    def __init__(self, imie,nazwisko,wiek,stanowisko,pensja):
        Pracownik.__init__(self, imie,nazwisko,wiek,stanowisko,pensja)
        self.zespol = []

    def dodaj_do_zespolu(self,pracownik):
        self.zespol.append(pracownik)

    def przedstaw_sie(self):
       return Osoba.przedstaw_sie(self) + f"Ilosc podwladnych: {len(self.zespol)}"


manager = Manager("Krystian","Włodarczyk",25,"CEO",20000.0)

pracownik_1 = Pracownik("John","Doe",20,"Programist",100000.0)
pracownik_2 = Pracownik("Alice","Doe",23,"Programist",80000.0)

manager.dodaj_do_zespolu(pracownik_1)
manager.dodaj_do_zespolu(pracownik_2)

print(manager.przedstaw_sie())
print(manager.info_o_pracy())

print(pracownik_1.przedstaw_sie())
print(pracownik_2.info_o_pracy())