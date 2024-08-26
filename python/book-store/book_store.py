from collections import Counter
from functools import lru_cache

def total(basket):
    if not basket:
        return 0
    
    prices = [0, 800, 1520, 2160, 2560, 3000]
    
    @lru_cache(maxsize=None)
    def find_min_price(counts):
        if not any(counts):
            return 0
        
        min_price = float('inf')
        n = len(counts)
        
        for group_size in range(1, min(6, n + 1)):
            new_counts = list(counts)
            for i in range(group_size):
                new_counts[i] -= 1
            new_counts = tuple(sorted((x for x in new_counts if x > 0), reverse=True))
            
            price = prices[group_size] + find_min_price(new_counts)
            min_price = min(min_price, price)
            
            # Consider splitting a group of 5 into 3 + 2
            if group_size == 5 and n >= 5:
                split_counts = list(counts)
                for i in range(3):
                    split_counts[i] -= 1
                for i in range(3, 5):
                    split_counts[i] -= 1
                split_counts = tuple(sorted((x for x in split_counts if x > 0), reverse=True))
                split_price = prices[3] + prices[2] + find_min_price(split_counts)
                min_price = min(min_price, split_price)
        
        return min_price
    
    book_counts = Counter(basket).values()
    counts = tuple(sorted(book_counts, reverse=True))
    return find_min_price(counts)