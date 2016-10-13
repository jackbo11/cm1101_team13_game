class player:
	def __init__(self, name, gender, age, smoker):
		self.__name = name.title()
		self.__gender = gender.title()
		self.__age = age
		self.__smoker = bool(smoker)
		self.__money = 30.0
		self.__drunkenness = 0
		self.__drink_left = 0
		self.__happiness = 1
		self.__cig_left = 0
		if self.__smoker:
			self.__cig_left = 10
		
	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		print("You cannot change your name!")

    @property
	def gender(self):
		return self.__gender

	@gender.setter
	def gender(self, gender):
		print("You cannot change your gender!")