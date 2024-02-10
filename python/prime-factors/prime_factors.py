def factors(value):
    found_divisors = []
    divisor = 2
    while value > 1:
        if value % divisor == 0:
            found_divisors.append(divisor)
            value = value / divisor
        else:
            divisor += 1
    return found_divisors
