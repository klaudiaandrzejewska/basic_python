# Stwórz klase kosmetyk z potrzebnymi wartościami takimi jak cena,rodzaj, nazwa, firma i co tam dalej zechcesz, jak storzysz klase to przyjdz/
class Kosmetyk:
    def __init__(self, firma, nazwa, rodzaj, cena):
        self.firma = firma
        self.nazwa = nazwa
        self.rodzaj = rodzaj
        self.cena = cena
        self.opis = None

    def __eq__(self, other):
        return self.nazwa == other.nazwa

    def __str__(self) -> str:
        return f"{self.firma} -  {self.nazwa} do {self.rodzaj} i kosztuje {self.cena} zł"

#
# kosmetyk_1 = Kosmetyk('anwen', 'pianka oczyszczająca', 'oczyszczania twarzy ', 25)
# kosmetyk_2 = Kosmetyk('anwen123', 'pianka oczyszczająca', '123oczyszczania twarzy ', 32)
# print(kosmetyk_1 == kosmetyk_2)

