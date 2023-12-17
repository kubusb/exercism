"""
Collatz Conjecture
"""
def steps(number):
    """
    This function terurns number of steps needed to complete Collatz Conjecture
    """
    iteration = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    else:
        while number > 1:
            if number % 2 == 0:
                number /= 2
                iteration += 1
            else:
                number = 3 * number + 1
                iteration += 1
        return iteration
