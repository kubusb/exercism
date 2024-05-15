from collections import Counter

def rank_to_value(rank):
    if rank in "23456789":
        return int(rank)
    elif rank in ['T', '10']:
        return 10
    elif rank == 'J':
        return 11
    elif rank == 'Q':
        return 12
    elif rank == 'K':
        return 13
    elif rank == 'A':
        return 14
    else:
        return None

def hand_rank(hand):
    ranks = sorted([rank_to_value(card[0]) if card[0] != '1' else rank_to_value(card[:2]) for card in hand], reverse=True)
    suits = [card[1] if card[0] != '1' else card[2] for card in hand]
    rank_counts = Counter(ranks)
    is_flush = len(set(suits)) == 1
    is_straight = all(ranks[i] - 1 == ranks[i + 1] for i in range(4))
    
    if is_straight and is_flush:
        return (8, ranks)
    if 4 in rank_counts.values():
        return (7, [rank for rank, count in rank_counts.items() if count == 4] + [rank for rank, count in rank_counts.items() if count != 4])
    if 3 in rank_counts.values() and 2 in rank_counts.values():
        return (6, [rank for rank, count in rank_counts.items() if count == 3] + [rank for rank, count in rank_counts.items() if count == 2])
    if is_flush:
        return (5, ranks)
    if is_straight:
        return (4, ranks)
    if 3 in rank_counts.values():
        return (3, [rank for rank, count in rank_counts.items() if count == 3] + sorted([rank for rank, count in rank_counts.items() if count != 3], reverse=True))
    if list(rank_counts.values()).count(2) == 2:
        return (2, sorted([rank for rank, count in rank_counts.items() if count == 2], reverse=True) + [rank for rank, count in rank_counts.items() if count == 1])
    if 2 in rank_counts.values():
        return (1, [rank for rank, count in rank_counts.items() if count == 2] + sorted([rank for rank, count in rank_counts.items() if count == 1], reverse=True))
    return (0, ranks)

def best_hands(hands):
    parsed_hands = [[(card[:-1], card[-1]) for card in hand.split()] for hand in hands]
    ranked_hands = [(hand, hand_rank(hand)) for hand in parsed_hands]
    best_rank = max(rank for hand, rank in ranked_hands)
    best_hands = [hand for hand, rank in ranked_hands if rank == best_rank]
    return [' '.join(card[0] + card[1] for card in hand) for hand in best_hands]
