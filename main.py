class Rechnung():
    """
    Klasse enthält die Daten einer Rechnung. Den Betrag und den Zeitraum.
    """
    def __init__(self,betrag:float,zeitraum:str):
        self.betrag = betrag
        self.zeitraum = zeitraum

class Mitbewohner():
    def __init__(self, name:str, anwesenheit_tage:int):
        self.name = name
        self.anwesenheit_tage = anwesenheit_tage

    def zahlt(self,Rechnung:Rechnung, mitbewohner2): # hier nur der Variablen Name -> darin steckt dann eine Mitbewohner() Instanz
        #cost_per_day = Rechnung.betrag / 31
        #amount_for_MA = cost_per_day * self.anwesenheit_tage
        koeffizient = self.anwesenheit_tage / self.anwesenheit_tage + mitbewohner2.anwesenheit_tage # hier dann Zugriff auf ein Attribut der Instanz
        due = Rechnung.betrag * koeffizient
        return due


class PDF_File():
    def __init__(self,filename:str):
        self.filename = filename

    #def generate(self,Rechnung:Rechnung, Mitbewohner:Mitbewohner, Mitbewohner:Mitbewohner):
        #pass




strom = Rechnung(40, 'Januar')
Tom = Mitbewohner('Tom', 31)
Anna = Mitbewohner('Anna', 21)

print(Anna.zahlt(Rechnung=strom, mitbewohner2=Tom))