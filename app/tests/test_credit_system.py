import unittest
from parameterized import parameterized

from ..Konto import Konto


class TestCreditSystem(unittest.TestCase):
    def setUp(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "87013092831"
        self.konto = Konto(imie, nazwisko, pesel)
    
    @parameterized.expand([
        [[-100, 100, -200, 100, 100]],
        [[]]
    ])
    def test_kredyt_nie_udzielony(self, historia):
        self.konto.historia = historia
        zaciagniety = self.konto.zaciagnij_kredyt(500)
        self.assertFalse(zaciagniety, "Kredyt został zaciągnięty, a nie powinien być!")
    
    @parameterized.expand([
        [[-100, 100, 100, 100]],
        [[-200, -300, 200, 100, 50]],
        [[-500, -400, -600, 300, 1000, 500]],
    ])
    def test_kredyt_udzielony_wplaty(self, historia):
        self.konto.historia = historia
        zaciagniety = self.konto.zaciagnij_kredyt(500)
        self.assertEqual(self.konto.saldo, 500, "Saldo się nie zgadza!")
        self.assertTrue(zaciagniety, "Kredyt nie został zaciągnięty, a powinien być!")
    
    @parameterized.expand([
        [[-1000, 100, -200, 100, 800, -200]],
        [[-300, 200, 300, -100, 300, -100, 200]],
        [[-300, 200, -1000, -100, 300, 200, 400, -200]],
    ])
    def test_kredyt_udzielony_transakcje(self, historia):
        self.konto.historia = historia
        zaciagniety = self.konto.zaciagnij_kredyt(500)
        self.assertEqual(self.konto.saldo, 500, "Saldo się nie zgadza!")
        self.assertTrue(zaciagniety, "Kredyt nie został zaciągnięty, a powinien być!")
