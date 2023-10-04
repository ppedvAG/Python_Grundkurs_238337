# Fehlerbehandlung
import traceback

# Es gibt Fehler die nicht vorhersehbar sind die nicht durch ifs gefangen werden können
# Diese Fehler können mithilfe der try-except Mechanik gefangen werden

# zahl = int(input("Gib eine Zahl ein: "))

# eingabe = input("Gib eine Zahl ein: ")
# if eingabe.isnumeric():
# 	zahl = int(eingabe)

try:
	zahl = int(input("Gib eine Zahl ein: "))
	zahl2 = int(input("Gib eine zweite Zahl ein: "))
	if zahl2 == 0:
		raise ZeroDivisionError  # raise: Fehler selbst verursachen
	print(zahl / zahl2)

except ValueError as e:  # Hier kommen wir nur herein, wenn keine Zahl eingegeben wurde
	print("Keine Zahl eingegeben")
	print(e)  # Python interne Nachricht

	for line in traceback.format_exception(e):  # Stack Trace ausgeben (hier eine Liste)
		print(line)
except KeyboardInterrupt:
	print("Programm per Strg+C beendet")
except EOFError:
	print("Programm per Strg+D beendet")
except:  # BaseException as e:
	print("Anderer Fehler")
	raise  # Lässt das Programm hier trotzdem abstürzen (wirft die Exception weiter)
else:  # Wird ausgeführt, wenn kein Fehler auftritt
	print("Keine Fehler")
finally:  # Wird immer ausgeführt, auch wenn kein Fehler auftritt
	print("Try-Except fertig")

# Übung 1
# Erstelle ein Programm, das den User nach zwei Integern fragt
# Falls der User zwei Integer eingibt sollen diese addiert und das Ergebnis in der Konsole ausgegeben werden und das Programm kann beendet werden
# Falls der Benutzer einen falschen Typen eingibt soll das Programm ihn darauf hinweisen, das nur Integer akzeptiert werden und ihn erneut nach den Zahlen fragen

# Übung 2
# Definiere eine beliebige Liste
# Erstelle ein Programm, das den User fragt, das wievielte Element in der Konsole ausgegeben werden soll
# Falls die Zahl außerhalb des Listen-Indexes liegt soll ein Fehler geworfen und der User darauf hingewiesen werden

# Übung 3
# Füge der beschleunigen Funktion deiner Fahrzeug-Klasse aus Modul 9 eine eigene Exception hinzu:
#    - Sie soll geworfen werden, falls die Höchstgeschwindigkeit überschritten wird
