class Konto:
    def __init__(self, imie, nazwisko, pesel, rabat=""):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel

        if rabat.startswith("PROM_") and len(rabat) == 8:
            self.saldo = 50
        else:
            self.saldo = 0
