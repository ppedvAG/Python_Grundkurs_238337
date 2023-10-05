# Kontrollstrukturen

# if-Anweisungen
# Enthalten eine/mehrere Bedingungen und prüft ob diese True sind
# Benötigt Vergleichsoperatoren und/oder Logische Operatoren

# Vergleichsoperatoren
# ==, !=/<>, <, >, <=, >=

a = 4
b = 7
if a < b:  # Am Ende von Strukturen wird ein Doppelpunkt benötigt
	print("a ist kleiner als b")  # Einrückungen beachten
elif a > b:
	print("a ist größer als b")
else:
	print("a ist gleich b")


if a < b:
	print("a kleiner b")
	if a < 5:
		print("a kleiner 5")
		print("Innerhalb der inneren if")

# Logische Operatoren
# &/and, |/or, ~/not
# in: Prüft, ob ein Wert innerhalb einer Liste ist
# is: Prüft, ob zwei Objekte identisch sind

if a < b and a < 5:
	print("a kleiner b und kleiner 5")

if 3 not in [1, 2, 3]:
	print("3 ist nicht enthalten")

if "e" in "Text":
	print("e ist in Text enthalten")

text = "Text"
if ~text.isupper():
	print("Nicht alle Zeichen sind uppercase")

if "Text":  # Truthyness: Prüft ob ein Objekt nicht None (= null) ist
	print("XYZ")

if "Text" is not None:  # Selbiges wie oben
	print()

if 0:  # 0 ist kein Truthy Wert
	print()

print(4 | 1)  # Binäre Verknüpfung

# Ternary Operator
# Ermöglicht die Vereinfachung von ifs in eine Zeile
if a < b:
	print("a ist kleiner als b")
elif a > b:
	print("a ist größer als b")
else:
	print("a ist gleich b")

print("a größer b" if a > b else "a kleiner b" if a < b else "a gleich b")

# Übung 1
# Wir haben 3 vorgegebene Listen
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7]
# Finde heraus welche Liste die längste ist (es können auch mehrere Listen die längsten sein)
if len(list1) > len(list2) and len(list1) > len(list3):
	print("list1 ist die längste")
elif len(list2) > len(list3) and len(list2) > len(list1):
	print("list2 ist die längste")
else:
	print("list3 ist die längste")


laengen = [len(list1), len(list2), len(list3)]
laengen.sort()
maxLaenge = laengen[-1]
if len(list1) == maxLaenge:
	print()
if len(list2) == maxLaenge:
	print()
if len(list3) == maxLaenge:
	print()


# Übung 2
# Nimm die oberen drei Listen und überprüfe ob eine der Listen eine der drei Zahlen enthält: 3, 7, 10
gesamt = list1 + list2 + list3
if 3 in gesamt or 7 in gesamt or 10 in gesamt:
	print()