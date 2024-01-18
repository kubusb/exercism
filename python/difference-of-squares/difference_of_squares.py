def square_of_sum(number):
    result = 0
    for number in range(1, (number +  1)):
        result +=  number
    return result ** 2

def sum_of_squares(number):
    result = 0
    for number in range(1, number + 1):
        result += number ** 2
    return result


def difference_of_squares(number):
    return (square_of_sum(number) - sum_of_squares(number))
