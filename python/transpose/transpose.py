def transpose(lines):
    # If lines are empty, return nothing.
    if len(lines) == 0:
        return ""
    
    # If there is only one line, transposition will be easy:
    if not "\n" in lines:
        newline = "\n"
        return newline.join(list(lines))
    
    # Count number of symbols in each line, decide which line is the longest.
    # Edit if lines are too short - add spaces to the END of the lines.
    # Then transpose 1:1 keeping the spaces.