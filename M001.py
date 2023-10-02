# Ich bin ein Kommentar
# Mehrzeilige Kommentare gibt es hier nicht

# Variablen
# name = Wert
# Der Typ einer Variable wird durch den Inhalt vorgegeben

# 4 Datentypen: int (Ganze Zahlen), float (Kommazahlen), str (String, Text), bool (Wahr-/Falschwert)

# int: Ganze Zahl
# Kann beliebig groß sein
ganzeZahl = 583759281935746239054675490235265714783264537941735462

# Float: Kommazahl
# Kann beliebig groß sein
kommaZahl = 53287580912356715329649.1357289012537647353529746325340354769524

# String: Text
# Strings müssen geöffnet und geschlossen werden mit "" oder ''
text = "Ein Text"
text2 = 'Ein Text'

# Boolean: Wahr-/Falschwert
wahr = True
falsch = False

# complex: Komplexe Zahlen
# Mathematisch undefinierte Zahlen
complex = 12 + 5j

# Funktionen
# Code, der bereits existiert, den wir verwenden können
print(ganzeZahl)
print("Zwei Text")

# String Funktionen

# str.lower() und str.upper()
# Schreiben den String lowercase oder UPPERCASE
print(text.upper())  # Erzeugt einen neuen String
print(text)

# str.count(Zeichen)
# Gibt die Anzahl des gegebenen Zeichens aus
print(text.count("E"))

# str.rstrip(Zeichen), str.lstrip(Zeichen), str.strip(Zeichen)
# Schneiden Zeichen links und/oder rechts weg
print(text.rstrip("t"))

# Strings verbinden
print(text + text2)  # Hier wird wieder ein neuer Text erstellt
print(text)

text = text + text2  # Mithilfe von =, + oder += werden die Werte tatsächlich verändert
text += text2
print(text)

# Index
# Eine Collection an einer/mehreren Stelle(n) angreifen
# Kann auch einen Bereich nehmen
# Kann auch von rechts angreifen
print(text[0])  # Zeichen an der nullten Stelle
print(text[0:3])  # Nimm alle Zeichen von 0 bis exklusive 3
print(text[-1])  # Mit - kann von rechts die Liste angegriffen werden
print(text[-4:-1])
print(text[-4:0])  # Funktioniert nicht
print(text[-4:])  # Nimm alles von -4 bis zum Ende
print(text[:3])
print(text[3:])

# len(Collection)
# Gibt die Länge eines iterierbaren Objekts zurück
# Collection haben selbst keine Length Funktion
print(len(text))

liste = [1, 2, 3]
print(len(liste))

# Arithmetische Operatoren
# +, -, *, /
# %: Modulo
# **: Potenzierungsoperator
# //: Ganzzahldivision
zahl1 = 5
zahl2 = 8

zahl1 + zahl2  # Berechne die Summe und wirf das Ergebnis weg
zahl1 += zahl2

zahl1 **= zahl2  # Schreibe das Ergebnis von zahl1^zahl2 in zahl1 hinein
print(zahl1)

print(zahl1 % 5)  # Rest einer Division (hier 1)

# Arithmetik mit Strings
text += text2

print(text * 10)  # Ein TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin TextEin Text
text *= 10



# Übung 1
# Lege drei numerische Variablen an, addiere sie zusammen und schreibe das Ergebnis in eine neue Variable
# Potenziere danach die Variable mit sich selbst und schreibe das Ergebnis erneut in eine Variable
z1 = 3
z2 = 8
z3 = 4
summe = z1 + z2 + z3
summe2 = summe ** summe

# Übung 2
# Nimm die potenzierte Zahl aus Übung 1 und stelle fest ob diese Restlos durch 2 teilbar (gerade) ist
print(summe2 % 2)

# Übung 3
# Lege zwei Variablen an: Vorname befüllt mit Max und Nachname befüllt mit Mustermann
# Verbinde diese zwei Variablen und zähle danach die Buchstaben 'M' und 'm'
# Das Ergebnis soll 3 sein
vorname = "Max"
nachname = "Mustermann"
vollerName = vorname + nachname
print(vollerName.count("M") + vollerName.count("m"))
print(vollerName.lower().count("m"))

# Übung 4
# Schreibe deinen Vornamen ohne Großbuchstaben in eine Variable
# Verwende danach diese Variable, und gib diese mit dem ersten Buchstaben groß geschrieben aus
name = "lukas"
print(name[0].upper() + name[1:].lower())
print(name.capitalize())
print(name.title())