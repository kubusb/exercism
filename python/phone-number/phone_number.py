class PhoneNumber:
    def __init__(self, number):
        # Remove all non-digit characters
        cleaned_number = ''.join(filter(str.isdigit, number))
        
        # Set the cleaned number as the instance attribute
        self.number = cleaned_number
        
    def __str__(self):
        # Format the phone number as XXXXXXXXXX
        return self.number
