points = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 0,
    'Y': 3,
    'Z': 6
}

rules = {
    ('A', 'X'): 'C',
    ('A', 'Y'): 'A',
    ('A', 'Z'): 'B',
    ('B', 'X'): 'A',
    ('B', 'Y'): 'B',
    ('B', 'Z'): 'C',
    ('C', 'X'): 'B',
    ('C', 'Y'): 'C',
    ('C', 'Z'): 'A',
}

with open('i.txt') as input:
    input = input.read()
    rounds = [(round.split(" ")[0], round.split(" ")[1]) for round in input.split('\n')]
    total_points = 0
    for round in rounds:
        shape = rules[round]
        outcome = round[1]
        total_points += points[outcome] + points[shape]

print(total_points)