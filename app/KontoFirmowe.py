from app.Konto import Konto


class KontoFirmowe(Konto):
    def __init__(self, nazwa_firmy, nip):
        self.nazwa_firmy = nazwa_firmy
        self.saldo = 0
        self.transfer_costs = {"zwykły": 0, "ekspresowy": 5}
        self.historia = []

        if KontoFirmowe.czy_poprawny_nip(nip):
            self.nip = nip
        else:
            self.nip = "Niepoprawny NIP!"

    @classmethod
    def czy_poprawny_nip(cls, nip):
        return len(nip) == 10
