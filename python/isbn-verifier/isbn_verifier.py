def is_valid(isbn):
    control_sum = 0
    index = 10
    isbn = str(isbn.replace("-", ""))
    if len(isbn) == 10:
        if isbn[0:8].isdigit() and (isbn[9].isdigit() or isbn[9] == "X"):
            if isbn[9].isdigit():
                control_digit = int(isbn[9])
            elif isbn[9].upper() == "X":
                control_digit = 10
            else:
                return False
            for digit in isbn[0:9]:
                control_sum = control_sum + index * int(digit)
                index -= 1
            control_sum = control_sum + int(control_digit)
            return bool(control_sum % 11 == 0)
        return False
    return False
