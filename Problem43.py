# Recursively generates all permutations of a given sequence
def permutations(seq):
    if len(seq) == 0:
        return [[]]
    result = []
    for i in range(len(seq)):
        elem = seq[i]
        rest = seq[:i] + seq[i + 1:]
        for p in permutations(rest):
            result.append([elem] + p)
    return result

# Each function checks divisibility of a specific 3-digit slice of the digit list
def divisible_by_17(d): return int(''.join(d[7:10])) % 17 == 0
def divisible_by_13(d): return int(''.join(d[6:9])) % 13 == 0
def divisible_by_11(d): return int(''.join(d[5:8])) % 11 == 0
def divisible_by_7(d):  return int(''.join(d[4:7])) % 7 == 0
def divisible_by_5(d):  return int(''.join(d[3:6])) % 5 == 0
def divisible_by_3(d):  return int(''.join(d[2:5])) % 3 == 0
def divisible_by_2(d):  return int(''.join(d[1:4])) % 2 == 0

# Checks if a permutation satisfies all the divisibility rules
def is_valid_pandigital(digits):
    return (
        divisible_by_17(digits) and
        divisible_by_13(digits) and
        divisible_by_11(digits) and
        divisible_by_7(digits) and
        divisible_by_5(digits) and
        divisible_by_3(digits) and
        divisible_by_2(digits)
    )

# Finds all 0–9 pandigital numbers that satisfy the divisibility rules
def find_valid_pandigitals():
    valid = []
    for p in permutations('0123456789'):
        if p[5] not in ('0', '5'):
            continue
        if is_valid_pandigital(p):
            valid.append(''.join(p))
    return valid

if __name__ == '__main__':
    summer = 0
    for number in find_valid_pandigitals():# Finding all 0–9 pandigital numbers with special divisibility properties
        print(number)           # Prints all the pandigital numbers with special divisibility properties
        summer += int(number)   # Sums all the pandigital numbers with special divisibility properties
    print("Sum:", summer)       # prints the sum of all the pandigital numbers with special divisibility properties