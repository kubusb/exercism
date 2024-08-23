from typing import List, Tuple, Optional

def can_chain(dominoes: List[Tuple[int, int]]) -> Optional[List[Tuple[int, int]]]:
    if not dominoes:
        return []
    
    def build_chain(chain: List[Tuple[int, int]], remaining: List[Tuple[int, int]]) -> Optional[List[Tuple[int, int]]]:
        if not remaining:
            return chain if chain[0][0] == chain[-1][1] else None
        
        for i, domino in enumerate(remaining):
            if not chain or domino[0] == chain[-1][1]:
                new_chain = chain + [domino]
                result = build_chain(new_chain, remaining[:i] + remaining[i+1:])
                if result:
                    return result
            if not chain or domino[1] == chain[-1][1]:
                new_chain = chain + [(domino[1], domino[0])]  # Reverse the domino
                result = build_chain(new_chain, remaining[:i] + remaining[i+1:])
                if result:
                    return result
        
        return None

    # Try starting with each domino
    for i, start_domino in enumerate(dominoes):
        result = build_chain([start_domino], dominoes[:i] + dominoes[i+1:])
        if result:
            return result
        # Try with reversed start domino
        result = build_chain([(start_domino[1], start_domino[0])], dominoes[:i] + dominoes[i+1:])
        if result:
            return result

    return None