from zbozi import Zbozi

class ZlevneneZbozi(Zbozi):
    def __init__(self, nazev, cena, sleva):
        """
        Nastavi cenu, nazev zbozi a slevu
        :param nazev: str Nazev jen znaky anglicke abecedy 2-50
        :param cena: float 0 az 1mio, kladne cislo
        :param sleva: float 0.0 az 0.5, vyse slevy v procentech
        """
        super().__init__(nazev, cena)
        if type(sleva) is not float or not (0.0 <= sleva <= 0.5):
            raise Exception('Sleva musi byt cislo mezi 0.0 a 0.5')
        self._sleva = sleva

    def get_cena(self):
        """
        Vrati cenu po sleve
        :return: float
        """
        return self._cena * (1 - self._sleva)