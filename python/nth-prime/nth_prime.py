def prime(number):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if number < 1:
        raise ValueError('there is no zeroth prime')

    current_number = 2
    found_prime = 1

    while found_prime <= number:
        if is_prime(current_number):
            if found_prime == number:
                return current_number
            current_number += 1
            found_prime += 1
        else:
            current_number += 1
