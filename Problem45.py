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


pent_set = pentagonal_numbers(10000000)
hex_set = hexagonal_numbers(10000000)

for i in hex_set:
    if i in pent_set:
        print(i)