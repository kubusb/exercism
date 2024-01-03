def color_code(color):
    resistors = {
        'black' : 0,
        'brown' : 1,
        'red'   : 2,
        'orange': 3,
        'yellow': 4,
        'green' : 5,
        'blue'  : 6,
        'violet': 7,
        'grey'  : 8,
        'white' : 9
    }
    return resistors[color]


def colors():
    result = []
    resistors = {
        'black' : 0,
        'brown' : 1,
        'red'   : 2,
        'orange': 3,
        'yellow': 4,
        'green' : 5,
        'blue'  : 6,
        'violet': 7,
        'grey'  : 8,
        'white' : 9
    }

    for key in resistors:
        result.append(key)

    return result
