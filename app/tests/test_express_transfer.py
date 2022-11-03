import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe


class TestExpressTransfer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.imie = "Dariusz"
        cls.nazwisko = "Januszewski"
        cls.pesel = "87013092831"

        cls.nazwa_firmy = "Januszex sp. z o.o."
        cls.nip = "8461627563"
    

    def test_udany_przelew_ekspresowy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto.zaksieguj_przelew(400, rodzaj="ekspresowy")
        self.assertEqual(konto.saldo, 99, "Saldo się nie zgadza!")

    
    def test_nieudany_przelew_ekspresowy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto.zaksieguj_przelew(600, rodzaj="ekspresowy")
        self.assertEqual(konto.saldo, 500, "Saldo się zmieniło!")


    def test_udany_przelew_ekspresowy_konto_firmowe(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 500
        konto.zaksieguj_przelew(400, rodzaj="ekspresowy")
        self.assertEqual(konto.saldo, 95, "Saldo nie jest poprawne!")


    def test_udany_przelew_ekspresowy_saldo_ponizej_0(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 500
        konto.zaksieguj_przelew(600, rodzaj="ekspresowy")
        self.assertEqual(konto.saldo, 500, "Saldo nie jest poprawne!")
