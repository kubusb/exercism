def transpose(lines):
    newline = "\n"
    # If lines are empty, return nothing.
    if len(lines) == 0:
        return ""
    
    # If there is only one line, transposition will be easy:
    if not "\n" in lines:
        return newline.join(list(lines))
    
    # Count number of symbols in each line, decide which line is the longest.
    counter_longest_line_symbol_count = 0
    list_of_lines = lines.split(newline)
    
    for line in list_of_lines:
        if len(line) > counter_longest_line_symbol_count:
            counter_longest_line_symbol_count = len(line)
    print("Longest line detected has the following number of chars: {}".format(counter_longest_line_symbol_count))

    # Edit if lines are too short - add spaces to the END of the lines.
    for line in list_of_lines:
        if len(line) < counter_longest_line_symbol_count:
            line = line + (counter_longest_line_symbol_count - len(line))*" "
    # Then transpose 1:1 keeping the spaces.