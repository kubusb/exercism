def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    result = 0
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    for i in range(1, number, 1):
        if number % i == 0:
            result += i

    if result == number:
        return "perfect"
    elif result > number:
        return "abundant"
    elif result < number:
        return "deficient"
