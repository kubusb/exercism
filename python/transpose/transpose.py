def transpose(lines):
    # If lines are empty, return nothing.
    if len(lines) == 0:
        return ""
    
    # If there is only one line, transposition will be easy:
    if not "\n" in lines:
        newline = "\n"
        return newline.join(list(lines))