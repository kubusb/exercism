def proverb(*inputs, qualifier):
    if not inputs:
        return []

    proverb = []
    for i in range(len(inputs) - 1):
        line = f"For want of a {inputs[i]} the {inputs[i + 1]} was lost."
        proverb.append(line)
    
    if qualifier is None:
        last_line = f"And all for the want of a {inputs[0]}."  # Initialize the last line
        proverb.append(last_line)
    else:
        last_line = f"And all for the want of a {qualifier} {inputs[0]}."  # Initialize the last line
        proverb.append(last_line)       

    return proverb
