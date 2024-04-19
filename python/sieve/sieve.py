def primes(limit):
    if limit < 2:
        return []  # No prime numbers less than 2

    # Initialize a boolean array where True means the index is assumed prime
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    # Sieve of Eratosthenes
    p = 2
    while (p * p <= limit):
        if (is_prime[p] == True):
            # Marking multiples of p as not prime
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1

    # Collecting all prime numbers
    primes = [p for p in range(limit + 1) if is_prime[p]]
    return primes
