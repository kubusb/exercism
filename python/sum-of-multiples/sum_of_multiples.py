def sum_of_multiples(limit, multiples):
    resulting_set = set()
    if multiples is None or len(multiples) == 0 or multiples == 0:
        return 0
    else:
        for multiple in multiples:
            if multiple == 0:
                continue
            current = multiple
            while current < limit:
                resulting_set.add(current)
                current = current + multiple
    return sum(resulting_set)
