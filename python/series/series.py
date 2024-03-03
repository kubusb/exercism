""" Series """
def slices(series, length):
    """ Series """
    result = []

    # Error handling
    if length == 0:
        # if the slice length is zero.
        raise ValueError("slice length cannot be zero")

    if length < 0:
        # if the slice length is negative.
        raise ValueError("slice length cannot be negative")

    if series == "" or series is None:
        # if the series provided is empty.
        raise ValueError("series cannot be empty")

    if len(series) < length:
        # if the slice length is longer than the series.
        raise ValueError("slice length cannot be greater than series length")
    
    # Handle the case, where slice size = series
    if len(series) == length:
        return [series]

    if len(series) > length:
        current_position = 0
        while (current_position + length) <= len(series):
            result.append(str(series[current_position:(current_position+length)]))
            current_position += 1
    
    return result