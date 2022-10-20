class Konto:
    def __init__(self, imie, nazwisko, pesel, rabat=""):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel

        if rabat.startswith("PROM_") and len(rabat) == 8:
            account_year = int(pesel[0:1])
            account_month = int(pesel[2:3])

            if account_year >= 60 or (21 <= account_month <= 72):
                self.saldo = 50
        else:
            self.saldo = 0
