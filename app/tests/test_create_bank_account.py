import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "97012663712"

        pierwsze_konto = Konto(imie, nazwisko, pesel)
        self.assertEqual(pierwsze_konto.imie, imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.pesel, pesel, "PESEL nie został zapisany!")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "PESEL ma złą długość!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

        rabat = "PROM_R3&"
        konto_rabat = Konto(imie, nazwisko, pesel, rabat=rabat)
        self.assertEqual(konto_rabat.saldo, 50, "Konto nie otrzymało rabatu!")

    #tutaj proszę dodawać nowe testy