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
    # for index, digit in enumerate(number_str):
    #     print("Number was: {}, I:{}, D:{}".format(number, index, digit))
    #     # Step 1:
    print(number_list)
