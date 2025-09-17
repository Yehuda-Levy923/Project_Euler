# Finds all pentagonal numbers until n using the formula: P(n) = n(3n−1)/2 inspiration form Problem42.py
def pentagonal_numbers(limit):
    all_pentagonal_numbers = set()
    for n in range(limit):
        all_pentagonal_numbers.add(n*(3*n - 1)//2)
    return all_pentagonal_numbers

# Finds all hexagonal numbers until n using the formula: H(n) = n(2n−1) inspiration form Problem42.py
# All triangular numbers are hexagonal so this finds them too
def hexagonal_numbers(limit):
    all_hexagonal_numbers = set()
    for n in range(limit):
        all_hexagonal_numbers.add(n*(2*n - 1))
    return all_hexagonal_numbers

# Finds numbers that are both pentagonal and hexagonal
def find_common_pentagonal_hexagonal(n):
    pent_set = pentagonal_numbers(n)
    hex_set = hexagonal_numbers(n)
    common_numbers = sorted(pent_set.intersection(hex_set))
    return common_numbers

if __name__ == '__main__':
    for number in find_common_pentagonal_hexagonal(35000):
        print(number) # Prints all the pentagonal & hexagonal numbers below the limit