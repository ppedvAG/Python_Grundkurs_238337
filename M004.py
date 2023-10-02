# Schleifen

# Führt Code mehrmals aus
# Wenn am Ende der Schleife die Bedingung noch wahr ist, wird die Schleife wiederholt

# while-Schleife
# Hat eine Bedingung und wird solange ausführt, wie die Bedingung True ist

a = 0
b = 10

while a < b:
	print(a)
	a += 1  # In Python gibt es kein ++/--
print("Nach der Schleife")

# break und continue
# Ermöglichen das Steuern der Schleife
# break: Beendet die Schleife
# continue: Springt zum Schleifenkopf zurück (führt den Code danach nicht aus)

a = 0
while a < b:
	print(a)
	print("a kleiner b")
	a += 1
	if a == 5:
		break  # Springt aus der Schleife heraus

print("Nach der Schleife")

a = 0
while a < b:
	a += 1
	if a == 5:
		continue  # Springt in den Schleifenkopf zurück
	print(a)
	print("a kleiner b")

# Endlosschleife
while True:
	a += 1
	if a == 500:
		break  # Mache etwas bis zu einem bestimmten Punkt


# for-Schleife
# Benötigt immer eine Collection
# Wird in anderen Sprachen als foreach bezeichnet

liste = [1, 2, 3, 4, 5]
for element in liste:
	print(element)

for i in range(10):  # int i = 0; i < 10; i++
	print(i)

for i in range(10, -1, -1):  # int i = 10; i >= 0; i--
	print(i)

for zeichen in "Das ist ein Text":
	print(zeichen)

# else bei einer Schleife
# Ermöglicht, nach erfolgreichem Ausführen der Schleife ein Stück Code auszuführen
c = 0
d = 10
while c < d:
	c += 1
	if c == 5:
		break  # else wird verhindert
else:
	print("Schleife erfolgreich beendet")


# fstring
# Formatted String
# Code in einen String einbinden

a = 5
output = "Die Zahl ist " + str(a)  # ohne fstring
output2 = f"Die Zahl ist {a}"  # mit fstring

for i in range(10):
	# 3 Ausgaben: Die Zahl selbst, die Zahl hoch 2, die Gleichung von zahl^2
	print("Die Zahl ist " + str(i))
	print("Die Zahl hoch 2 ist " + str(i ** 2))
	print(str(i) + "^2=" + str(i ** 2))

	print(f"Die Zahl ist {i}")
	print(f"Die Zahl hoch 2 ist {i ** 2}")
	print(f"{i}^2={i ** 2}")

# Übung 1:
# FizzBuzz
# 1. Schleife schreiben, die von 1 bis inklusive 100 hochzählt
# 2. Wir müssen in der Schleife jede Zahl auf ihre Teilbarkeit prüfen:
# Falls sie durch 3 teilbar ist, soll in der Konsole "Fizz" ausgegeben werden
# Falls sie durch 5 teilbar ist, soll in der Konsole "Buzz" ausgegeben werden
# Falls sie sowohl durch 3 als auch 5 teilbar ist, soll in der Konsole "FizzBuzz" ausgegeben werden
# Falls sie weder durch 3 noch 5 teilbar ist, soll die Zahl selbst in der Konsole ausgegeben werden
# 1, 2, Fizz, 4, Buzz, ..., 14, FizzBuzz

# Übung 2:
# Schreibe eine Schleife die dir alle Zahlen von 1 bis 200 zur Verfügung stellt
# Lass dir jede Zahl erst in der kardinalen und dann daneben in der ordinalen Schreibweise darstellen
# Zahl + Endung 'st', 'nd', 'rd' oder 'th'
# 1st, 2nd, 3rd, 4th, ..., 21st, 22nd, 23rd, 24th
# Bonus: Berücksichtige alle Zahlen die mit 11, 12 oder 13 enden

# Übung 3:
# Stoppuhr
# Bevor die Minute hochtickt, müssen die Sekunden einmal eine vollkommene Umdrehung hinter sich gebracht haben
# time.sleep(Float) Funktion hier nützlich

# Übung 4:
# Erstelle eine Schleife die das kleine Einmaleins von 1 bis 10 berechnet, und jeden einzelnen
# Schritt in der Konsole ausgibt
# "1 x 1 = 1"
# "1 x 2 = 2"
# ...
# "5 x 5 = 25"
# ...
# "7 x 4 = 28"
# ...
# "10 x 10 = 100"