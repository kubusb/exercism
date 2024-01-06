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

suffixes = {
    0 : "",
    1 : "deca",
    2 : "hecto",
    3 : "kilo",
    4 : "mega",
    5 : "giga",
    6 : "tera",
}

def label(colors):
    result = ""
    number_of_colors = 1
    for color in colors:
        if number_of_colors < 3:
            result += str(resistors[color])
            number_of_colors += 1
        zeroes = resistors[colors[2]] * "0"
    print(int(result))
    print(zeroes)
    if len(zeroes) == 0:
        return str(int(result)) + " ohms"
    elif len(zeroes) == 1:
        return result + "0 ohms"
    elif len(zeroes) == 2:
        return result[0] + " kiloohms"
    elif len(zeroes) == 3:
        return result + " kiloohms"
    elif len(zeroes) == 4:
        return result + "0 kiloohms"
    elif len(zeroes) == 6:
        return result + " megaohms"
    elif len(zeroes) == 9:
        return result + " gigaohms"
