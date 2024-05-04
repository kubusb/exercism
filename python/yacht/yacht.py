# Define constants for categories
ONES = "Ones"
TWOS = "Twos"
THREES = "Threes"
FOURS = "Fours"
FIVES = "Fives"
SIXES = "Sixes"
FULL_HOUSE = "Full House"
FOUR_OF_A_KIND = "Four of a Kind"
LITTLE_STRAIGHT = "Little Straight"
BIG_STRAIGHT = "Big Straight"
CHOICE = "Choice"
YACHT = "Yacht"

def score(dice, category):
    if category == ONES:
        return dice.count(1) * 1
    elif category == TWOS:
        return dice.count(2) * 2
    elif category == THREES:
        return dice.count(3) * 3
    elif category == FOURS:
        return dice.count(4) * 4
    elif category == FIVES:
        return dice.count(5) * 5
    elif category == SIXES:
        return dice.count(6) * 6
    elif category == FULL_HOUSE:
        unique_dice = set(dice)
        if len(unique_dice) == 2 and (dice.count(dice[0]) in [2, 3]):
            return sum(dice)
        else:
            return 0
    elif category == FOUR_OF_A_KIND:
        for die in set(dice):
            if dice.count(die) >= 4:
                return die * 4
        return 0
    elif category == LITTLE_STRAIGHT:
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
    elif category == BIG_STRAIGHT:
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
    elif category == CHOICE:
        return sum(dice)
    elif category == YACHT:
        return 50 if len(set(dice)) == 1 else 0
    else:
        return 0
