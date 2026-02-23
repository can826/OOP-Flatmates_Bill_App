class Rechnung():
    """
    Klasse enthält die Daten einer Rechnung. Den Betrag und den Zeitraum.
    """
    def __init__(self,betrag:float,zeitraum:str, titel='Rechnung'):
        self.betrag = betrag
        self.zeitraum = zeitraum
        self.titel = titel


class Mitbewohner():
    def __init__(self, name:str, anwesenheit_tage:int):
        self.name = name
        self.anwesenheit_tage = anwesenheit_tage

    def zahlt(self,Rechnung:Rechnung, mitbewohner2): # hier nur der Variablen Name -> darin steckt dann eine Mitbewohner() Instanz
        gewicht = self.anwesenheit_tage / (self.anwesenheit_tage + mitbewohner2.anwesenheit_tage) # hier dann Zugriff auf ein Attribut der Instanz
        due = Rechnung.betrag * gewicht
        return due


