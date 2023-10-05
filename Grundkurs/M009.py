# Klassen und Objekte

# Klasse
# Bauplan für Objekte
# Hier werden Funktion und Member definiert die später die Objekte haben werden
# Innerhalb der Klasse gibt es generell keine konkreten Werte (werden später bei Objekterstellung eingegeben)

wort = "Text"  # Objekt von Typ str
print(type(wort))  # <class 'str'>

wort2 = "Text2"  # Ein separates Objekt von Typ str
print(type(wort2))  # <class 'str'>

if type(wort) == str:  # Typvergleich
	print()


# Person Klasse
class Person:
	x = 100  # Diese Variable ist auf der Klasse selbst und nicht auf den Objekten

	# Konstruktor
	# Hier werden die Objektbasierten Variablen angelegt
	# Parameter bestimmen die Werte die der Benutzer übergeben muss
	def __init__(self, vorname: str, nachname: str, alter: int, adresse = ""):
		self.vorname = vorname
		self.nachname = nachname
		self.alter = alter
		self.adresse = adresse
		# pass  # Mach nichts (Leerer Body)

	def sprechen(self, text: str):
		print(f"Die Person {self.vorname} {self.nachname} sagt: {text}")

# -------------------------------------------------------------------------------------

# Nach der Klasse

person = Person("Max", "Mustermann", 33)  # (= new Person())
print(person.vorname)
print(person.nachname)
print(person.alter)

person2 = Person("X", "Y", 20, "Zuhause")  # Zweites separates Objekt

person.sprechen("Hallo")
person2.sprechen("Servus")

# Neue Felder hinzufügen
person.geschlecht = "M"  # Sollte nicht gemacht werden
del person.geschlecht

# Objekte in Action

class Kurs:
	def __init__(self, titel: str, tage:int, *teilnehmer: Person):
		self.titel = titel
		self.tage = tage
		self.teilnehmer = list(teilnehmer)

	def neuerTeilnehmer(self, neu: Person):
		self.teilnehmer.append(neu)

	def listTeilnehmer(self):
		for tn in self.teilnehmer:
			print(f"Der Teilnehmer {tn.vorname} {tn.nachname} nimmt am Kurs {self.titel} für {self.tage} Tage teil.")

p1 = Person("", "", 25)
p2 = Person("", "", 48)
p3 = Person("", "", 26)
kurs = Kurs("Python Grundkurs", 3, p2, p3)
kurs.neuerTeilnehmer(p1)
p2 = None  # (= null)

kurs.listTeilnehmer()


# Übung 1:
# 1. Erstelle eine Fahrzeug-Klasse
# 2. Diese Klasse soll typische Eigenschaften eines Fahrzeuges enthalten: (in __init__)
#     - Fahrzeug-Name
#     - Preis
#     - Maximale Geschwindigkeit
#     - Derzeitige Geschwindigkeit
#     - Motorzustand (An/Aus)
# 3. Die Klasse soll auch folgende Methoden enthalten:
#     - Beschleunigen (Erhöhe bzw Verringere die Derzeitige Geschwindigkeit aber übersteige nicht das Maximum) -> Parameter int (Wieviel soll beschleunigt werden)
#     - StarteMotor (Setze Motorzustand auf True, funktioniert nur wenn das Auto noch nicht gestartet ist)
#     - StoppeMotor (Motor kann nur gestoppt werden, wenn das Auto nicht fährt)
#     - Beschreibung (Gibt alle Informationen über die Klasse wieder)
# 4. Erstelle eine Instanz der Klasse und nutze die Beschreibungs Funktion (Konkrete Werte)
