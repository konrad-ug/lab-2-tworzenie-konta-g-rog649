import unittest

from ..Konto import Konto


class TestTransferHistory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    

    def test_historia_przelew_zwykły(self):
        konto1 = Konto("Konto", "Pierwsze", "12345678901")
        konto2 = Konto("Konto", "Drugie", "12345678901")

        konto1.zaksieguj_przelew(500, konto2)
        konto2.zaksieguj_przelew(300, konto1)

        self.assertListEqual(konto1.historia, [-500, 300], "Zła historia przelewów konta 1!")
        self.assertListEqual(konto2.historia, [500, -300], "Zła historia przelewów konta 2!")
    

    def test_historia_przelew_ekspresowy(self):
        konto1 = Konto("Konto", "Pierwsze", "12345678901")
        konto2 = Konto("Konto", "Drugie", "12345678901")

        konto1.zaksieguj_przelew(500, konto2, rodzaj="ekspresowy")
        konto2.zaksieguj_przelew(300, konto1, rodzaj="ekspresowy")

        self.assertListEqual(
            konto2.historia,
            [-500, -konto1.transfer_costs["ekspresowy"], -300],
            "Zła historia przelewów konta 1!"
        )
        self.assertListEqual(
            konto2.historia,
            [500, -300, -konto2.transfer_costs["ekspresowy"]],
            "Zła historia przelewów konta 2!")
