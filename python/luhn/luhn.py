class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")  # Remove spaces from the card number

    def valid(self):
        if not self.card_num.isdigit() or len(self.card_num) <= 1:  # Check if card_num is numeric and has at least two digits
            return False

        digits = [int(digit) for digit in self.card_num]  # Convert the card number string into a list of integers

        # Step 1: Double every second digit from the right, starting from the second rightmost digit
        for i in range(len(digits) - 2, -1, -2):
            digits[i] *= 2
            if digits[i] > 9:  # Subtract 9 if the result is greater than 9
                digits[i] -= 9

        # Step 2: Sum all the digits
        total_sum = sum(digits)

        # Step 3: Check if the total sum modulo 10 is equal to 0
        return total_sum % 10 == 0
