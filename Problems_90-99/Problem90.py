# Finds all the perfect squares below n.
def all_squares(n):
    squares = set()
    i = 1
    while i * i < n:
        squares.add(i * i)
        i += 1
    return squares

# Checks if ALL required perfect squares (1, ..., 81) can be formed by combining a digit from C1 and a digit from C2, in either order.
def check_if_represents_all_corrected(C1, C2):
    required_squares = all_squares(100)
    squares_formed = set()

    C1_extended = set(C1)
    C2_extended = set(C2)
    if 6 in C1:
        C1_extended.add(9)
    if 9 in C1:
        C1_extended.add(6)
    if 6 in C2:
        C2_extended.add(9)
    if 9 in C2:
        C2_extended.add(6)

    for d1 in C1_extended:
        for d2 in C2_extended:
            n1 = d1 * 10 + d2
            if n1 in required_squares:
                squares_formed.add(n1)

            n2 = d2 * 10 + d1
            if n2 in required_squares:
                squares_formed.add(n2)

    return squares_formed == required_squares

# Generates all combinations of six distinct digits from 0 to 9.
def generate_six_digit_combinations():
    digits = list(range(10))
    all_combinations = []
    for i in range(1 << 10):
        current_combination = []
        if bin(i).count('1') == 6:
            for j in range(10):
                if i & (1 << j):
                    current_combination.append(digits[j])
            all_combinations.append(set(current_combination))
    return all_combinations

# Finds all valid pairs of cubes that can represent all required perfect squares.
def find_valid_pairs():
    combinations = generate_six_digit_combinations()
    valid_pair_count = 0

    for i in range(len(combinations)):
        for j in range(i, len(combinations)):
            C1 = combinations[i]
            C2 = combinations[j]
            if check_if_represents_all_corrected(C1, C2):
                valid_pair_count += 1

    return valid_pair_count

if __name__ == "__main__":
    print("Total valid pairs on cubes:", find_valid_pairs()) # Print the total valid pairs on cubes: 1217
