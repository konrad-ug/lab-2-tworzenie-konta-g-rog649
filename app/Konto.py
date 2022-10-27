class Konto:
    def __init__(self, imie, nazwisko, pesel, rabat=None):
        self.imie = imie
        self.nazwisko = nazwisko

        rabat_start = "PROM_"
        rabat_chars = 3
        rabat_correct = (
            rabat is not None
            and rabat.startswith(rabat_start)
            and len(rabat) == len(rabat_start) + rabat_chars
        )
        
        pesel_year = int(pesel[0:2])
        pesel_month = int(pesel[2:4])
        elderly = (
            # 1800-1899
            pesel_month >= 81
            # 1900-1959
            or (pesel_month <= 12 and pesel_year < 60)
        )

        if rabat_correct and not elderly:
            self.saldo = 50
        else:
            self.saldo = 0

        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"
    
    
    def zaksieguj_przelew(self, kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota
