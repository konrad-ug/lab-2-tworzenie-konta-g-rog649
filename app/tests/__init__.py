from ..KontoFirmowe import KontoFirmowe

class KontoFirmoweMock(KontoFirmowe):
    @classmethod
    def czy_poprawny_nip(cls, nip):
        if len(nip) != 10: return "length"
        return ""
