class RejestrKont:
    konta = []
    
    @classmethod
    def dodaj_konto(cls, konto):
        cls.konta.append(konto)

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
