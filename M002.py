# List
# Typ, der mehrere Werte halten kann
# Hat einen Index
# Ist veränderbar
# Duplikate sind erlaubt
# Verschiedene Datentypen sind möglich (sollte vermieden werden)

meineListeObjekt = list()  # -> new list()
meineListe = [1, 2, 3, True, "Text"]  # Listen Klammern sind eckig
print(meineListe)

# Index
print(meineListe[0])
print(meineListe[0:3])

# Werte verändern
meineListe[3] = 4
print(meineListe)

# Listenfunktionen
# list.append(Element)
# Fügt ein neues ELement hinzu
meineListe.append(5)
print(meineListe)

meineListe.append([1, 2, 3])  # Verschachtelte Liste
print(meineListe)

# 2 Möglichkeiten
# +=
# list.extend(Liste)
meineListe += [1, 2, 3]
print(meineListe)

meineListe.extend([1, 2, 3])
print(meineListe)

# list.pop(Index)
# Element an einem Index entfernen
meineListe.pop(6)
print(meineListe)

# Hier auch len verwenden um die Länge zu holen
print(len(meineListe))



# Tupel
# Verhält sich wie die Liste, ist aber nicht veränderbar
# Hat einen Index, Duplikate erlaubt, hat Funktionen
meinTupel = (1, 2, 3)  # Tupel Klammern sind rund
print(meinTupel)

print(meinTupel[0])
# meinTupel[0] = 10  # Nicht möglich

# Tupel über Umweg ändern
temp = list(meinTupel)
temp[0] = 10
meinTupel = tuple(temp)
print(meinTupel)

# Unpacking
# Zerlegt eine Collection in ihre Einzelteile
# Teile werden in einzelne Variablen geschrieben
a, b, c = meinTupel
print(a)
print(b)
print(c)

# Funktioniert bei jedem iterierbaren Typen
text = "Test"
q, w, e, r = text


# Range
# Ermöglicht, einen Bereich von X bis Y zu Erstellen
# Wird häufig in Schleifen verwendet
# Die Range enthält keine Werte
print(range(1_000_000_000))  # range(0, 1000000000) -> Range Objekt (Anleitung für die Erstellung der Zahlen)
# print(list(range(1_000_000_000)))  # Hier werden die Werte erzeugt

print(list(range(100)))  # Nur Obergrenze (exklusiv)
print(list(range(-50, 50)))  # Untergrenze und Obergrenze (exklusiv)
print(list(range(0, 101, 5)))  # Schrittgröße kann auch angegeben werden


# Set
# Verhält sich wie Liste, aber jedes Element muss eindeutig sein
meinSet = {1, 2, 3}  # Set Klammern sind geschwungen
print(meinSet)

meinSet.add(4)
print(meinSet)

meinSet.add(4)
print(meinSet)  # Nichts passiert

# Duplikate entfernen
duplikate = [1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 6, 7]
duplikate = set(duplikate)
duplikate = list(duplikate)
print(duplikate)


# Dictionary
# Liste von Key-Value Paaren
# Jeder Schlüssel hat einen Wert und muss eindeutig sein
meinCar = {
	"Marke": "Audi",  # Schlüssel als String definieren
	"Modell": "A3",
	"Baujahr": 2019
}

print(meinCar)

print(meinCar["Marke"])  # Hier wird ein Stringbasierter Index benötigt

# Schlüssel anpassen
meinCar["KM"] = 10000  # Wird neu erstellt falls nicht existent
print(meinCar)

meinCar["KM"] = 20000  # Wird neu erstellt falls nicht existent
print(meinCar)

# dict.keys(), dict.values(), dict.items()
print(meinCar.keys())
print(meinCar.values())
print(meinCar.items())


# Konvertierungen
# Typen von einer Variable in einen anderen Typen umwandeln
print(int(4.5))  # Konvertierung zu int
print(int("4"))  # Konvertierung direkt über int Konstruktor
# print(list(3))  # Nicht möglich
print(list([3]))
print(tuple([3]))
print(int(True))
print(int(False))
print(bool(4))  # True
print(bool(-1))  # True
print(bool(0))
print(str([3]))
# print(dict(Test1=0, Test2=1))


# Übung 1
# Wir haben 3 vorgegebene Listen
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7, 8]
# Kombiniere die drei Listen in eine ganze Liste und schließe Duplikate aus

# Übung 2
# Erstelle einen String und wandele ihn in eine Liste um, dabei soll jedes einzelne Zeichen ein Element der Liste werden

# Übung 3
# Lasse eine Liste erstellen die bei 0 beginnt und alle geraden Zahlen bis 20 enthält
# Nicht selbst schreiben, sondern Python machen lassen
