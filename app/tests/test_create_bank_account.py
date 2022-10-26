import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    def test_tworzenie_konta(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "87013092831"

        pierwsze_konto = Konto(imie, nazwisko, pesel)
        self.assertEqual(pierwsze_konto.imie, imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

        # PESEL
        self.assertEqual(pierwsze_konto.pesel, pesel, "PESEL nie został zapisany!")

        konto_pesel = Konto(imie, nazwisko, "1234")
        self.assertEqual(konto_pesel.pesel, "Niepoprawny pesel!", "Wpisany zły PESEL do konta!")
