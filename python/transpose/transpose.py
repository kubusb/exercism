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
    squared_list_of_lines = []
    for line in list_of_lines:
        if len(line) < counter_longest_line_symbol_count:
            line = line + (counter_longest_line_symbol_count - len(line))*" "
        squared_list_of_lines.append(line)

    
    # Then transpose 1:1 keeping the spaces.
    # line_counter = 0
    # line_position = 0
    # result = []
    # transposed_line = ""
    # for line in list_of_lines:
    #     while line_counter < len(list_of_lines):
    #         transposed_line = transposed_line + list_of_lines[line_counter][line_position]
    #         line_counter += 1
    #         line_position += 1
    #     result.append(transposed_line)
    # print(result)
    print(squared_list_of_lines)
    #print("TyleLinii:-{}-,\nPoTyleZnakow:-{}-".format(len(list_of_lines), counter_longest_line_symbol_count))
    print("WynikTyleLinii:={}=\nPoTyleZnakow={}=".format(counter_longest_line_symbol_count, len(list_of_lines)))
    
    counter = 0
    transposed_line = ""
