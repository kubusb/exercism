def rectangles(strings):
    # Step 1: Check if the input list is empty
    if not strings:
        return 0
    
    # Parse the diagram into a 2D list of characters
    grid = [list(line) for line in strings]
    rows = len(grid)
    cols = len(grid[0])
    
    def is_corner(x, y):
        return grid[x][y] == '+'
    
    def is_horizontal_edge(x1, y1, y2):
        return all(grid[x1][y] in ['-', '+'] for y in range(y1, y2 + 1))
    
    def is_vertical_edge(y1, x1, x2):
        return all(grid[x][y1] in ['|', '+'] for x in range(x1, x2 + 1))
    
    count = 0
    for x1 in range(rows):
        for y1 in range(cols):
            if is_corner(x1, y1):
                for x2 in range(x1 + 1, rows):
                    for y2 in range(y1 + 1, cols):
                        if is_corner(x1, y2) and is_corner(x2, y1) and is_corner(x2, y2):
                            if is_horizontal_edge(x1, y1, y2) and is_horizontal_edge(x2, y1, y2) and \
                               is_vertical_edge(y1, x1, x2) and is_vertical_edge(y2, x1, x2):
                                count += 1
    return count
