import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature: {} of level {}".format(
            self.name, self.level
        )

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness/10

        return base_roll*fire_modifier*scale_modifier

    def breath_fire(self):
        pass


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2

    def can_hide(self):
        pass


class Wizard(Creature):
    def smile(self, creature):
        print("The wizard {} smiles at {}".format(self.name, creature.name))

        my_roll = self.get_defensive_roll()
        #creature_roll = random.randint(1, 12) * creature.level
        creature_roll = creature.get_defensive_roll()

        print("Your wizard rolled {}...".format(my_roll))
        print("The {} rolls {}...".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("The Wizard wins! And triumphs over {}".format(creature.name))
            print()
            return True
        else:
            print("The Creature {} wins! And the Wizard has been DEFEATED".format(creature.name))
            print()
            return False





