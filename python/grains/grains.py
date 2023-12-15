list_of_numbers_of_grains = []

def square(number):
    global list_of_numbers_of_grains
    number_of_grains = 0
    board_field_number = 1
    number = int(number)
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    while board_field_number <= number:
        if board_field_number == 1:
            number_of_grains = 1
            list_of_numbers_of_grains = [1]
        else:
            number_of_grains = list_of_numbers_of_grains[-1] * 2
            list_of_numbers_of_grains.append(number_of_grains)
        board_field_number = board_field_number + 1
    return number_of_grains

def total():
    global list_of_numbers_of_grains
    suma = 0
    for each_result in list_of_numbers_of_grains:
        suma = suma + each_result
    return suma
