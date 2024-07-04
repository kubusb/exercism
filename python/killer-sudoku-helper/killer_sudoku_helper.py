def combinations(target, size, exclude):
    def backtrack(start, current_sum, current_combination):
        if len(current_combination) == size:
            if current_sum == target:
                result.append(current_combination[:])
            return

        for num in range(start, 10):
            if num not in exclude and current_sum + num <= target:
                current_combination.append(num)
                backtrack(num + 1, current_sum + num, current_combination)
                current_combination.pop()

    result = []
    backtrack(1, 0, [])
    return sorted(result)
