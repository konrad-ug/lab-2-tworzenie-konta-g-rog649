from app.Konto import Konto


class KontoFirmowe(Konto):
    def __init__(self, nazwa_firmy, nip):
        self.nazwa_firmy = nazwa_firmy
        self.saldo = 0

        if KontoFirmowe.czy_poprawny_nip(nip):
            self.nip = nip
        else:
            self.nip = "Niepoprawny NIP!"
    

    @classmethod
    def czy_poprawny_nip(cls, nip):
        return len(nip) == 10


    def zaksieguj_przelew(self, kwota, rodzaj="zwykły"):
        if self.saldo >= kwota:
            self.saldo -= kwota

            if rodzaj == "ekspresowy":
                self.saldo -= 5
