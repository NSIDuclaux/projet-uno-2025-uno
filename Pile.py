class Pile:

	def __init__(self):
		self.valeurs = []

	def empiler(self, valeur):
		self.valeurs.append(valeur)

	def depiler(self):
		if self.valeurs:
			return self.valeurs.pop()
    
	def estVide(self):
		return self.valeurs == []
	
	def __str__(self):
		ch = ''
		for x in self.valeurs:
			ch = "|\t" + str(x) + "\t|" + "\n" + ch
		ch = "\nEtat de la pile:\n" + ch
		return ch