# Function to find the greatest common denominator (Taken directly from Problem5.py)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Finds all reduced proper fractions with denominators <= d that fall between x and y
# For each denominator, determines the valid numerator range based on x and y bounds
# Only counts fractions where gcd(numerator, denominator) = 1 (reduced form)
def reduced_proper_fractions_between_x_and_y(d, x, y):
    count = 0
    for denom in range(2, d + 1):
        start = int(denom * x) + 1
        end = int(denom * y)
        if denom * y == end:
            end -= 1
        for num in range(start, end + 1):
            if gcd(num, denom) == 1:
                count += 1
    return count

if __name__ == "__main__":
    limit = int(input("Enter the limit of depth: "))                      # Choose the depth limit for the denominator
    lower = float(input("Enter the lower bound: "))                       # Inputs the lower bound we will check from
    upper = float(input("Enter the upper bound: "))                       # Inputs the upper bound we will check from
    print(reduced_proper_fractions_between_x_and_y(limit, lower, upper))  # Finds the amount of reduced proper fractions between
                                                                          # lower and upper bounds with the inputted depth