def largest_product(series, size):
    # Check for invalid inputs
    if size < 0:
        raise ValueError("span must not be negative")
    if size > len(series):
        raise ValueError("span must be smaller than string length")
    if not series.isdigit():
        raise ValueError("digits input must only contain digits")
    if size == 0:
        return 1

    # Convert the series string to a list of integers
    digits = [int(d) for d in series]
    
    # Initialize the maximum product
    max_product = 0
    
    # Iterate through all possible series of the given size
    for i in range(len(digits) - size + 1):
        # Calculate the product of the current series
        product = 1
        for j in range(size):
            product *= digits[i + j]
        
        # Update the maximum product if necessary
        max_product = max(max_product, product)
    
    return max_product
