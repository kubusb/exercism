def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    
    def generate_row(n):
        if n == 0:
            return [1]
        elif n == 1:
            return [1, 1]
        else:
            prev_row = generate_row(n - 1)
            new_row = [1]
            for i in range(len(prev_row) - 1):
                new_row.append(prev_row[i] + prev_row[i + 1])
            new_row.append(1)
            return new_row
    
    return [generate_row(i) for i in range(row_count)]
