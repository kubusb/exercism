import re

def answer(question):
    what_is = re.findall(r"^What is (-?[0-9]\d*)\?", question)
    addition = re.findall(r"^What is (-?[0-9]\d*) plus (-?[0-9]\d*)\?", question)
    subtraction = re.findall(r"^What is (-?[0-9]\d*) minus (-?[0-9]\d*)\?", question)
    multiplication = re.findall(r"^What is (-?[0-9]\d*) multiplied by (-?[0-9]\d*)\?", question)
    division = re.findall(r"^What is (-?[0-9]\d*) divided by (-?[0-9]\d*)\?", question)
    if len(what_is) > 0:
        return int(what_is[0])
    elif len(addition) > 0:
        return int(addition[0][0]) + int(addition[0][1])
    elif len(subtraction) > 0:
        return int(subtraction[0][0]) - int(subtraction[0][1])
    elif len(multiplication) > 0:
        return int(multiplication[0][0]) * int(multiplication[0][1])
    elif len(division) > 0:
        return int(division[0][0]) / int(division[0][1])
    else:
        raise ValueError("unknown operation")
    return False
