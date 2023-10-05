# Model Klasse
# Klasse die Datensätze aus der Tabelle repräsentieren kann
class User:
	def __init__(self, user):
		self._id = user[0]
		self._vorname = user[1]

	@property
	def id(self):
		return self._id

	@property
	def vorname(self):
		return self._vorname