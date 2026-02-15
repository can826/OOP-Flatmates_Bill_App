
Wenn ich ein Parameter in einer Methode verwenden möchte der bereits in der Klasse initialisert wurde,
dann muss ich den Paramter nicht an die Methode übergeben sondern kann ihn einfach innerhalb der Methode verwenden! 
* Jede Klasse soll nur **eine Verantwortlichkeit** haben



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