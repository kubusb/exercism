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

tolerance = {
    "grey" : " ±0.05%",
    "violet" : " ±0.1%",
    "blue" : " ±0.25%",
    "green" : " ±0.5%",
    "brown" : " ±1%",
    "red" : " ±2%",
    "gold" : " ±5%",
    "silver" : " ±10%"
}

def resistor_label(colors):
    result = ""
    number_of_colors = 1
    if len(colors) == 1:
        return "0 ohms"
    for color in colors:
        if number_of_colors < 3:
            result += str(resistors[color])
            number_of_colors += 1
        zeroes = resistors[colors[2]] * "0"
    print(int(result))
    print(zeroes)
    if len(zeroes) == 0:
        result = str(int(result)) + " ohms"
    elif len(zeroes) == 1:
        result = result + "0 ohms"
    elif len(zeroes) == 2:
        result = result[0] + " kiloohms"
    elif len(zeroes) == 3:
        result = result + " kiloohms"
    elif len(zeroes) == 4:
        result = result + "0 kiloohms"
    elif len(zeroes) == 6:
        result = result + " megaohms"
    elif len(zeroes) == 9:
        result = result + " gigaohms"

    if len(colors) == 4:
        return result + tolerance[colors[3]]

    if len(colors) == 5:
        return result + tolerance[colors[4]]

    return result
