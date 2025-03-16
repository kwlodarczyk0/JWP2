class Ksiazka:
    def __init__(self,tytul,autor,rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania

    def opis(self):
        return (f"Tytuł: {self.tytul} \n"
                f"Autor: {self.autor} \n"
                f"Rok wydania: {self.rok_wydania}")

class Ebook(Ksiazka):
    def __init__(self,tytul,autor,rok_wydania,rozmiar_pliku):
        Ksiazka.__init__(self,tytul,autor,rok_wydania)
        self.rozmiar_pliku = rozmiar_pliku

    def opis(self):
        return Ksiazka.opis(self)+("\n"
                                   f"Rozmar pliku: {self.rozmiar_pliku} MB")

class Audiobook(Ksiazka):
    def __init__(self,tytul,autor,rok_wydania,czas_trwania):
        Ksiazka.__init__(self,tytul,autor,rok_wydania)
        self.czas_trwania = czas_trwania

    def opis(self):
        return Ksiazka.opis(self)+("\n"
                                   f"Czas trwania: {self.czas_trwania} minut ")


ebook_1 = Ebook("Pan Tadeusz","Adam Mickiewicz",2010,"5")
print(ebook_1.opis())
print("-----------")
audiobook_1 = Audiobook("Lalka","Bolesław Prus",2022,200)
print(audiobook_1.opis())




