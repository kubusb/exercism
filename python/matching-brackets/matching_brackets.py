def is_paired(test_string):
    # Dictionary to hold the matching opening and closing characters
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    # Stack to keep track of opening brackets
    stack = []

    # Iterate through each character in the string
    for char in test_string:
        # If the character is an opening bracket, push it onto the stack
        if char in bracket_pairs.values():
            stack.append(char)
        # If the character is a closing bracket
        elif char in bracket_pairs:
            # If the stack is empty or the top of the stack does not match the corresponding opening bracket, return False
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            # If the stack is not empty and the top matches, pop the top element from the stack
            else:
                stack.pop()

    # If the stack is empty at the end, all brackets were properly closed and nested; return True
    # Otherwise, return False
    return not stack
