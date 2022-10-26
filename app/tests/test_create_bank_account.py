import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.imie = "Dariusz"
        cls.nazwisko = "Januszewski"
        cls.pesel = "87013092831"
    

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

        # PESEL
        self.assertEqual(pierwsze_konto.pesel, self.pesel, "PESEL nie został zapisany!")

        konto_pesel = Konto(self.imie, self.nazwisko, "1234")
        self.assertEqual(konto_pesel.pesel, "Niepoprawny pesel!", "Wpisany zły PESEL do konta!")
    

    def test_rabat(self):
        rabat_start = "PROM_"
        rabat_znaki = "R&3"

        konto_rabat = Konto(self.imie, self.nazwisko, self.pesel, rabat=rabat_start + rabat_znaki)
        self.assertEqual(konto_rabat.saldo, 50, "Konto nie dostało rabatu!")
