class Konto:
    def __init__(self, imie, nazwisko, pesel, rabat=None):
        self.imie = imie
        self.nazwisko = nazwisko

        rabat_start = "PROM_"
        rabat_chars = 3
        if (
            rabat is not None
            and rabat.startswith(rabat_start)
            and len(rabat) == len(rabat_start) + rabat_chars
        ):
            self.saldo = 50
        else:
            self.saldo = 0

        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"
