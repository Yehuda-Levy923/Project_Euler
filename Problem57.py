# Function to find the greatest common denominator (Taken directly from Problem5.py)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function that converts decimals to fractions using numerator and denominator
def fraction_converter(num):
    numerator, denominator = num
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

# Finds the approximate sqrt of 2 to the requested depth using the equation:  1 + 1 / (2 + 1 / (2 + 1 / ...))
def approx_sqrt_2(depth):
    num, den = 3, 2
    if depth == 1:
        return num, den
    for _ in range(2, depth + 1):
        num, den = num + 2 * den, num + den
    return num, den

# Compares the length of 2 digits in a tuple (in this case numerator and denominator) and returns true if the first is longer
def comp_length(tup):
    return len(str(tup[0])) > len(str(tup[1]))

# Function that counts how many times the numerator has more digits than the denominator
def count_longer_numerators(num):
    count = 0
    for i in range(num + 1):
        if comp_length(fraction_converter(approx_sqrt_2(depth=i))):
            count += 1
    return count

if __name__ == "__main__":
    n = int(input("Enter the upper limit for n: ")) # Inputting the limit for depth we will calculate
    print(count_longer_numerators(n)) # Prints the amount of numbers which the numerator is larger than the denominator
                                      # for the equation: 1 + 1 / (2 + 1 / (2 + 1 / ...)) with n depth  runtime: O(n^2)

    print(int(((2*((n-1)-((n-1) % 13)))/13) + 1)) # Separate non-bruteforce way to solve the same problem runtime: O(1)