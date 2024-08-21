def measure(bucket_one, bucket_two, goal, start_bucket):
    # Ensure the goal is achievable
    if goal > max(bucket_one, bucket_two):
        raise ValueError("Goal is larger than both buckets")
    
    # Set up initial state based on start_bucket
    if start_bucket == "one":
        state = (bucket_one, 0)
        other_bucket = bucket_two
    elif start_bucket == "two":
        state = (0, bucket_two)
        other_bucket = bucket_one
    else:
        raise ValueError("Invalid start bucket")
    
    visited = set()
    queue = [(state, [state])]
    
    while queue:
        current_state, path = queue.pop(0)
        
        if current_state in visited:
            continue
        
        visited.add(current_state)
        
        # Check if we've reached the goal
        if goal in current_state:
            actions = len(path)
            if current_state[0] == goal:
                return (actions, "one", current_state[1])
            else:
                return (actions, "two", current_state[0])
        
        # Generate next possible states
        next_states = [
            (bucket_one, current_state[1]),  # Fill bucket one
            (current_state[0], bucket_two),  # Fill bucket two
            (0, current_state[1]),  # Empty bucket one
            (current_state[0], 0),  # Empty bucket two
        ]
        
        # Pour from bucket one to bucket two
        amount = min(current_state[0], bucket_two - current_state[1])
        next_states.append((current_state[0] - amount, current_state[1] + amount))
        
        # Pour from bucket two to bucket one
        amount = min(current_state[1], bucket_one - current_state[0])
        next_states.append((current_state[0] + amount, current_state[1] - amount))
        
        for next_state in next_states:
            if next_state not in visited and not (next_state[0] == 0 and next_state[1] == other_bucket):
                queue.append((next_state, path + [next_state]))
    
    raise ValueError("Goal is not reachable")