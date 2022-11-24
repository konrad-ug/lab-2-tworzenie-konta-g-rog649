import unittest

from ../RejestrKont import RejestrKont

class TestAccountRegister(unittest.TestCase):
    def setUp(self):
        imie1 = "Dariusz"
        nazwisko1 = "Januszewski"
        pesel1 = "87013092831"
        self.konto1 = Konto(imie1, nazwisko1, pesel1)

        imie2 = "Dariusz"
        nazwisko2 = "Januszewski"
        pesel2 = "94120294917"
        self.konto2 = Konto(imie, nazwisko, pesel)
    
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
        found_account = RejestrKont.wyszukaj_konto(pesel2)
        self.assertEqual(found_account, konto2, "Złe konto znalezione!")
    