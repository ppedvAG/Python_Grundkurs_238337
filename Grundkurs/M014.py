# Decorator
# Sind Funktionen die andere Funktionen bearbeiten können
# Werden mit @Name hinzugefügt


# Funktionen sind Objekte
def test():
	pass

print(type(test))  # <class 'function'>

def testDecorator(func):  # func: Die zu dekorierende Funktion
	def wrapper():  # Den Code der vom Decorator ausgeführt werden soll
		print("Vor der Funktion")
		func()  # Der eigentliche Funktionscode
		print("Nach der Funktion")
	return wrapper  # Hier wird das Wrapper Objekt zurück gegeben


@testDecorator  # Über @Name den Decorator anhängen
def hallo():
	print("Hello World")

hallo()

h = testDecorator(hallo)  # Ohne @ Syntax
h()

# Decorator mit Parameter
def testDecoratorParam(func):
	def wrapper(*args, **kwargs):  # Der Wrapper gibt die Form der Funktion vor. Über *args und **kwargs können alle Parameter abgedeckt werden
		print("Vor der Funktion")
		func(*args, **kwargs)  # Hier die Parameter weitergeben
		print("Nach der Funktion")
	return wrapper

@testDecoratorParam
def hallo(name: str):
	print(f"Hallo {name}")

hallo("Lukas")

# Decorator mit Parameter und Return
def testDecoratorReturn(func):
	def wrapper(*args, **kwargs):
		print("Vor der Funktion")
		return func(*args, **kwargs)  # Hier einfach return davor schreiben
		# print("Nach der Funktion")
	return wrapper

@testDecoratorReturn
def addiere(x, y):
	return x + y

print(addiere(3, 4))

# Sinnvoller Decorator
def measureTime(func):
	def wrapper(*args, **kwargs):
		import time

		start = time.time()
		func(*args, **kwargs)

		print(f"Dauer: {float(int((time.time() - start) * 100)/100)}s")
	return wrapper


@measureTime
def list100mio():
	print(list(range(10_000_000)))

# list100mio()


# Vordefinierte Decorator
# property
class Quadrat:
	def __init__(self, seite: float):
		self._seite = seite

	@property  # Getter
	def seite(self):
		return self._seite

	@seite.setter  # Setter
	def seite(self, neueLaenge):
		if neueLaenge > 0:
			self._seite = neueLaenge
		else:
			print("Neue Länge ungültig")

q = Quadrat(10)
print(q._seite)  # Kann trotzdem angegriffen werden, auch wenn es bei den Vorschlägen nicht sichtbar ist
print(q.seite)
q.seite = 20

print(q.seite)