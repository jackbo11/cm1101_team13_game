import random
import map
import items


class Player:
    def __init__(self, name="Player", gender="Male", age=18, smoker="no"):
        self.name = name.title()
        self.gender = self.__determine_gender(gender)
        self.age = age
        self.smoker = self.__determine_smoker(smoker)
        self.inventory = [items.item_id, items.item_driving_license, items.item_playing_cards, items.item_money]
        self.current_room = map.rooms["Talybont"]
        self.__money = 30.0
        self.__drunkenness = 0
        self.__drink_left = 0
        self.__happiness = 1
        self.__cig_left = 0
        if self.smoker:
            self.__cig_left = 10

    @staticmethod
    def __determine_gender(gender_to_determine):
        gender_to_determine = gender_to_determine.lower()
        if gender_to_determine:
            if gender_to_determine[0] == "m":
                return "Male"
            elif gender_to_determine[0] == "f":
                return "Female"
        else:
            return "Unknown"

    @staticmethod
    def __determine_smoker(smoker_to_determine):
        if smoker_to_determine:
            smoker_to_determine = smoker_to_determine.lower()
            if smoker_to_determine[0] == "y" or smoker_to_determine == "true":
                return True
            else:
                return False
        else:
            return False

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        if money > 50.0:
            self.__money = 50.0
        elif money < 0.0:
            self.__money = 0.0
        else:
            self.__money = money

    @property
    def drunkenness(self):
        return round(self.__drunkenness, 1)

    @drunkenness.setter
    def drunkenness(self, drunkenness):
        if drunkenness > 10:
            self.__drunkenness = 10
        elif drunkenness < 0:
            self.__drunkenness = 0
        else:
            self.__drunkenness = drunkenness

    @property
    def drink_left(self):
        return self.__drink_left

    @drink_left.setter
    def drink_left(self, drink_left):
        if drink_left > 5:
            self.__drink_left = 5
        elif drink_left < 0:
            self.__drink_left = 0
        else:
            self.__drink_left = drink_left

    @property
    def happiness(self):
        return self.__happiness

    @happiness.setter
    def happiness(self, happiness):
        if happiness > 10:
            self.__happiness = 10
        elif happiness < 0:
            self.__happiness = 0
        else:
            self.__happiness = happiness

    @property
    def cig_left(self):
        return self.__cig_left

    @cig_left.setter
    def cig_left(self, cig_left):
        if cig_left > 10:
            self.__cig_left = 10
        elif cig_left < 0:
            self.__cig_left = 0
        else:
            self.__cig_left = cig_left

    def increase_happiness(self, increment):
        self.happiness = self.happiness + increment

    def increase_happiness_random(self):
        self.increase_happiness(round(random.random(), 1))

    def increase_drunkenness(self, increment):
        self.drunkenness = self.drunkenness + increment

    def increase_drunkenness_random(self):
        self.increase_drunkenness(round(random.random(), 1))

    def smoke(self):
        if self.smoker:
            if self.cig_left > 0:
                self.cig_left -= 1
                self.increase_happiness_random()
                return "You smoke a cigarette."
            else:
                return "You have no cigarettes left!"
        else:
            return "You are a non smoker!"

    def drink(self, amount=1):
        for i in range(amount):
            self.increase_drunkenness_random()
            self.increase_happiness_random()
            self.drink_left -= 1
        return "You drink."

    def fill_drink(self, amount=5):
        self.drink_left += amount

    def pay(self, amount):
        self.money = self.money - amount

    def get_stats(self):
        return """
        -----------------------------------
        Stats for {0}
        -----------------------------------
        Gender: {1}
        Age: {2}
        Happiness: {3}/10
        Drunkenness: {4}/10
        Drink left: {5}/5
        Money: £{6}
        Cigarettes left {7}/10
        ====================================

        """.format(self.name, self.gender, self.age, self.happiness, self.drunkenness, self.drink_left, self.money,
                   self.cig_left)
