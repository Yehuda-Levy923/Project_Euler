# Finds all square numbers until limit using the formula: P(n) = n * n inspiration form Problem42.py (Directly from Problem61.py)
def square_numbers(limit):
    all_square_numbers = set()
    for n in range(limit):
        all_square_numbers.add(n*n)
    return all_square_numbers

# Computes the periodic simple continued fraction of √D using the (m,d,a) recurrence
def cont_frac_period(n):
    a0 = int(n**0.5)
    if a0 * a0 == n:
        return a0, []
    A, m, d, a = [], 0, 1, 0
    first = True
    while a != 2 * a0:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        if not first:
            A.append(a)
        first = False
    return a0, A

# Builds all convergents recursively from the continued fraction coefficients A
def convergent(A, num, den, i, last):
    if i >= last:
        return num * A[i] + 1, A[i]
    numerator, denominator = convergent(A, den, A[i + 1], i + 1, last)
    return num * numerator + denominator, numerator

# Applies the parity rule:
#                           (x₁, y₁) = (hr−1, kr−1),   if r is even
#                           (x₁, y₁) = (h2r−1, k2r−1), if r is odd
def solve_pell(d):
    a0, A = cont_frac_period(d)
    L = len(A) - 1
    p, q = 1, 0
    if L > 0:
        if L % 2 == 0:
            p, q = convergent(A, a0, A[1], 1, L - 2)
        else:
            A += A[1:] * 2
            p, q = convergent(A, a0, A[1], 1, 2 * L - 1)
    return p, q

# Goes through all numbers below D (except squares) and returns the D with the largest fundamental x under a given bound
def check_all_pell_smaller_D(max_D):
    best = (0, 0, 0)
    all_squares = square_numbers(max_D)
    for d in range(2, max_D):
        if d in all_squares:
            continue
        x, y = solve_pell(d)
        if x > best[0]:
            best = x, y, d
    return best


if __name__ == "__main__":
    D = int(input("Enter the desired maximum D to solve for: ")) # Inputs maximum D that you want to find largest x
    print(f"Fundamental solution for D = {D}: ")    # Tells you what you input and what it's finding
    result = check_all_pell_smaller_D(D+1) # Stores results so there is no need to repeat calling the function
    print(f"x = {result[0]}"     # Prints the largest fundamental solution for x lower than the given D
          f"\ny = {result[1]}\n" # Prints the y for the largest fundamental solution for x lower than the given D
          f"D = {result[2]}")    # Prints the D for the largest fundamental solution for x lower than the given D