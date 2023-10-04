# Funktionen
# Code wiederverwenden
# Funktionen sind Objekte, sie sind erst verfügbar, wenn das Skript an der Stelle ausgeführt wird

# hallo()  # Funktion ist erst ab Zeile 7 sichtbar

def hallo():
	print("Hallo Welt")

hallo()

print(hallo)  # Funktionszeiger

# Funktion mit Parameter

def hallo(name):
	print(f"Hallo {name}")

hallo("Josef")
hallo("Markus")
hallo("Lukas")
hallo(123)
hallo([1, 2, 3])
hallo(True)  # Hier kann ein beliebiger Wert hereinkommen

# 2 Möglichkeiten

# 1. Typvergleich
def halloTypvergleich(name):
	if type(name) == str:
		print(f"Hallo {name}")
	else:
		print("Name ist kein String")

halloTypvergleich("Josef")
halloTypvergleich("Markus")
halloTypvergleich("Lukas")
halloTypvergleich(123)
halloTypvergleich([1, 2, 3])
halloTypvergleich(True)

# 2. Typ "empfehlen"
def halloEmpfehlung(name: str):
	print(f"Hallo {name}")

halloEmpfehlung("Josef")
halloEmpfehlung("Markus")
halloEmpfehlung("Lukas")
halloEmpfehlung(123)
halloEmpfehlung([1, 2, 3])
halloEmpfehlung(True)

# return Werte
# Funktionen können auch Ergebnisse haben
def addiere(x: int, y: int):
	return x + y

summe = addiere(3, 4)

def dividiere(x: int, y: int) -> int:  # Rückgabetyp vorgeben
	return x / y


# Keyword Arguments
# Parameter können in einer beliebigen Reihenfolge angegeben werden
def printPerson(vorname, nachname, alter, adresse):
	print()

printPerson(alter=30, adresse="Zuhause", nachname="Mustermann", vorname="Max")

# Default Parameter
# Ermöglicht, einen Standardwert für Parameter zu setzen
def printPerson(vorname = "", nachname = "", alter = 0, adresse = ""):
	print()

printPerson(nachname="Test", adresse="Teststraße")  # vorname und alter werden mit den Standardwerten befüllt
printPerson(vorname="Max", alter=30)  # Funktion konfigurieren (nur die Parameter vorgeben die auch wirklich benötigt werden)

# Arbitrary Arguments
# Gibt die Möglichkeit, beliebig viele Parameter zu übergeben
# Werden in Python Internen Funktionen als *args bezeichnet
def summieren(*zahlen: int):
	x = 0
	for zahl in zahlen:
		x += zahl
	return x

summieren(1, 2, 3)
summieren(1, 2, 3, 4, 5, 6)
summieren(1)
summieren()  # Keine Parameter sind auch beliebig viele Parameter


# Unpacking
# Liste in ihre Einzelteile zerlegen
# summieren([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(summieren(*[1, 2, 3, 4, 5, 6, 7, 8, 9]))
a, *b, c = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # a=1, c=9, b=[2, 3, 4, 5, 6, 7, 8]

# Dict mit Schleife iterieren
meinCar = {
	"Marke": "Audi",  # Schlüssel als String definieren
	"Modell": "A3",
	"Baujahr": 2019
}

for k, v in meinCar.items():
	print(f"{k}: {v}")

tabelle = [[i, i**2, i**i] for i in range(10)]
for s1, s2, s3 in tabelle:
	print(f"Die Zahl ist: {s1}, die Zahl hoch 2 ist {s2}, die Zahl hoch sich selbst ist {s3}")

for s1, *s2 in tabelle:
	print(f"Die Zahl ist: {s1}, die Zahl hoch 2 ist {s2}, die Zahl hoch sich selbst ist {s2[1]}")

# Arbitrary Keyword Arguments
# Gibt die Möglichkeit, beliebig viele benannte Argumente zu übergeben
# Werden in Python internen Funktionen als **kwargs bezeichnet
# Innerhalb der Funktion wird dieser Parameter als Dictionary gesehen
def printTeilnehmer(**teilnehmer):
	for k, v in teilnehmer.items():
		print(f"Teilnehmer {k} namens {v} nimmt an dem Kurs teil")

printTeilnehmer(T1="Josef", T2="Markus", Trainer="Lukas")

printTeilnehmer(**meinCar)  # Dictionary entpacken


# Übung 1:
# Wir wollen eine Funktion erstellen, die beliebig viele Zahlen als Parameter erhalten kann
# Und uns die größte dieser Zahlen zurückgibt

# Übung 2:
# Wir wollen eine Funktion erstellen, die einen String als Parameter erhält
# Die Funktion soll dann in der Konsole ausgeben, aus wie vielen Klein- und Großbuchstaben der String besteht
# Die Funktion soll zusätzlich zählen wie viele Sonderzeichen (Nummern inkludiert) enthalten sind und das ebenfalls ausgeben
# Sonderzeichen: 4 | Groß: 3 | Klein: 12

# Übung 3
# Schreibe eine Funktion, die eine Liste von Strings als Parameter empfängt
# Diese Funktion soll die Strings als eine Aufzählung zusammenbauen und am Ende zurück geben
# Beispiele:
# Parameter: []
# Keine Parameter angegeben
# Parameter: ["Teilnehmer"]
# Teilnehmer
# Parameter: ["Teilnehmer1", "Teilnehmer2"]
# Teilnehmer1 und Teilnehmer2
# Parameter: ["Teilnehmer1", "Teilnehmer2", "Teilnehmer3", "Teilnehmer4"]
# Teilnehmer1, Teilnehmer2, Teilnehmer3 und Teilnehmer4
