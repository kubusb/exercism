def maximum_value(maximum_weight, items):
    n = len(items)
    # Create a 1D table to store the maximum values
    dp = [0 for _ in range(maximum_weight + 1)]
    
    # Build the table bottom-up
    for i in range(n):
        for w in range(maximum_weight, items[i]["weight"] - 1, -1):
            dp[w] = max(dp[w], dp[w - items[i]["weight"]] + items[i]["value"])
    
    return dp[maximum_weight]