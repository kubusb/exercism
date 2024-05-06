def egg_count(display_value):
    # Let's start by converting decimal to binary:
    quotient = display_value
    binary_result = []
    while quotient > 0:
        remainder = int(quotient % 2)
        quotient = int(quotient / 2)
        binary_result.append(remainder)
    return binary_result.count(1)
