def is_triangle(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a + b >= c and b + c >= a and a + c >= b and a > 0 and b > 0 and c > 0:
        return True
    else:
        return False

def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if is_triangle(sides) is True:
        if a == b and b == c:
            return True
    return False


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if is_triangle(sides) is True:
        if a == b or a == c or b == c:
            return True
    return False


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if is_triangle(sides) is True:
        if a != b and a != c and b != c:
            return True
    return False