class player:
	def __init__(self, name, gender, age, smoker):
		self.name = name
		self.gender = gender
		self.age = age
		self.smoker = smoker
		self.money = 30.0
		self.drunkenness = 0
		self.drink_left = 0
		self.happiness = 1
		self.cig_left = 0
		if self.smoker:
			self.cig_left = 10
		