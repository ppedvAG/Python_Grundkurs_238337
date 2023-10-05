# List Comprehension
# Gibt die Möglichkeit, schnell aus einer Expression heraus eine Liste zu erzeugen
# Das Muster enthält eine Schleife und erzeugt daraus eine Liste

# Mit Schleife
zahlen = []
for i in range(10):
	zahlen.append(i)
print(zahlen)

# Mit List Comprehension
zahlenLC = [i for i in range(10)]  # Hier in der Klammer eine Schleife schreiben, danach den Cursor an den Anfang setzen und die Schleifenvariable ausschreiben
print(zahlenLC)

# Alle geraden Zahlen von 0 bis 100
zahlenGerade = []
for i in range(100):
	if i % 2 == 0:
		zahlenGerade.append(i)
print(zahlenGerade)

# Mit LC
zahlenGeradeLC = [i for i in range(100) if i % 2 == 0]
print(zahlenGeradeLC)

# Alle Zahlen hoch sich selbst
zahlenPotenziert = []
for i in range(100):
	zahlenPotenziert.append(i ** i)
print(zahlenPotenziert)

# Mit LC
# Links kann der Wert bearbeitet werden (in append)
zahlenPotenziertLC = [i ** i for i in range(100)]

# Ergebnis zu einem String konvertieren
print([f"{i}^2={i ** 2}" for i in range(100)])

# Ergebnis zu einer Liste von Listen konvertieren
# tabelle = [[i, i**2, i**i] for i in range(100)]
# for row in tabelle:
# 	print(row)

# Kleines 1x1 mit LC
print([f"{i} * {j} = {i * j}" for i in range(1, 11) for j in range(1, 11)])

# Ternary Operator
print(["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1, 100)])

# Alle Wörter in einem Text finden die ein E oder e enthalten
text = "Alle Wörter in einem Text finden die ein E oder e enthalten"
splitList = text.split(" ")
print([wort.upper() for wort in splitList if "t" in wort or "T" in wort])


# Übung 1
# Schreibe eine List-Comprehension die nur Zahlen aus einer Range von 1 bis inklusive 30 in die neue Liste packt, falls die Zahl durch 6 teilbar ist
# Bevor die Zahl in die neue Liste gepackt wird, soll sie um 12 erhöht werden

# Übung 2
# Schreibe eine List-Comprehension die aus einem Text alle Kleinbuchstaben nimmt und Groß in die Liste schreibt

# Übung 3
# Schreibe eine List-Comprehension die aus einem Text alle Anfangsbuchstaben nimmt

# Übung 4
# Schreibe eine List-Comprehension die aus einem Text alle Wörter nimmt die 3 oder weniger Zeichen haben
