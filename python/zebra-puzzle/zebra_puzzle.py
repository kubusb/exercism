def solve_zebra_puzzle():
    houses = [
        {"color": "yellow", "nation": "Norwegian", "drink": "water", "hobby": "reading", "pet": "fox"},
        {"color": "blue", "nation": "Ukrainian", "drink": "tea", "hobby": "football", "pet": "horse"},
        {"color": "red", "nation": "Englishman", "drink": "milk", "hobby": "chess", "pet": "snails"},
        {"color": "ivory", "nation": "Spaniard", "drink": "orange juice", "hobby": "dancing", "pet": "dog"},
        {"color": "green", "nation": "Japanese", "drink": "coffee", "hobby": "painting", "pet": "zebra"}
    ]
    return houses

def drinks_water():
    houses = solve_zebra_puzzle()
    return next(house["nation"] for house in houses if house["drink"] == "water")

def owns_zebra():
    houses = solve_zebra_puzzle()
    return next(house["nation"] for house in houses if house["pet"] == "zebra")