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
        # Nie udzielenie
        [[-100, 100, -200, 100, 100], 500, False],
        # Wpłata - trzy ostatnie dodatnie
        [[-100, 100, 100, 100], 500, True],
        [[-200, -300, 200, 100, 50], 600, True],
        [[-500, -400, -600, 300, 1000, 500], 700, True],
        # Wpłata - suma 5 większa, niż kwota
        [[-1000, 100, -200, 100, 800, -200], 550, True],
        [[-300, 200, 300, -100, 300, -100, 200], 100, True],
        [[-300, 200, -1000, -100, 300, 200, 400, -200], 350, True],
    ])
    def test_kredyt(self, historia, kwota, udany):
        messages = [
            "Kredyt został zaciągnięty, a nie powinien być!",
            "Kredyt nie został zaciągnięty, a powinien być!"
        ]
        self.konto.historia = historia
        zaciagniety = self.konto.zaciagnij_kredyt(kwota)
        self.assertEqual(zaciagniety, udany, messages[udany])

