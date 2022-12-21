import unittest

from ..Konto import Konto
from ..RejestrKont import RejestrKont

class TestAccountRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        imie1 = "Dariusz"
        nazwisko1 = "Januszewski"
        pesel1 = "87013092831"
        cls.konto1 = Konto(imie1, nazwisko1, pesel1)

        imie2 = "Dariusz"
        nazwisko2 = "Januszewski"
        pesel2 = "94120294917"
        cls.konto2 = Konto(imie2, nazwisko2, pesel2)
    
    def tearDown(self):
        RejestrKont.konta = []
    
    @classmethod
    def tearDownClass(cls):
        RejestrKont.konta = []
    
    def test_ile_kont(self):
        self.assertEqual(RejestrKont.ile_kont(), 0)

        RejestrKont.dodaj_konto(self.konto1)
        self.assertEqual(RejestrKont.ile_kont(), 1)

        RejestrKont.dodaj_konto(self.konto2)
        self.assertEqual(RejestrKont.ile_kont(), 2)
    
    def test_dodaj_konto(self):
        RejestrKont.dodaj_konto(self.konto1)
        self.assertListEqual(RejestrKont.konta, [self.konto1], "Konto nie zostało dodane!")

    def test_wyszukaj_konto(self):
        RejestrKont.dodaj_konto(self.konto1)
        RejestrKont.dodaj_konto(self.konto2)
        found_account = RejestrKont.wyszukaj_konto(self.konto2.pesel)
        self.assertEqual(found_account, self.konto2, "Złe konto znalezione!")
    
    def test_usun_konto(self):
        RejestrKont.dodaj_konto(self.konto1)
        RejestrKont.dodaj_konto(self.konto2)
        RejestrKont.usun_konto(self.konto1.pesel)
        self.assertEqual(RejestrKont.ile_kont(), 1, "Konto nie zostało usunięte!")
    
    def test_zmien_konto(self):
        RejestrKont.dodaj_konto(self.konto1)
        RejestrKont.zmien_konto(self.konto1.pesel, {"imie": "Grzegorz", "pesel": "nieZmieniaj"})
        found_account = RejestrKont.wyszukaj_konto(self.konto1.pesel)
        self.assertEqual(found_account.imie, "Grzegorz", "Imię nie zmieniło się!")
        self.assertEqual(found_account.pesel, self.konto1.pesel, "Pesel zmienił się!")
