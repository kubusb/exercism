import sys

def grep(pattern, flags, files):
    results = []
    
    # Parse flags
    line_numbers = '-n' in flags
    only_filenames = '-l' in flags
    case_insensitive = '-i' in flags
    invert_match = '-v' in flags
    exact_match = '-x' in flags
    
    for file in files:
        try:
            with open(file, 'r') as f:
                lines = f.readlines()
                
            file_has_match = False
            for i, line in enumerate(lines, 1):
                line = line.rstrip('\n')
                
                # Apply case insensitivity if flag is set
                if case_insensitive:
                    search_condition = pattern.lower() in line.lower()
                    if exact_match:
                        search_condition = pattern.lower() == line.lower()
                else:
                    search_condition = pattern in line
                    if exact_match:
                        search_condition = pattern == line
                
                # Invert match if flag is set
                if invert_match:
                    search_condition = not search_condition
                
                if search_condition:
                    file_has_match = True
                    if only_filenames:
                        if file not in results:
                            results.append(file + '\n')
                        break
                    else:
                        result = ''
                        if len(files) > 1:
                            result += f"{file}:"
                        if line_numbers:
                            result += f"{i}:"
                        result += line + '\n'
                        results.append(result)
            
            if only_filenames and file_has_match and file + '\n' not in results:
                results.append(file + '\n')
                
        except FileNotFoundError:
            print(f"File not found: {file}", file=sys.stderr)
    
    return ''.join(results)
