# List of primes for the divisibility constraints (d2d3d4 % 2, d3d4d5 % 3, ..., d8d9d10 % 17)
PRIMES = [2, 3, 5, 7, 11, 13, 17]

# Recursively builds pandigital numbers satisfying the special divisibility rules
# pos: index in PRIMES list (starting from the end)
# suffix: current string of digits built so far (rightmost part of the number)
# used_digits: set of digits already used
def build_pandigital(pos, suffix, used_digits):
    if pos < 0:
        # All constraints satisfied — prepend the last unused digit
        for d in set("0123456789") - used_digits:
            yield d + suffix
        return

    # Try each unused digit in the current position
    for d in "0123456789":
        if d not in used_digits:
            # Check if the 3-digit number formed with this digit and the first two of suffix
            # is divisible by the current prime
            if int(d + suffix[:2]) % PRIMES[pos] == 0:
                yield from build_pandigital(pos - 1, d + suffix, used_digits | {d})

# Finds all valid pandigital numbers with the special divisibility property
# Starts from all possible last 3 digits divisible by 17, then recursively builds the rest of the number.
def find_valid_pandigitals():
    valid_numbers = []
    for n in range(17, 1000, 17):
        s = f"{n:03d}"
        if len(set(s)) == 3:  # Ensures digits are unique
            for num in build_pandigital(len(PRIMES) - 2, s, set(s)):
                valid_numbers.append(num)
    return valid_numbers

if __name__ == '__main__':
    total_sum = 0
    for number in find_valid_pandigitals():# Finding all 0–9 pandigital numbers with special divisibility properties
        print(number)           # Prints all the pandigital numbers with special divisibility properties
        total_sum += int(number)   # Sums all the pandigital numbers with special divisibility properties
    print("Sum:", total_sum)       # Prints the sum of all the pandigital numbers with special divisibility properties