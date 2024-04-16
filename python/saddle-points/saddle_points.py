def saddle_points(matrix):
    # Check for irregular matrix where rows have different lengths
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")
    
    if matrix == []:
        return []

    saddle_points = []
    row_len = len(matrix)
    col_len = len(matrix[0])

    # Check each element in the matrix
    for i in range(row_len):
        for j in range(col_len):
            element = matrix[i][j]
            # Check if the element is the maximum in its row
            row_max = all(element >= matrix[i][k] for k in range(col_len))
            # Check if the element is the minimum in its column
            col_min = all(element <= matrix[k][j] for k in range(row_len) if j < len(matrix[k]))

            if row_max and col_min:
                # Adjusting the output to be a dictionary with "row" and "column"
                saddle_points.append({"row": i + 1, "column": j + 1})

    return saddle_points
