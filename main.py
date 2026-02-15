from fpdf import FPDF
import webbrowser
import os


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
        gewicht = self.anwesenheit_tage / (self.anwesenheit_tage + mitbewohner2.anwesenheit_tage) # hier dann Zugriff auf ein Attribut der Instanz
        due = Rechnung.betrag * gewicht
        return due


class PDF_File():
    def __init__(self,filename:str):
        self.filename = filename

    def __str__(self):
        return f"Name des Dokuments: {self.filename}"

    def create_PDF(self, rechnung,mitbewohner1,mitbewohner2):
        # create pdf instanz
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()  # Fügt eine Seite hinzu bzw. erstellt di erste Seite

        # Add Image
        pdf.image(name='files/house.png', w=30,h=30)

        anteil_MA_1= str(round(mitbewohner1.zahlt(Rechnung=rechnung, mitbewohner2=mitbewohner2),2))
        anteil_MA_2= str(round(mitbewohner2.zahlt(Rechnung=rechnung, mitbewohner2=mitbewohner1),2))

        # Add Text
        pdf.set_font(family='Arial', size=22, style='B')
        ## add a cell --> a cell is like a rectangel
        pdf.cell(w=0, h=80, txt='Flatmate Bill', border=0, align='C',ln=1)  # Bekommt die größe der Zelle: w und h sind entsprechen der unit die wir in der Klasse definiert haben siehe oben unit='pt'

        # H2 Rechnung
        pdf.set_font(family='Arial', size=18, style='B')
        pdf.cell(w=200, h=100, txt='Rechnung', border=0)
        # H2 Period
        pdf.set_font(family='Arial', size=18, style='B')
        pdf.cell(w=120, h=100, txt=rechnung.zeitraum, border=0, ln=1)
        pdf.cell(w=0, h=50, ln=1)

        # Namen der MA
        pdf.set_font(family='Arial', size=22, style='B')
        pdf.cell(w=300, h=50, txt='Anwesende Mitbewohner', border=0, ln=1)
        ## MA1
        pdf.set_font(family='Arial', size=16)
        pdf.cell(w=150, h=30, txt=mitbewohner1.name, border=0)
        pdf.cell(w=190, h=30, txt=f'{anteil_MA_1} EUR', border=0, ln=1)
        ## MA2
        pdf.cell(w=150, h=30, txt=mitbewohner2.name, border=0)
        pdf.cell(w=190, h=30, txt=f'{anteil_MA_2} EUR', border=0, ln=1)

        # Ausgabe der PDF in ein Direc
        pdf.output(name=f'files/{self.filename}.pdf')
        # Automatisches öffnen des File im Browser (URI Schema wird erstellt)
        # For a URI you need the absolute apth
        absolute_path=os.path.abspath(f'files/{self.filename}.pdf')
        webbrowser.open(absolute_path)




strom = Rechnung(40, 'März')
Tom = Mitbewohner('Tom', 31)
Anna = Mitbewohner('Anna', 21)

print(Anna.zahlt(Rechnung=strom, mitbewohner2=Tom))
print(Tom.zahlt(Rechnung=strom, mitbewohner2=Anna))

pdf = PDF_File(filename='Strom')
ausgabe = pdf.create_PDF(rechnung=strom,mitbewohner1=Tom, mitbewohner2=Anna)