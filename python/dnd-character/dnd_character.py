import random

def modifier(constitution):
    return (constitution - 10) // 2

class Character:
    def __init__(self):
        self.strength = self.roll_ability()
        self.dexterity = self.roll_ability()
        self.constitution = self.roll_ability()
        self.intelligence = self.roll_ability()
        self.wisdom = self.roll_ability()
        self.charisma = self.roll_ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def roll_ability(self):
        # Roll four 6-sided dice
        dice = [random.randint(1, 6) for _ in range(4)]
        # Sum the largest three dice
        total = sum(sorted(dice)[1:])
        return total

    def ability(self):
        return random.randint(3, 18)
