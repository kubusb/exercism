import random
from math import floor

class Character:
    def __init__(self):
        self.strength = self.roll_ability()
        self.dexterity = self.roll_ability()
        self.constitution = self.roll_ability()
        self.intelligence = self.roll_ability()
        self.wisdom = self.roll_ability()
        self.charisma = self.roll_ability()
        self.hitpoints = self.calculate_hitpoints()

    def roll_ability(self):
        dice = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(dice)[1:])

    def calculate_hitpoints(self):
        constitution_modifier = floor((self.constitution - 10) / 2)
        return 10 + constitution_modifier

def modifier(self):
    constitution_modifier = floor((Character.constitution - 10) / 2)
    return 10 + constitution_modifier