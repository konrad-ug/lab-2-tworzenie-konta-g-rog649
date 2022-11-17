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

    def zaciagnij_kredyt(self, kwota):
        amount_twice_balance = self.saldo >= 2 * kwota
        contains_zus = -1775 in self.historia

        if amount_twice_balance and contains_zus:
            self.saldo += kwota
            return True
        
        return False
