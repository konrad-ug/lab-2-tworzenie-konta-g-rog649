import unittest

from ..Konto import Konto


class TestTransferHistory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    

    def test_historia_przelewów(self):
        konto1 = Konto("Konto", "Pierwsze", "12345678901")
        konto2 = Konto("Konto", "Drugie", "12345678901")

        konto1.zaksieguj_przelew(500, konto2)
        konto2.zaksieguj_przelew(300, konto1)

        self.assertEqual(konto2.historia, [500, -300], "Zła historia przelewów!")
