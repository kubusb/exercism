def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    
    max_value = target + 1
    dp = [max_value] * (target + 1)
    dp[0] = 0
    coin_used = [[] for _ in range(target + 1)]

    for i in range(1, target + 1):
        for coin in coins:
            if coin <= i:
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    coin_used[i] = coin_used[i - coin] + [coin]

    if dp[target] == max_value:
        raise ValueError("can't make target with given coins")

    return sorted(coin_used[target])
