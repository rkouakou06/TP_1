# encoding : utf8
"""This script allows to create an animal."""

class Animal():
    """Class to create animals"""
    def __init__(self, species, age, diet, foot, name):
        self.species = species
        self.age = age
        self.diet = diet
        self.foot = foot
        self.name = name

    def __str__(self):
        return self.species +"/"+str(self.age) +"/"+self.diet +"/"+str(self.foot) +"/"+self.name


if __name__ == "__main__" :
    a = Animal("Test", "21", "diet", "foot", "name")
    print(a.__getattribute__)
