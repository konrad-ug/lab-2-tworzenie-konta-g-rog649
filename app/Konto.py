from datetime import date

class Konto:
    def __init__(self, imie, nazwisko, pesel, rabat=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.transfer_costs = {"zwykły": 0, "ekspresowy": 1}
        self.historia = []

        rabat_start = "PROM_"
        rabat_chars = 3
        rabat_correct = (
            rabat is not None
            and rabat.startswith(rabat_start)
            and len(rabat) == len(rabat_start) + rabat_chars
        )

        pesel_year = int(pesel[0:2])
        pesel_month = int(pesel[2:4])
        elderly = (
            # 1800-1899
            pesel_month >= 81
            # 1900-1959
            or (pesel_month <= 12 and pesel_year < 60)
        )

        if rabat_correct and not elderly:
            self.saldo = 50
        else:
            self.saldo = 0

        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"

    def zmien_stan_konta(self, kwota):
        if kwota != 0:
            self.saldo += kwota
            self.historia.append(kwota)

    def zaksieguj_przelew(self, kwota, konto, rodzaj="zwykły"):
        if self.saldo >= kwota:
            self.zmien_stan_konta(-kwota)
            self.zmien_stan_konta(-self.transfer_costs[rodzaj])
            konto.zmien_stan_konta(kwota)

    def zaciagnij_kredyt(self, kwota):
        last_payments = (
            len(self.historia) >= 3
            and all(amount > 0 for amount in self.historia[-3:])
        )
        last_sum = (
            len(self.historia) >= 5
            and sum(self.historia[-5:]) > kwota
        )

        if not (last_payments or last_sum):
            return False
        
        self.saldo += kwota
        return True
    
    def send_history_mail(self, mail, connection):
        success = connection.send_mail(
            mail,
            f"Wyciąg z dnia {date.today()}",
            f"Twoja historia konta to: {self.historia}"
        )

        return success
