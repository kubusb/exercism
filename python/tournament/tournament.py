from collections import defaultdict

def tally(rows):
    # Initialize a defaultdict to store team statistics
    teams = defaultdict(lambda: {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0})
    
    # Process each match result
    for row in rows:
        team1, team2, result = row.strip().split(';')
        
        teams[team1]['MP'] += 1
        teams[team2]['MP'] += 1
        
        if result == 'win':
            teams[team1]['W'] += 1
            teams[team1]['P'] += 3
            teams[team2]['L'] += 1
        elif result == 'loss':
            teams[team2]['W'] += 1
            teams[team2]['P'] += 3
            teams[team1]['L'] += 1
        elif result == 'draw':
            teams[team1]['D'] += 1
            teams[team2]['D'] += 1
            teams[team1]['P'] += 1
            teams[team2]['P'] += 1
    
    # Sort teams by points (descending) and then alphabetically
    sorted_teams = sorted(teams.items(), key=lambda x: (-x[1]['P'], x[0]))
    
    # Prepare the output
    output = ["Team                           | MP |  W |  D |  L |  P"]
    for team, stats in sorted_teams:
        row = f"{team:<30} | {stats['MP']:>2} | {stats['W']:>2} | {stats['D']:>2} | {stats['L']:>2} | {stats['P']:>2}"
        output.append(row)
    
    return output

# Example usage:
input_data = [
    "Allegoric Alaskans;Blithering Badgers;win",
    "Devastating Donkeys;Courageous Californians;draw",
    "Devastating Donkeys;Allegoric Alaskans;win",
    "Courageous Californians;Blithering Badgers;loss",
    "Blithering Badgers;Devastating Donkeys;loss",
    "Allegoric Alaskans;Courageous Californians;win"
]

result = tally(input_data)
for line in result:
    print(line)
