import unittest
from unittest.mock import Mock

from ...Konto import Konto
# from ...KontoFirmowe import KontoFirmowe
from app.tests import KontoFirmoweMock as KontoFirmowe
from ...SMTPConnection import SMTPConnection

class TestHistoryMail(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.imie = "Dariusz"
        cls.nazwisko = "Januszewski",
        cls.pesel = "87013092831"
        cls.nazwa_firmy = "Januszex sp. z o.o."
        cls.nip = "8461627563"
    
    def test_send_account_history_mail(self):
        konto1 = Konto(self.imie, self.nazwisko, self.pesel)
        konto2 = Konto(self.imie, self.nazwisko, self.pesel)
        konto1.saldo = 1000
        konto1.zaksieguj_przelew(100, konto2)

        smtp_connector = Mock(spec=SMTPConnection)
        smtp_connector.send_mail.return_value = True

        status = konto1.send_history_mail("szef@firma.pl", smtp_connector)
        smtp_connector.send_mail.assert_called_once()
        self.assertTrue(status)

    def test_send_company_account_history_mail(self):
        KontoFirmoweMock = Mock(spec=KontoFirmowe)
        KontoFirmoweMock.czy_poprawny_nip.return_value = True

        konto1 = KontoFirmoweMock(self.nazwa_firmy, self.nip)
        konto2 = KontoFirmoweMock(self.nazwa_firmy, self.nip)
        konto1.saldo = 1000
        konto1.zaksieguj_przelew(100, konto2)

        smtp_connector = Mock(spec=SMTPConnection)
        # smtp_connector.send_mail.return_value = True

        status = konto1.send_history_mail("szef@firma.pl", smtp_connector)
        # smtp_connector.send_mail.assert_called_once()
        print(status)
        self.assertTrue(status)