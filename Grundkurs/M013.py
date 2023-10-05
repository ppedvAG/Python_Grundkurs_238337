# Lambda Expressions

# Anonyme Funktionen: Funktionen die nur temporär verwendet werden und in eine Variable geschrieben werden können
# In anderen Sprachen wird ein Pfeil verwendet (->, =>)
# In Python gibt es das lambda Keyword

# Eigenschaften
# - Kein Name
# - Beliebig viele Parameter
# - Kein Return Keyword
# - Eine Zeile Code
# - Kein Schleifen, kein break/continue

# Syntax:
# lambda <Parameter>: <Funktion>

addiere = lambda x, y: x + y  # Kein Return Keyword
print(addiere(4, 5))

summieren = lambda *zahlen: sum(zahlen)
print(summieren(2, 3, 4, 5, 6, 7, 8))


# Verwendung
# Parameter bei Funktionen
def lambdaTest(func):
	func()


lambdaTest(lambda: print("Text"))  # Über den Lambda-Parameter kann die Funktionsweise der Funktion angepasst werden
lambdaTest(lambda: print("Anderer Text"))

# Häufig verwendete Funktionen
# filter(), map()

# filter(): Filtert eine Liste anhand eines Kriteriums
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9]

zahlenGerade = filter(lambda zahl: zahl % 2 == 0, zahlen)  # Hier wird eine Lambda-Expression benötigt mit einem Parameter die einen Boolean zurück gibt

def filter2(func, collection):
	temp = []
	for element in collection:
		if func(element) == True:
			temp.append(element)
	return temp

print(zahlenGerade)  # <filter object at 0x00000219C351B1F0>
print(list(zahlenGerade))  # filter Objekt: Anleitung zum Erstellen der fertigen Liste -> list(...) um die Liste zu generieren

zahlenGeradeLC = [i for i in zahlen if i % 2 == 0]
print(zahlenGeradeLC)

# map()
# Liste transformieren
zahlenGeradeText = map(lambda zahl: f"Die Zahl ist {zahl}", zahlen)
print(list(zahlenGeradeText))

zahlenGeradeTextLC = [f"Die Zahl ist {zahl}" for zahl in zahlen]
print(zahlenGeradeTextLC)

zahlenTabelle = map(lambda zahl: [zahl, zahl * 2, zahl ** zahl], zahlen)
for element in zahlenTabelle:
	print(element)