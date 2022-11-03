import unittest

from ..Konto import Konto


class TestMoneyTransfer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    

    def test_udane_ksiegowanie_przelewu(self):
        konto1 = Konto("Konto", "Pierwsze", "12345678901")
        konto2 = Konto("Konto", "Drugie", "12345678901")

        konto1.saldo = 1000
        konto1.zaksieguj_przelew(200, konto2)

        self.assertEqual(konto1.saldo, 800, "Pieniądze nie zostały zaksięgowane!")
    
    
    def test_nieudane_ksiegowanie_przelewu(self):
        konto1 = Konto("Konto", "Pierwsze", "12345678901")
        konto2 = Konto("Konto", "Drugie", "12345678901")

        konto1.saldo = 200
        konto1.zaksieguj_przelew(1000, konto2)

        self.assertEqual(konto1.saldo, 200, "Saldo się nie zgadza!")
