import re

class PhoneNumber:
    def __init__(self, number):
        # Remove all non-digit characters
        cleaned_number = ''.join(filter(str.isdigit, number))

        if re.search(r'[a-z]', number):
            raise ValueError("letters not permitted")

        punctuation_pattern = r'[@!:]'
        if re.search(punctuation_pattern, number):
        # if a phone number has punctuation in place of some digits.
            raise ValueError("punctuations not permitted")

        if len(cleaned_number) < 10:
            raise ValueError("must not be fewer than 10 digits")

        if len(cleaned_number) > 11:
            raise ValueError("must not be greater than 11 digits")
        
        if len(cleaned_number) == 11 and cleaned_number[0] != "1":
        # if a phone number has 11 digits, but starts with a number other than 1.
            raise ValueError("11 digits must start with 1")

        if cleaned_number[-7:].startswith("0"):
        # if a phone number has an exchange code that starts with 0.
            raise ValueError("exchange code cannot start with zero")

        if cleaned_number[-7:].startswith("1"):
        # if a phone number has an exchange code that starts with 1.
            raise ValueError("exchange code cannot start with one")

        if cleaned_number[-10:].startswith("0"):
        # if a phone number has an area code that starts with 0.
            raise ValueError("area code cannot start with zero")

        if cleaned_number[-10:].startswith("1"):
        # if a phone number has an area code that starts with 1.
            raise ValueError("area code cannot start with one")

        # Set the cleaned number as the instance attribute
        if len(cleaned_number) == 11 and cleaned_number.startswith('1'):
            self.number = cleaned_number[1:]
        else:
            self.number = cleaned_number
            self.area_code = cleaned_number[0:3]
        
    def pretty(self):
        return f"({self.number[0:3]})-{self.number[3:6]}-{self.number[6:]}"

    def __str__(self):
        # Format the phone number as XXXXXXXXXX
        return self.number
