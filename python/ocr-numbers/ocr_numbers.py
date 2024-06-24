# Define the OCR digit patterns
DIGITS = {
    ' _ | ||_|   ': '0',
    '     |  |   ': '1',
    ' _  _||_    ': '2',
    ' _  _| _|   ': '3',
    '   |_|  |   ': '4',
    ' _ |_  _|   ': '5',
    ' _ |_ |_|   ': '6',
    ' _   |  |   ': '7',
    ' _ |_||_|   ': '8',
    ' _ |_| _|   ': '9',
}

def convert(input_grid):
    # Ensure input_grid is a list of strings
    if isinstance(input_grid, str):
        lines = input_grid.split('\n')
    elif isinstance(input_grid, list):
        lines = input_grid
    else:
        raise ValueError("Invalid input format")

    # Validate the size of the input grid
    if len(lines) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(len(line) % 3 != 0 for line in lines):
        raise ValueError("Number of input columns is not a multiple of three")

    # Process each group of 4 lines
    result = []
    for i in range(0, len(lines), 4):
        result.append(convert_line(lines[i:i+4]))
    
    # Join the results with commas
    return ','.join(result)

def convert_line(line_block):
    digits = []
    num_digits = len(line_block[0]) // 3
    for i in range(num_digits):
        digit = ''.join(line[i*3:(i+1)*3] for line in line_block)
        digits.append(DIGITS.get(digit, '?'))
    return ''.join(digits)
