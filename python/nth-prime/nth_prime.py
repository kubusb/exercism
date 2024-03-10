def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')

    current_number = 2
    found_prime = 1

    while found_prime <= number:
        if found_prime == number:
            return current_number
        break
# Sprawdzanie liczby: Dla każdej liczby sprawdź, czy jest liczbą pierwszą. Można to zrobić, dzieląc ją przez wszystkie liczby mniejsze od niej i większe od 1. Jeśli żaden dzielnik nie dzieli jej bez reszty, liczba jest pierwsza.
# Licznik: Jeśli liczba jest pierwsza, zwiększ licznik liczb pierwszych o 1. Jeśli licznik równa się n, znaleziono n-tą liczbę pierwszą.
# Powtórzenie: Jeśli nie osiągnięto jeszcze n-tej liczby pierwszej, przejdź do następnej liczby i powtórz proces.