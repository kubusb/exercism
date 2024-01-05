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

def value(colors):
    result = ""
    number_of_colors = 1
    for color in colors:
        if number_of_colors < 3:
            result += str(resistors[color])
            number_of_colors += 1
    return int(result)
