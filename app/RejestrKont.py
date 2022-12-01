class RejestrKont:
    konta = []
    
    @classmethod
    def dodaj_konto(cls, konto):
        cls.konta.append(konto)

    @classmethod
    def zmien_konto(cls, pesel, data):
        account = RejestrKont.wyszukaj_konto(pesel)

        allowed_keys = {"imie", "nazwisko"}
        for key, value in data.items():
            if key not in allowed_keys:
                continue

            account[key] = value
        
        return False

    @classmethod
    def ile_kont(cls):
        return len(cls.konta)
    
    @classmethod
    def wyszukaj_konto(cls, pesel):
        return next(
            (
                konto for konto in cls.konta
                if konto.pesel == pesel
            ),
            None
        )
