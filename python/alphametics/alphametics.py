from itertools import permutations

def solve(puzzle):
    # Extract unique letters and numbers from the puzzle
    letters = ''.join(set(c for c in puzzle if c.isalpha()))
    
    # Get the words from the puzzle
    words = puzzle.replace('+', ' ').replace('==', ' ').split()
    
    # Check for leading zeros
    first_letters = set(word[0] for word in words)
    
    # Generate all possible digit permutations
    for perm in permutations('0123456789', len(letters)):
        sol = dict(zip(letters, perm))
        
        # Skip solutions with leading zeros
        if any(sol[letter] == '0' for letter in first_letters):
            continue
        
        # Evaluate the equation
        if sum(int(''.join(sol[c] for c in word)) for word in words[:-1]) == \
           int(''.join(sol[c] for c in words[-1])):
            return {k: int(v) for k, v in sol.items()}
    
    return None