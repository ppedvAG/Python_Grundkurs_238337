# Vererbung

# Klassen können eine oder mehrere Oberklassen haben und dadurch eine Vererbungshierarchie aufbauen
# Die Oberklasse gibt ihre Member nach unten weiter (Funktionen, Felder)
# object ist die Oberklasse von allen Klassen in Python

class Lebewesen:
	"""
	Die Lebewesen Klasse.

	Sie implementiert einen Konstruktor mit dem Parameter alter und eine Funktion namens Bewegen mit dem Parameter distanz.
	"""
	def __init__(self, alter: int):
		self.alter = alter

	def bewegen(self, distanz: int):
		"""
		Bewegt das Lebewesen um eine gegebene Distanz.

		:param distanz: Die Distanz in Meter.
		"""
		print(f"{type(self).__name__} hat sich um {distanz}m bewegt")  # Über type(self) diese Funktion Typagnostisch machen

class Mensch(Lebewesen):  # In der Klammer die Oberklasse(n) angeben
	def __init__(self, alter: int, name: str):
		# super(): Greift in die Oberklasse
		# Funktionen aus der Oberklasse ausführen
		# Wird hier verwendet um Konstruktoren zu verketten
		super().__init__(alter)
		self.name = name

	def __str__(self):  # ToString
		return f"Der Mensch heißt {self.name} und ist {self.alter} Jahre alt. Die Daten von Lebewesen sind: {super().__str__()}"

	def sprechen(self, text: str):
		print(f"{self.name} sagt: {text}")

	# def bewegen(self, distanz: int):  # Überschreibung von Lebewesen
	# 	print(f"Der Mensch hat sich um {distanz}m bewegt")

class Katze(Lebewesen):
	pass

# -------------------------------------------------------------

# Nach den Klassen

m = Mensch(30, "Max")
print(m.alter)  # Alter wird von Lebewesen vererbt
m.bewegen(10)  # Bewegen wird von Lebewesen vererbt
m.sprechen("Hallo")

print(m)  # Wenn ein Objekt in print kommt wird die __str__ Methode des Objekts ausgeführt

k = Katze(2)
k.bewegen(5)

# docstring
# Ermöglicht die Dokumentation von Klassen und Funktionen
# Wird mit """ geöffnet und geschlossen (''' auch möglich)
# Bei Mouse-Over von einer Funktion oder Klasse wird der Text angezeigt
# Docstrings müssen unter dem Member geschrieben werden