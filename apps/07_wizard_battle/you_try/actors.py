import random


class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, other_creature):
        pass


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature: {} of level {}".format(
            self.name, self.level
        )


