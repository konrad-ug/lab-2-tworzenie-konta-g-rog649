import unittest

from ..Konto import Konto


class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "97012663712"
        pesel_senior = "55012663712"
        pesel_junior = "01252663712"

        pierwsze_konto = Konto(imie, nazwisko, pesel)
        self.assertEqual(pierwsze_konto.imie, imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.pesel, pesel, "PESEL nie został zapisany!")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "PESEL ma złą długość!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

        rabat_start = "PROM_"
        konto_rabat = Konto(imie, nazwisko, pesel, rabat=rabat_start + "R3&")
        self.assertEqual(konto_rabat.saldo, 50, "Konto nie otrzymało rabatu!")

        konto_rabat_znaki_plus = Konto(imie, nazwisko, pesel, rabat=rabat_start + "R3&7")
        self.assertEqual(konto_rabat_znaki_plus.saldo, 0, "Konto otrzymało rabat (za dużo znaków)!")

        konto_rabat_znaki_minus = Konto(imie, nazwisko, pesel, rabat=rabat_start + "R3")
        self.assertEqual(konto_rabat_znaki_minus.saldo, 0, "Konto otrzymało rabat (za mało znaków)!")

        konto_rabat_znaki_start = Konto(imie, nazwisko, pesel, rabat="ABCD_" + "R3&")
        self.assertEqual(konto_rabat_znaki_start.saldo, 0, "Konto otrzymało rabat (zły początek kodu)!")

        konto_rabat_senior = Konto(imie, nazwisko, pesel_senior, rabat=rabat_start + "R3&")
        self.assertEqual(konto_rabat_senior.saldo, 0, "Senior dostał rabat!")

        konto_rabat_senior = Konto(imie, nazwisko, pesel_senior, rabat=rabat_start + "R3&")
        self.assertEqual(konto_rabat_senior.saldo, 50, "Junior nie dostał rabatu!")
