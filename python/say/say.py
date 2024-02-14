def say(number):
    if number < 1 or number > 999_999_999_999:
        raise ValueError("input out of range")
