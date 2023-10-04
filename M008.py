# In- und Output

# print(...)

# input(Text)
# Fordert den Benutzer auf, eine Eingabe zu machen
# Stoppt die Konsole solange der Benutzer keine Eingabe getätigt hat
# eingabe = input("Gib deinen Namen ein: ")
# print(f"Dein Name ist {eingabe}")
#
# zahl = input("Gib eine Zahl ein: ")
# zahl = int(zahl)
# print(f"Deine Zahl mal 2 ist: {zahl * 2}")

# open(Pfad)
# Ermöglicht uns mit Dateien zu interagieren
file = open("Test.txt", "w")
file.writelines("Test1\n")
file.writelines("Test2\n")
file.writelines("Test3\n")
file.flush()  # Die geschriebenen Zeilen werden nur in einen Buffer geschrieben, mit Flush in das File schreiben
file.close()  # Files sollten immer geschlossen werden

# Escape-Sequenzen
# Unschreibbare Zeichen in Strings einbauen
# https://docs.microsoft.com/en-us/cpp/c-language/escape-sequences?view=msvc-170
# \n für Zeilenumbruch, \\ für einzelnen Backslash

# with-Statement
# Öffnet den Stream ganz normal, aber schließt ihn am Ende des Blocks automatisch
with open("Test.txt", "w") as file2:
	file2.writelines("Test1\n")
	file2.writelines("Test2\n")
	file2.writelines("Test3\n")

# rstring
# String der keine Escape-Sequenzen interpretiert
# Nützlich bei Pfaden
# pfad = "C:\Users\lk3\source\repos\Python_Grundkurs_2023_10_02\venv\Scripts\python.exe"  # Hier werden Escape-Sequenzen interpretiert
pfad2 = "C:\\Users\\lk3\\source\\repos\\Python_Grundkurs_2023_10_02\\venv\\Scripts\\python.exe"  # Backslashes Escapen
pfadR = r"C:\Users\lk3\source\repos\Python_Grundkurs_2023_10_02\venv\Scripts\python.exe"  # r vor String um Escape-Sequenzen zu ignorieren

# Das os Modul
# Modul zur Interaktion mit dem Betriebssystem
# -> Pfad-/Fileoperationen sind hier auch inkludiert

import os
os.path.join("Test", "Test.txt")  # Betriebssystemunabhängig Pfade verknüpfen
os.path.exists("")  # Existiert ein File/Ordner?
os.mkdir("Test")  # Ordner erstellen

# Übung 1:
# Funktion die dem User die Möglichkeiten (w, r, a) gibt
# User soll eine davon auswählen über input()
# Wenn der User keine valide Möglichkeit eingibt, soll die Eingabe wiederholt werden
# Bei w oder a soll ein File geöffnet werden und eine Erfolgsmeldung in das File geschrieben werden
# Bei r soll das File ausgelesen werden und der Inhalt in die Konsole geschrieben werden
def userEingabe():
	while True:
		eingabe = input("Gib einen w, r oder a ein: ")
		if eingabe in ["w", "r", "a"]:
			with open("Test.txt", eingabe) as file:
				if eingabe == "r":
					print(file.readlines())
				else:
					file.writelines("Erfolg")
				return

# Übung 2:
# Erstelle ein Programm, das zwei Integer oder Floats abfragt
# Gib dem Nutzer die Möglichkeit per Tastendruck zwischen Addition, Subtraktion, Multiplikation und Division zu wählen.
# -> Zahl zwischen 1 und 4 -> Rechenoperation auswählen
# Bei Ungültiger Eingabe soll der Benutzer erneut nach seiner Entscheidung gefragt werden.
# Lasse das Ergebnis inklusive der Rechnung in der Konsole ausgeben
# Frage nach Ende der Operation ob der Benutzer eine neue Rechnung (Wiederholen) durchführen will
def rechner():
	while True:
		zahl1 = int(input("Gib die erste Zahl ein: "))
		zahl2 = int(input("Gib die zweite Zahl ein: "))
		rechenoperation = int(input("Gib die Rechenoperation ein (1: Addition, 2: Subtraktion, 3: Multiplikation, 4: Division): "))

		if rechenoperation == 1:
			print(f"{zahl1} + {zahl2} = {zahl1 + zahl2}")
		elif rechenoperation == 2:
			print(f"{zahl1} - {zahl2} = {zahl1 - zahl2}")
		elif rechenoperation == 3:
			print(f"{zahl1} * {zahl2} = {zahl1 * zahl2}")
		elif rechenoperation == 4:
			print(f"{zahl1} / {zahl2} = {zahl1 / zahl2}")
		else:
			continue

		wiederholen = input("Y drücken für Wiederholung")
		if wiederholen.lower() != "y":
			break