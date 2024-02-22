simple_digit_mapping = {
    0:"zero"
    1:"one"
    2:"two"
    3:"three"
    4:"four"
    5:"five"
    6:"six"
    7:"seven"
    8:"eight"
    9:"nine"
}

def say(number):
    number_list = []
    current_split = ""
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    for index, digit in enumerate(str(number)):
        if len(str(number)) <= 3:
            number_list.append(number)
            break
        else:
            print("Number was: {}, I:{}, D:{}".format(number, index, digit))
    print("Number is shorter than 4!")
    print(number_list)
    #     current_split += digit
    #     if (index + 1) % 3 == 0:
    #         number_list.appnd(current_split)
    #         current_split = ""
    # print(number_list)