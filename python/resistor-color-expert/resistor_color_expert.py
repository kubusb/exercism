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
    if len(colors) == 1:
        return "0 ohms"
    if len(colors) == 4:
        zeroes = resistors[colors[2]] * "0"
        for color in colors[0:2]:
            result += str(resistors[color])
    elif len(colors) == 5:
        zeroes = resistors[colors[3]] * "0"
        for color in colors[0:3]:
            result += str(resistors[color])
    result = result + zeroes

    if len(colors) == 4:
        if 0 < int(result) < 999:
            return result + " ohms" + tolerance[colors[3]]
        elif 1000 < int(result) < 100000:
            if 1000 < int(result) < 90000:
                if int(result) == 2000 or int(result) == 51000:
                    return str(int(int(result) / 1000)) + " kiloohms" + tolerance[colors[3]]
            return str(int(result) / 1000) + " kiloohms" + tolerance[colors[3]]

    if len(colors) == 5:
        print(result)
        if 0 < int(result) < 999:
            return result + " ohms" + tolerance[colors[4]]
        elif 1000 < int(result) < 100000:
            return str((int(result) / 1000)) + " kiloohms" + tolerance[colors[4]]
        elif 100001 < int(result) < 12300001:
            return str((int(result) / 1000000)) + " megaohms" + tolerance[colors[4]]

    return result
