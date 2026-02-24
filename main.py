from flat import Rechnung, Mitbewohner
from pdf_generation import PDF_File

## Hole Infos für die Rechnung
rechnung_betrag = float(input('Geben Sie den Betrag der Rechnung ein '))
rechnung_zeitraum = input('Geben Sie den Zeitraum an. z.B. Mai 2026')
rechnung_titel = input('Geben Sie einen Titel für die Rechnung ein ')
# Erstelle Rechnungs Instanz
rechnung= Rechnung(rechnung_betrag,rechnung_zeitraum, rechnung_titel)
while True:
    # MA1
    name_ma1 = input('Geben Sie ihren Namen ein ')
    ma1_anwesenheit_tage = int(input(f'Wie viele Tage war {name_ma1} im {rechnung_zeitraum} anwesend (Ganzahl)'))
    # MA2
    name_ma2 = input('Geben Sie den Namen des Mitbewohners an ')
    ma2_anwesenheit_tage = int(input(f'Wie viele Tage war {name_ma2} im {rechnung_zeitraum} anwesend (Ganzahl)'))
    if ma1_anwesenheit_tage <= 31 and ma2_anwesenheit_tage <= 31:
        ma1 = Mitbewohner(name_ma1, ma1_anwesenheit_tage)
        ma2 = Mitbewohner(name_ma2, ma2_anwesenheit_tage)
        break
    else:
        print('Ein Mitbewohner kann maximnal 31 Tage anwesend sein!')

# Berechne die Beträge der MA
betrag_ma1 = ma1.zahlt(rechnung,ma2)
betrag_ma2 = ma2.zahlt(rechnung,ma1)
# Ausgabe der Ergebnisse
print(f'{ma1.name} zahlt {betrag_ma1} ')
print(f'{ma2.name} zahlt {betrag_ma2} ')

# Erstelle PDF
pdf = PDF_File(rechnung.titel)
pdf.create_PDF(rechnung=rechnung,mitbewohner1=ma1, mitbewohner2=ma2)