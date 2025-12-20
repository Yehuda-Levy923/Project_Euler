# Generates a list of pentagonal numbers using the formula: P(n) = n(3n−1)/2
def pentagon_numbers(limit):
    return [(n * (3 * n - 1)) // 2 for n in range(1, limit)]

# Checks if a number is in the precomputed set of pentagonal numbers
def is_pentagonal(x, pent_set):
    return x in pent_set

# Checks if the sum of two numbers is a pentagonal number
def checks_for_addition(num1, num2, pent_set):
    return is_pentagonal(num1 + num2, pent_set)

# Checks if the absolute difference of two numbers is a pentagonal number
def checks_for_subtraction(num1, num2, pent_set):
    return is_pentagonal(abs(num1 - num2), pent_set)

# Finds the smallest pair of pentagonal numbers whose sum and difference are also pentagonal
def find_smallest_pentagon_pair():
    pent_list = pentagon_numbers(2400)     # Precompute a list of pentagonal numbers
    pent_set = set(pent_list)              # Convert to set for fast membership checks
    min_diff = None                        # Tracks the smallest difference found
    final_result = None                    # Stores the matching pair

    for i in range(len(pent_list)):
        for j in range(i + 1, len(pent_list)):  # Avoid duplicate and reversed pairs
            pi = pent_list[i]
            pj = pent_list[j]
            if checks_for_addition(pi, pj, pent_set) and checks_for_subtraction(pi, pj, pent_set):
                diff = abs(pj - pi)
                if min_diff is None or diff < min_diff:
                    min_diff = diff              # Update smallest difference
                    final_result = (pi, pj)      # Store the pair with desired property
    return final_result, min_diff

if __name__ == '__main__':
    result = find_smallest_pentagon_pair() # Finds the first valid pentagonal pair and the difference
    print(result)  # Prints the first pair of pentagonal numbers with the special property and their difference