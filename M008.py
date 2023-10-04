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
