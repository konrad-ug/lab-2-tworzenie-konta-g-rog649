import unittest
from unittest.mock import Mock

from ...Konto import Konto
from ...SMTPConnection import SMTPConnection

class TestHistoryMail(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.imie = "Dariusz"
        cls.nazwisko = "Januszewski",
        cls.pesel = "87013092831"
    
    def test_send_history_mail(self):
        konto1 = Konto(self.imie, self.nazwisko, self.pesel)
        konto2 = Konto(self.imie, self.nazwisko, self.pesel)
        konto1.saldo = 1000
        konto1.zaksieguj_przelew(100, konto2)

        smtp_connector = Mock(spec=SMTPConnection)

        status = konto1.send_history_mail("szef@firma.pl", smtp_connector)
        smtp_connector.send_mail().assert_called_once()
        self.assertTrue(status)
