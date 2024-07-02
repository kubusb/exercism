def annotate(minefield):
    if not minefield:
        return []
    
    if not all(len(row) == len(minefield[0]) for row in minefield):
        raise ValueError("The board is invalid with current input.")

    height = len(minefield)
    width = len(minefield[0])
    
    def count_adjacent_mines(x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < height and 0 <= ny < width and minefield[nx][ny] == '*':
                    count += 1
        return count
    
    result = []
    for x in range(height):
        row = ""
        for y in range(width):
            if minefield[x][y] not in [' ', '*']:
                raise ValueError("The board is invalid with current input.")
            if minefield[x][y] == '*':
                row += '*'
            else:
                mine_count = count_adjacent_mines(x, y)
                row += str(mine_count) if mine_count > 0 else ' '
        result.append(row)
    
    return result
