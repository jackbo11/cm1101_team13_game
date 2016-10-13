import random


class Player:
    def __init__(self, name, gender, age, smoker):
        self.name = name.title()
        self.gender = gender.title()
        self.age = age
        self.smoker = bool(smoker)
        self.__money = 30.0
        self.__drunkenness = 0
        self.__drink_left = 0
        self.__happiness = 1
        self.__cig_left = 0
        if self.smoker:
            self.__cig_left = 10

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        if money > 50.0:
            self.__money = 50
        elif money < 0.0:
            self.__money = 0
        else:
            self.money = money

    @property
    def drunkenness(self):
        return self.__drunkenness

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
        if happiness > 5:
            self.__happiness = 5
        elif happiness < 0:
            self.__happiness = 0
        else:
            self.__happiness = happiness

    @property
    def cig_left(self):
        return self.__cig_left

    @cig_left.setter
    def cig_left(self, cig_left):
        if cig_left > 30:
            self.__cig_left = 30
        elif cig_left < 0:
            self.__cig_left = 0
        else:
            self.__cig_left = cig_left

    def increase_happiness(self, increment):
        self.happiness = self.happiness + increment

    def smoke(self):
        if self.smoker:
            if self.cig_left > 0:
                self.cig_left -= 1
                self.increase_happiness(random.random())
                return "You smoke a cigarette."
            else:
                return "You have no cigarettes left!"
        else:
            return "You are a non smoker!"
