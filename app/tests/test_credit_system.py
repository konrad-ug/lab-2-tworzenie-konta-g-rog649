import unittest
from parameterized import parameterized

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestCreditSystem(unittest.TestCase):
    def setUp(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "87013092831"
        self.konto = Konto(imie, nazwisko, pesel)

        nazwa_firmy = "Januszex sp. z o.o."
        nip = "8461627563"
        
        self.kontoFirmowe = KontoFirmowe(nazwa_firmy, nip)
        self.messages = [
            "Kredyt został zaciągnięty, a nie powinien być!",
            "Kredyt nie został zaciągnięty, a powinien być!"
        ]
    
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
        self.konto.historia = historia
        zaciagniety = self.konto.zaciagnij_kredyt(kwota)
        self.assertEqual(zaciagniety, udany, self.messages[udany])


    @parameterized.expand([
        # Saldo nie 2 razy większe, niż zaciągnięta kwota
        [[1775], 1000, 1000, False],
        [[1775], 1000, 2000, False],
        # W historii brak przelewu do ZUS
        [[], 1000, 2001, False],
        [[1324], 1000, 2001, False],
        # Oba warunki spełnone
        [[1775], 1000, 2001, True],
        [[-300, 1775, -500], 1000, 2001, True]
    ])
    def test_kredyt_konto_firmowe(self, historia, saldo, kwota, udany):
        self.kontoFirmowe.historia = historia
        self.kontoFirmowe.saldo = saldo
        zaciagniety = self.kontoFirmowe.zaciagnij_kredyt(kwota)
        self.assertEqual(zaciagniety, udany, self.messages[udany])
