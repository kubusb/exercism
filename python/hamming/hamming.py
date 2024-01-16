def distance(strand_a, strand_b):
    hamming = 0
    position = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    if len(strand_a) == 0:
        return 0
    while position < len(strand_a):
        if strand_a[position] != strand_b[position]:
            hamming += 1
        position += 1
    return hamming
