def rebase(input_base, digits, output_base):
    # Validate input base
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    
    # Validate output base
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    # Convert input to decimal (base 10)
    decimal = 0
    for digit in digits:
        if not 0 <= digit < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        decimal = decimal * input_base + digit
    
    # Handle special case for decimal 0
    if decimal == 0:
        return [0]
    
    # Convert decimal to output base
    output = []
    while decimal > 0:
        output.insert(0, decimal % output_base)
        decimal //= output_base
    
    return output
