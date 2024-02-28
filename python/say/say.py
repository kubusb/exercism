""" Converting numbers into words - exercism"""
simple_digit_mapping = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
    20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
    70: "seventy", 80: "eighty", 90: "ninety",
}

def say(number):
    """ Converting numbers into words"""
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    if number <= 20:
        return simple_digit_mapping[number]

    if number < 100:
        tens, remainder = divmod(number, 10)
        tens_word = simple_digit_mapping[tens * 10]
        return f"{tens_word}-{simple_digit_mapping[remainder]}" if remainder else tens_word

    if number < 1000:
        hundreds, remainder = divmod(number, 100)
        return f"{simple_digit_mapping[hundreds]} hundred" + (f" {say(remainder)}" if remainder else "")

    if number < 10_000:
        thousands, remainder = divmod(number, 1000)
        return f"{simple_digit_mapping[thousands]} thousand" + (f" {say(remainder)}" if remainder else "")

    if number <= 1_000_000:
        millions, remainder = divmod(number, 1_000_000)
        return f"{simple_digit_mapping[millions]} million" + (f" {say(remainder)}" if remainder else "")
