class Telefon:
    def __init__(self, model,producent,komunikacja,rozrywka):
        self.model = model
        self.producent = producent
        self.komunikacja = komunikacja
        self.rozrywka = rozrywka

class Komunikacja:
    def wyslij_wiadomosci(self,odbiorca,tresc):
        print(f"Wiadomość {tresc} wysłana do odbiorcy {odbiorca}")


class Rozrywka:
    def odtworz_muzyke(self,utwor):
        print(f"Utwór do odegrania: {utwor}")


# class Smartphone(Telefon):
#     def __init__(self,model,producent,komunikacja,rozrywka):
#         super().__init__(model,producent)
#         self.komunikacja = komunikacja
#         self.rozrywka = rozrywka

komunikacja = Komunikacja()
rozrywka = Rozrywka()

tel = Telefon("J20","Samsung",komunikacja,rozrywka)

tel.rozrywka.odtworz_muzyke("hymn ligi mistrzów")
tel.komunikacja.wyslij_wiadomosci("Jan", "Hello world")
