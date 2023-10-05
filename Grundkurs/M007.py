# Module
# Sind Libraries (Code Sammlungen) die aus Python Skripten bestehen
# Sie können importiert werden um die Funktionalität unseres Programmes zu erweitern
# Module sollten generell einen bestimmten Zweck erfüllen und nicht mehr

# Wie importiere ich Module?
# 2 Möglichkeiten
# Das import Keyword
# Syntax:
#   import <Modulname>
# Es bindet alle Funktion/Klassen des Moduls in dieses Skript ein

import M006  # Import jetzt alle Funktionen aus diesem Modul

M006.countCase("Ein weiterer Text")  # Wenn ein Skript importiert wird, wird das gesamte Skript ausgeführt

# Das from Keyword
# Syntax:
#   from <Modulname> import <F1>, <F2>, <F3>, ...
# Einzelne Member importieren anstatt alles

from M007b import test  # Hier wird auch das gesamte Skript ausgeführt, weil das Funktionsobjekt angelegt werden muss

test()  # Hier muss der Modulname nicht angegeben werden

from M006 import *  # import *: Importiere alles aus dem Skript und binde es in meinem Skript ein
countCase("Zwei Text")  # Modulname wird nicht mehr als Prefix benötigt

# Aliases
# Modulnamen können einen Alias bekommen um den tatsächlichen Namen zu kürzen
import M005 as M5

print(M5.text)

# Die Main Methode
# Wird ausgeführt wenn das Skript das gestartet wird
# Generell werden Skripte entweder direkt gestartet oder importiert
# Steht immer am Ende eines Skripts

# __name__
# Gibt den Namen des Skripts aus
# Gibt __main__ aus wenn das Skript direkt gestartet wird, gibt den Skriptnamen selbst aus wenn das Skript importiert wurde
print(__name__)

# Suchpfade
# Die Pfade in denen nach Modules gesucht wird bei import
# 3 Kategorien:
# Der Ordner mit dem Skript selbst
# Den Ordner der Python Runtime
# Der Ordner innerhalb der venv mit den externen Modulen (site-packages)
# Wenn ein Modul nicht gefunden wird, wird der ModuleNotFoundError geworfen
import sys
for path in sys.path:
	print(path)

# Module installieren
# 2 Möglichkeiten
# - Python Packages
# - Über pip
# -- pip install <Name>
# -- pip uninstall <Name>

import numpy as np
np.round(5.5)

# __init__.py
# Wird ausgeführt, wenn das Paket importiert wird


def main():
	print("Wird direkt ausgeführt")

if __name__ == "__main__":  # "Main Methode"
	main()  # main Methode auslagern
else:
	print("Wurde importiert")