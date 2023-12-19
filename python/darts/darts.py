import math

def score(x, y):
    x = abs(x)
    y = abs(y)

    distance_from_center_0 = math.sqrt(x ** 2 + y ** 2)
    if distance_from_center_0 > 10:
        return 0

    elif 10 >= distance_from_center_0 > 5:
        return 1

    elif 5 >= distance_from_center_0 > 1:
        return 5

    elif distance_from_center_0 <= 1:
        return 10
