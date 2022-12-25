import os
from app.Konto import Konto
import requests
from datetime import date

_url = os.getenv("BANK_APP_MF_URL", "https://wl-api.mf.gov.pl")

class KontoFirmowe(Konto):
    def __init__(self, nazwa_firmy, nip):
        self.nazwa_firmy = nazwa_firmy
        self.saldo = 0
        self.transfer_costs = {"zwykły": 0, "ekspresowy": 5}
        self.historia = []

        nip_errors = self.czy_poprawny_nip(nip)
        self.nip = {
            "": nip,
            "incorrect": "Pranie!",
            "length": "Niepoprawny NIP!"
        }[nip_errors]

    @classmethod
    def czy_poprawny_nip(cls, nip):
        if len(nip) != 10: return "length"
        curr_date = date.today()
        nip_url = f"{_url}/api/search/nip/{nip}?date={curr_date}"
        response = requests.get(nip_url)
        if response.status_code != 200:
            return "incorrect"
        
        response_json = response.json()
        if response_json["result"]["subject"] is None:
            return "incorrect"
        
        return ""

    def zaciagnij_kredyt(self, kwota):
        amount_twice_balance = self.saldo >= 2 * kwota
        contains_zus = -1775 in self.historia

        if amount_twice_balance and contains_zus:
            self.saldo += kwota
            return True
        
        return False
