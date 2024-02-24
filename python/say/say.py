simple_digit_mapping = {
    0:"zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"tewlve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",
    20:"twenty",
    30:"thirty",
    40:"fourty",
    50:"fifty",
    60:"sixsty",
    70:"seventy",
    80:"eighty",
    90:"ninety",
}

def say(number):
    number_list = []
    number_str = str(number)
    number_str_rev = str(number)[::-1]
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    if 0 <= number <= 99 :
        number_list.append(number_str)
        if 0 <= number <= 20:
            return simple_digit_mapping[number]
        if 21 <= number <= 29:
            return "twenty-" + simple_digit_mapping[number-20]
        if 31 <= number <= 39:
            return "thitry-" + simple_digit_mapping[number-30]
        if 41 <= number <= 49:
            return "fourty-" + simple_digit_mapping[number-40]
        if 51 <= number <= 59:
            return "fifty-" + simple_digit_mapping[number-50]
        if 61 <= number <= 69:
            return "sixty-" + simple_digit_mapping[number-60]
        if 71 <= number <= 79:
            return "seventy-" + simple_digit_mapping[number-70]
        if 81 <= number <= 89:
            return "eighty-" + simple_digit_mapping[number-80]
        if 91 <= number <= 99:
            return "ninety-" + simple_digit_mapping[number-90]
        else:
            return simple_digit_mapping[number]
    print(number_list)
