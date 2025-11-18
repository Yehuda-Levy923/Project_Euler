import random

# All the squares in monopoly
POSITIONS = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3',
             'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3',
             'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3',
             'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']

# Special squares (send you/get sent to closest)
CC_SPACES = [2, 17, 33]
CH_SPACES = [7, 22, 36]
RAILROADS = [5, 15, 25, 35]
UTILITIES = [12, 28]

# Drawing a community chest card finds where it sends you and how likely it will
def draw_community_chest(pos):
    card = random.randint(0, 15)
    if card == 0:
        return 0
    elif card == 1:
        return 10
    return pos

# Drawing a chance card finds where it sends you and how likely it will
def draw_chance(pos):
    card = random.randint(0, 15)
    if card == 0:
        return 0
    elif card == 1:
        return 10
    elif card == 2:
        return 11
    elif card == 3:
        return 24
    elif card == 4:
        return 39
    elif card == 5:
        return 5
    elif card in [6, 7]:
        return next((r for r in RAILROADS if r > pos), RAILROADS[0])
    elif card == 8:
        return next((u for u in UTILITIES if u > pos), UTILITIES[0])
    elif card == 9:
        new_pos = (pos - 3) % 40
        if new_pos in CC_SPACES:
            return draw_community_chest(new_pos)
        return new_pos
    return pos

# Simulates a turn a single dice roll (unless doubles) and returns where you end up
def simulate_turn(pos, n_sides):
    doubles = 0
    while True:
        die1 = random.randint(1, n_sides)
        die2 = random.randint(1, n_sides)

        if die1 == die2:
            doubles += 1
            if doubles == 3:
                return 10
        else:
            doubles = 0

        pos = (pos + die1 + die2) % 40

        if pos == 30:
            return 10

        if pos in CC_SPACES:
            pos = draw_community_chest(pos)

        if pos in CH_SPACES:
            pos = draw_chance(pos)

        if die1 != die2:
                break
    return pos

# Runs the game simulation (10000 turns) simulations amount of times with n_sided dice
def run_simulation(n_sides, simulations):
    visits = [0] * 40
    for _ in range(simulations):
        pos = 0
        for _ in range(10000):
            pos = simulate_turn(pos, n_sides)
            visits[pos] += 1
    return visits

# Calculates the likelihoods of landing on each square using what we found in teh simulations
def calculate_probabilities(visits):
    total = sum(visits)
    return [(POSITIONS[i], i, 100 * visits[i] / total) for i in range(40)]

# Prints the highest squares with the highest likelihoods and how likely they are
def print_top_positions(probabilities, top_n):
    sorted_probs = sorted(probabilities, key=lambda x: x[2], reverse=True)
    print("Top Most Likely Positions:")
    for i, (name, idx, prob) in enumerate(sorted_probs[:top_n], 1):
        print(f"{i:2}. {name:<6} (pos {idx:2}) - {prob:6.3f}%")

# Connects all the functions and runs it
def monopoly_probabilities(n_sides, simulations):
    visits = run_simulation(n_sides, simulations)
    probabilities = calculate_probabilities(visits)
    print_top_positions(probabilities,40)
    return probabilities


if __name__ == "__main__":
    amount_simulations = int(input("Enter the number of simulations: ")) # Inputs the number of simulations that you will simulate
    n = int(input("Enter how many sides for the dice: ")) # Inputs the number of sides for the dice
    monopoly_probabilities(n, amount_simulations) # Runs the program and outputs the list of all the squares and their likelihoods