# Finds all triangle numbers until limit using the equation: T(n) = n(n+1)/2 (Directly from Problem42.py)
def triangle_numbers(limit):
    all_triangle_numbers = set()
    for n in range(limit):
        all_triangle_numbers.add((n**2+n)//2)
    return all_triangle_numbers

# Finds all square numbers until limit using the formula: P(n) = n * n inspiration form Problem42.py
def square_numbers(limit):
    all_square_numbers = set()
    for n in range(limit):
        all_square_numbers.add(n*n)
    return all_square_numbers

# Finds all pentagonal numbers until limit using the formula: P(n) = n(3n−1)/2 inspiration form Problem42.py
def pentagonal_numbers(limit):
    all_pentagonal_numbers = set()
    for n in range(limit):
        all_pentagonal_numbers.add(n*(3*n - 1)//2)
    return all_pentagonal_numbers

# Finds all hexagonal numbers until limit using the formula: H(n) = n(2n−1) inspiration form Problem42.py
def hexagonal_numbers(limit):
    all_hexagonal_numbers = set()
    for n in range(limit):
        all_hexagonal_numbers.add(n*(2*n - 1))
    return all_hexagonal_numbers

# Finds all heptagonal numbers until limit using the formula: H(n) = n(5n-3)/2 inspiration form Problem42.py
def heptagonal_numbers(limit):
    all_heptagonal_numbers = set()
    for n in range(limit):
        all_heptagonal_numbers.add(n*(5*n-3)//2)
    return all_heptagonal_numbers

# Finds all octagonal numbers until limit using the formula: H(n) = n(3n-2) inspiration form Problem42.py
def octagonal_numbers(limit):
    all_octagonal_numbers = set()
    for n in range(limit):
        all_octagonal_numbers.add(n*(3*n-2))
    return all_octagonal_numbers

# Checks if a list is cyclic at the given length
def check_if_cyclic(cyclic_list, cycle_length):
    for i in range(0, cycle_length):
        mid1 = len(cyclic_list[i])
        left1, right1 = str(cyclic_list)[:mid1], str(cyclic_list)[mid1:]
        if i == cyclic_list - 1:
            mid2 = len(cyclic_list[0])
            left2, right2 = str(cyclic_list)[:mid2], str(cyclic_list)[mid2:]
        else:
            mid2 = len(cyclic_list[i+1])
            left2, right2 = str(cyclic_list)[:mid2], str(cyclic_list)[mid2:]

        if right1 == left2:
            continue

        if i == cycle_length-1:
            if right2 == left1:
                return True
    return False

# Builds all the types of numbers (triangle, square, etc.) (up to limit) into a list and returns that
def build_sets(limit):
    return   [  triangle_numbers  (limit),
                square_numbers    (limit),
                pentagonal_numbers(limit),
                hexagonal_numbers (limit),
                heptagonal_numbers(limit),
                octagonal_numbers (limit),  ]

# Recursively builds a path across sets, matching numbers by overlapping digits
def search(path, used_sets, sets, digits):
    if len(path) == len(sets):
        return path if str(path[-1])[-digits:] == str(path[0])[:digits] else None

    suffix = str(path[-1])[-digits:]
    for i, s in enumerate(sets):
        if i in used_sets:
            continue
        for num in s:
            if str(num)[:digits] == suffix:
                result = search(path + [num], used_sets | {i}, sets, digits)
                if result:
                    return result
    return None

# Finds a repeating cycle by checking which numbers in the sets fall within the valid range
def find_cycle(limit, digits, min_val, max_val):
    sets = [{n for n in s if min_val <= n < max_val} for s in build_sets(limit)]
    for i, s in enumerate(sets):
        for num in s:
            result = search([num], {i}, sets, digits)
            if result:
                return result
    return None


if __name__ == '__main__':
    digs = int(input("Enter the amount of digits you want: ")) # Inputs the amount of digits that you want to check for
    min_value = int(input("Enter the min value check: ")) # Inputs the minimum value that you want to check for
    max_value = int(input("Enter the max value check: ")) # Inputs the maximum value that you want to check for
    the_list = find_cycle(200, digs, min_value, max_value) # Halves the computing time by saving the list and not checking it twice
    print(the_list, sum(the_list)) # Prints the list followed by the sum of the amount of number you want