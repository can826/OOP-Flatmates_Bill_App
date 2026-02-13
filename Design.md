# Titel
Flatmate´s Bill App

# Beschreibung
Die App nimmt den Betrag einer Rechnung für einen bestimmten Zeitraum entgegen. Außerdem nimmt sie die Anzahl an Tagen die ein Mitbewohner während dem Zeitraum anwesend war.
Dann berechnet sie den Anteil jedes Mitbewohners an der Rechnung und gibt eine PDF aus.

## Input
Rechnunsbetrag
Zeitraum
Name Mitbewohner X 
Tage Mitbewohner X

## Output
Der Betrag pro Mitbewohner
Eine PDF wird in einem Directory gespeichert
Ein Link zu der PDF in der Web Ansicht (Cloud Link)
# Klassen
Rechnung:
    * Betrag
    * Zeitraum

Mitbewohner:
    * Name
    * Anwesnehit in Tagen
    * zahlt(Rechnung, Anwesenheit) -> die Methode bekommt eine Instanz von rechnung als Paramter
MERKE: Die Methode einer Klasse kann als Paramter auch eine gesamte andere Klasse bekommen. So kann sie auf deren Attribute zugreifen
  
PDF_File:
    * Filename
    * generate(Rechnung, Mitbewohner1, Mitbewohner2)
  
    

## Fragen
- Wie gebe ich der Klasse MA den Betrag aus der Klasse Rechnun? Das MA von RE erbt ist doch nicht sinnvoll oder ?