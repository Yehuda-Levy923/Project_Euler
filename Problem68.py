# Generates permutations for all the numbers in the list `arr` with length `r`.
def generate_permutations(arr, r):
    if r == 0:
        return [[]]
    result = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for perm in generate_permutations(rest, r-1):
            result.append([arr[i]] + perm)
    return result

# Builds the n-gon "lines" as triples: (external node, internal node, next internal node).
def build_lines(external, internal, n):
    return [(external[i], internal[i], internal[(i+1) % n]) for i in range(n)]

# Checks if all line sums are equal (magic property).
def is_magic(lines):
    sums = [sum(line) for line in lines]
    return len(set(sums)) == 1

# Concatenates all numbers in the lines into one string for comparison.
def build_string(lines):
    return "".join("".join(map(str, line)) for line in lines)

# It searches all possible arrangements of numbers 1..2n into external and internal nodes,
# checks which configurations form a valid magic n-gon (all line sums equal),
# and returns the largest concatenated string representation of such a solution.
def solve_magic_ngon(n):
    numbers = list(range(1, 2*n + 1))
    max_string = ""

    for external in generate_permutations(numbers, n):
        if min(external) != external[0]:
            continue

        internal = [num for num in numbers if num not in external]

        for perm in generate_permutations(internal, n):
            lines = build_lines(external, perm, n)
            if is_magic(lines):
                s = build_string(lines)
                if n == 5 and len(s) != 16:
                    continue
                if s > max_string:
                    max_string = s
    return max_string

if __name__ == "__main__":
    n = int(input("Enter the number for n= in the n-gon:")) # Inputs the number that you want to check the maximum 
                                                            # concatenated number for a solution to n-gon.
    print((solve_magic_ngon(n)))                            # Prints the largest concatenated n-gon solution