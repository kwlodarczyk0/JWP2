"""
Module docstring
"""

import dataclasses


@dataclasses.dataclass
class Ksiazka:
    """Class docstring"""

    def __init__(self, tytul, autor, dostepna=True):
        self.tytul = tytul
        self.autor = autor
        self.dostepna = dostepna


class Biblioteka:
    """Class docstring"""

    def __init__(self):
        self.lista_ksiazek = []

    def dodaj_ksiazke(self, ksiazka):
        """Method docstring"""
        self.lista_ksiazek.append(ksiazka)

    def wypozycz_ksiazke(self, tytul):
        """Method docstring"""
        for ksiazka in self.lista_ksiazek:
            if ksiazka.tytul == tytul:
                if ksiazka.dostepna is True:
                    ksiazka.dostepna = False
                    return f"Wypozyczono: {tytul}"
                return f"Ksiazka {tytul} niedostepna"
        return f"Brak ksiazki: {tytul}"

    def zwroc_ksiazke(self, tytul):
        """Method docstring"""
        for ksiazka in self.lista_ksiazek:
            if ksiazka.tytul == tytul:
                ksiazka.dostepna = True
                return f"Zwrocono: {tytul}"
        return f"Nie nalezy do biblioteki: {tytul}"

    def dostepne_ksiazki(self):
        """Method docstring"""
        dostepne = []
        for ksiazka in self.lista_ksiazek:
            if ksiazka.dostepna:
                dostepne.append(ksiazka.tytul)
        return dostepne


def main():
    """Method docstring"""
    biblioteka = Biblioteka()
    biblioteka.dodaj_ksiazke(Ksiazka("Wiedzmin", "Sapkowski"))
    biblioteka.dodaj_ksiazke(Ksiazka("Solaris", "Lem"))
    biblioteka.dodaj_ksiazke(Ksiazka("Lalka", "Prus", False))

    print(biblioteka.wypozycz_ksiazke("Solaris"))
    print(biblioteka.wypozycz_ksiazke("Lalka"))
    print(biblioteka.zwroc_ksiazke("Lalka"))
    print("Dostepne ksiazki: ", biblioteka.dostepne_ksiazki())


main()
