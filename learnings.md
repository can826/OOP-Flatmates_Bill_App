
Wenn ich ein Parameter in einer Methode verwenden möchte der bereits in der Klasse initialisert wurde,
dann muss ich den Paramter nicht an die Methode übergeben sondern kann ihn einfach innerhalb der Methode verwenden! 
* Jede Klasse soll nur **eine Verantwortlichkeit** haben

# Klasse erstellen - Paramter im Konstruktor verwenden
1. Als Parameter hinzufügen (Dynamisch)
Das ist der häufigste Weg. Du möchtest, dass jeder User beim Erstellen der Rechnung einen eigenen Titel festlegen kann.

```
class Rechnung():
    def __init__(self, betrag: float, zeitraum: str, titel: str): # Hier hinzugefügt
        self.betrag = betrag
        self.zeitraum = zeitraum
        self.titel = titel
```

2. Einen Standardwert festlegen (Statisch)
Wenn jede Rechnung erst einmal denselben Titel haben soll (z. B. "Unbenannt"), kannst du einen festen Wert (String) zuweisen. 
-> Option 2 (Fester Wert): Teils korrekt. Der User kann den Titel beim Erstellen (also in den Klammern Rechnung(...)) nicht festlegen. Aber: In Python sind Attribute standardmäßig "öffentlich". Das heißt, der User könnte ihn nach der Erstellung theoretisch trotzdem ändern:
meine_rechnung.titel = "Neuer Name". Er ist also nicht "schreibgeschützt", nur eben nicht über den Konstruktor konfigurierbar.
```
class Rechnung():
    def __init__(self, betrag: float, zeitraum: str):
        self.betrag = betrag
        self.zeitraum = zeitraum
        self.titel = "Standard-Rechnung" # Fester Wert statt Variable
```
3. Einen Standardwert im Parameter setzen
So ist der Titel optional. Wenn du ihn beim Erstellen nicht angibst, wird der Standard genutzt.

```
class Rechnung():
    def __init__(self, betrag: float, zeitraum: str, titel: str = "Rechnung"):
        self.betrag = betrag
        self.zeitraum = zeitraum
        self.titel = titel
```

# Fragen
- Wie übergebe ich Parameter an eine Methode, wenn der Parameter aus einer anderen Klasse kommt ? -> zahlt() in main.py Line14
- Wie gebe ich der Klasse MA den Betrag aus der Klasse Rechnung? Das MA von RE erbt ist doch nicht sinnvoll oder ?
  - In der Klasse MA bekommt die Methode zahlt() als Paramter ein Objekt der Klasse Rechnung. Dann kann innerhalb der Methode auf die Attribute der Klasse Rechnung zugegriffen werden. 
- Wenn ich einer Klasse einen Standardwert für ein Attribut geben möchte, schreibe ich es nicht in die init() sondern, 
liste es darunter asl Attribut auf ?
  - In die init() kommt der Parameter mit einem Standardwert. Wird eine Instanz erstellt, erhält sie als Wert für das Attribut den Standardwert. Wird bei der Erstellung der Instanz ein Wert übergeben, wird der Stadnardwert überschirieben.
    
- Was ist der Unterschied zwischen einem absoluten und einem relativen Pfad?
  - Absoluter Pfad:
       * Startet ganz oben bei der Wurzel (Root) des
         Betriebssystems.
       * Beinhaltet die komplette Kette:
         /Users/cc/Code_Übung/project/files/bill.pdf.
       * Funktioniert immer, egal von wo aus du das Programm
         startest.
    -  Relativer Pfad:
       * Startet in deinem aktuellen Arbeitsverzeichnis (da, wo du
         gerade "bist").
       * Beschreibt den Weg von "hier" aus: files/bill.pdf.
       * Ist kürzer, aber "bricht", wenn du das Skript aus einem
         anderen Ordner heraus aufrufst.

- An welcher Stelle runde ich den due ab ? Bereits in der Methode, sodass ich im return schon die gerundete Float habe ?
  oder erst bei der Ausgabe bzw. dem Schreiben in die PDF?
  - Option 1: Formatierung der Anzeige mit f String -> .2f (2 Float Nachkommastellen). Durch runden in der Ausgabe bleibt die mathematische 
  Formel unberührt, für interne Berehcnungen ist das besser! 
  - Option 2: mathematisches runden in der Methode mit round(zahl, 2), kurz vor dem return
  -> Merke: Trenne Logik und Präsentation. Logik sauber halten für weitere Berechnungen

# Code Organisieren - Was kommt in die main.py ?
## Seperation of Concerns 

**Best Practice Architektur: Separation of Concerns (Trennung der Zuständigkeiten)**
  In der Softwareentwicklung trennt man strikt zwischen der Logik/Daten (deinen
  Klassen) und dem Interface/Präsentation (deiner CLI).

  Der optimale Aufbau für dein Projekt:
   1. `models.py` (oder `flatmates_bill.py` / `classes.py`): Hier liegen nur deine
      Klassen (Rechnung, Mitbewohner, PDF_File). Keine print()-Befehle (außer zum
      Debuggen) und keine input()-Abfragen.
   2. `main.py`: Das ist der Einstiegspunkt (Entry Point) deines Programms. Jeder
      Programmierer erwartet, dass ein Programm startet, wenn er python main.py
      eintippt. Hier kommt dein CLI-Code hinein.

Aktuell hast du es genau umgekehrt: Deine main.py enthält die Klassen und deine
  interface.py enthält die CLI. 

  Lass uns im Detail anschauen, warum man das ändern sollte und was die Vor- und
  Nachteile sind.

  Was passiert bei deinem aktuellen Aufbau? (Ein versteckter Fehler)
  Wenn du dir deine aktuelle main.py ansiehst, hast du ganz unten Code stehen, der
  direkt ausgeführt wird:

   1 strom = Rechnung(70, 'März')
   2 Tom = Mitbewohner('Tom', 31)
   3 # ...
   4 ausgabe = pdf.create_PDF(...)
  Weil dieser Code nicht durch ein if __name__ == '__main__': geschützt ist,
  passiert Folgendes: Sobald du in deiner interface.py den Befehl from main import
  Rechnung... aufrufst, führt Python die gesamte main.py von oben nach unten aus.
  Das heißt, im Hintergrund wird bereits eine PDF für Tom und Anna generiert, bevor
  der User in der CLI überhaupt nach Daten gefragt wird!



# FPDF Package
## Vorgehen
* PDF erstellen mit: FPDF(orientation='P', unit='pt',format='A4')
* Erstelle eine Seite mit instanz.add_page()
* Font einstellen vor Texterstellung mit set_font(family='Arial' ,size=22, style='B')
* Zelle erstellen. Eine Zelle ist wie ein Rechteck auf der Seite. Darin erstellen wir den Text!
  * pdf.cell(w=100, h=80, txt='Flatmate Bill', border=0, align='C', ln=1) # Bekommt die größe der Zelle: w und h sind entsprechen der unit die wir in der Klasse definiert haben siehe oben unit='pt'
  * pdf.cell(w=50, h=30, txt='Rechnung', border=0)

### Wichitige Methoden und Parameter
* explain where to put the next cell -> ln=1
* align: Lage innerhalb der Zelle
* w=0 -> Zelle nimmt die gesamte Länge
* border=0 ohne rectangle ausdrucken