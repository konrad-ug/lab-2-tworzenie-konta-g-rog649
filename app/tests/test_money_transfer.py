import unittest

from ..Konto import Konto


class TestMoneyTransfer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    

    def test_udane_ksiegowanie_przelewu(self):
        konto = Konto("Jakieś", "Konto", "12345678901")

        konto.saldo = 1000
        konto.zaksieguj_przelew(200)

        self.assertEqual(konto.saldo, 800, "Pieniądze nie zostały zaksięgowane!")
    
    
    def test_nieudane_ksiegowanie_przelewu(self):
        konto = Konto("Jakieś", "Konto", "12345678901")

        konto.saldo = 200
        konto.zaksieguj_przelew(1000)

        self.assertEqual(konto.saldo, 200, "Saldo się nie zgadza!")
