# Flattens a nested list (Directly from Problem32.py)
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# Filters out all roots that are rational
def all_irrational_roots(n):
    all_irrational_roots_under_n = []
    for i in range(1, n+1):
        if i**0.5 % 1 != 0:
            all_irrational_roots_under_n.append(i)
    return all_irrational_roots_under_n

# Function that finds the square root of x to the digits-th depth
def sqrt_digits(x, digits):
    scale = 10 ** (2 * digits)
    n = x * scale
    guess = n//2
    while True:
        new_guess = (guess + n // guess) // 2
        if new_guess == guess:
            break
        guess = new_guess
    result = str(guess)
    integer_part = result[:-digits] if len(result) > digits else "0"
    decimal_part = result[-digits:].rjust(digits, "0")
    return list(integer_part + decimal_part)

# Sums all the digits in the lists of lists (of irrational square roots)
def find_sum_of_all(n, depth):
    all_sqrt = []
    for i in all_irrational_roots(n):
        all_sqrt.append(sqrt_digits(i, depth))
    return sum([int(i) for i in flatten(all_sqrt)])


if __name__ == "__main__":
    max_num = int(input("Enter max number you want to go until: ")) # Inputs the highest number we go until for the sum
    depth = int(input("Enter the depth you want: ")) # Inputs the amount of digits
    print(find_sum_of_all(max_num, depth-1)) # Prints the sum of all the digits in all the numbers (depth-1 because of the number before the decimal)