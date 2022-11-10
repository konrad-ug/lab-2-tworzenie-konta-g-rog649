import unittest

from ..Konto import Konto


class TestCreditSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.imie = "Dariusz"
        cls.nazwisko = "Januszewski"
        cls.pesel = "87013092831"

    def test_kredyt_nie_udzielony(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        zaciagniety = konto.zaciagnij_kredyt(500)
        self.assertFalse(zaciagniety, "Kredyt został zaciągnięty, a nie powinien być!")
    
    def test_kredyt_udzielony_wplaty(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [-100, 100, 100, 100]
        zaciagniety = konto.zaciagnij_kredyt(500)
        self.assertEqual(konto.saldo, 500, "Saldo się nie zgadza!")
        self.assertTrue(zaciagniety, "Kredyt nie został zaciągnięty, a powinien być!")
    
    def test_kredyt_udzielony_transakcje(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [-1000, 100, -200, 100, 800, -200]
        zaciagniety = konto.zaciagnij_kredyt(500)
        self.assertEqual(konto.saldo, 500, "Saldo się nie zgadza!")
        self.assertTrue(zaciagniety, "Kredyt nie został zaciągnięty, a powinien być!")
