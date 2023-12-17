def is_armstrong_number(number):
    result = 0
    for digit in str(number):
        ingreedient = int(digit) ** len(str(number))
        result = result + ingreedient
    if result == number:
        return True
    return False
