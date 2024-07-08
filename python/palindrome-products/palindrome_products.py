def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    return find_palindrome(min_factor, max_factor, largest=True)


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    return find_palindrome(min_factor, max_factor, largest=False)


def find_palindrome(min_factor, max_factor, largest):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    result = None
    factors = []

    if largest:
        outer_range = range(max_factor, min_factor - 1, -1)
        inner_range = lambda x: range(max_factor, x - 1, -1)
    else:
        outer_range = range(min_factor, max_factor + 1)
        inner_range = lambda x: range(x, max_factor + 1)

    for i in outer_range:
        for j in inner_range(i):
            product = i * j
            if result is not None:
                if (largest and product < result) or (not largest and product > result):
                    break
            if is_palindrome(product):
                if result is None or (largest and product > result) or (not largest and product < result):
                    result = product
                    factors = []
                if (min(i, j), max(i, j)) not in factors:
                    factors.append((min(i, j), max(i, j)))
                if largest:
                    break  # We found the largest palindrome, no need to continue inner loop

    return (result, factors)


def is_palindrome(n):
    return str(n) == str(n)[::-1]