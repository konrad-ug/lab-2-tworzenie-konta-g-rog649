import unittest

from app.tests import KontoFirmoweMock

from ..KontoFirmowe import KontoFirmowe


class TestMoneyTransfer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.nazwa_firmy = "Januszex sp. z o.o."
        cls.nip = "8461627563"

    def test_tworzenie_konta(self):
        konto = KontoFirmoweMock(self.nazwa_firmy, self.nip)
        self.assertEqual(
            konto.nazwa_firmy, self.nazwa_firmy, "Nazwa firmy nie została zapisana!"
        )
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(konto.nip, self.nip, "NIP nie został zapisany!")

    def test_zbyt_dlugi_nip(self):
        konto = KontoFirmoweMock(self.nazwa_firmy, "1234567890124525")
        self.assertEqual(
            konto.nip, "Niepoprawny NIP!", "Za długi NIP przypisany do konta!"
        )

    def test_zbyt_krotki_nip(self):
        konto = KontoFirmoweMock(self.nazwa_firmy, "123456")
        self.assertEqual(
            konto.nip, "Niepoprawny NIP!", "Za krótki NIP przypisany do konta!"
        )
    
    def test_niepoprawny_nip(self):
        konto = KontoFirmowe(self.nazwa_firmy, "0000000000")
        self.assertNotEqual(konto.nip, "0000000000", "Nieprawidłowy numer NIP!")
    
    def test_poprawny_nip(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        self.assertEqual(konto.nip, self.nip, "Prawidłowy numer NIP nie przypisany do konta!")
