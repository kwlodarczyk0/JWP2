import json

class ModelAI:
    liczba_modeli = 0

    def __init__(self, nazwa_modelu,wersja):
        self.nazwa_modelu = nazwa_modelu
        self.wersja = wersja
        self.nowy_model()
    def nowy_model(self):
        ModelAI.liczba_modeli += 1

    @classmethod
    def ile_modeli(cls):
        return ModelAI.liczba_modeli
    @classmethod
    def z_pliku(cls,nazwa_pliku):
        with open(nazwa_pliku,'r') as f:
            data = json.load(f)
            nazwa_modelu=data['name']
            version = data['version']
        return cls(nazwa_modelu,version)



model = ModelAI.z_pliku('model.json')
model_2 = ModelAI("model_test",1.0)

print("Ilosc modeli:",ModelAI.ile_modeli())