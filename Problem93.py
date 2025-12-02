# Generate all permutations of a list
def permutations(lst):
    if len(lst) == 0:
        return [[]]
    result = []
    for i in range(len(lst)):
        rest = lst[:i] + lst[i+1:]
        for p in permutations(rest):
            result.append([lst[i]] + p)
    return result

# Generate all combinations of length r from a list
def combinations(lst, r, start=0):
    if r == 0:
        return [[]]
    result = []
    for i in range(start, len(lst)):
        for c in combinations(lst, r-1, i+1):
            result.append([lst[i]] + c)
    return result

# Apply an operation
def apply_op(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            return None
    return None

# Recursively combine numbers
def all_results(nums):
    if len(nums) == 1:
        yield nums[0]
        return
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                a, b = nums[i], nums[j]
                rest = [nums[k] for k in range(len(nums)) if k != i and k != j]
                for op in ['+', '-', '*', '/']:
                    res = apply_op(a, b, op)
                    if res is not None:
                        yield from all_results(rest + [res])

# Generate all integer results for a set of digits
def generate_integers(digits):
    results = set()
    for perm in permutations(digits):
        for val in all_results(list(perm)):
            if val > 0 and abs(val - round(val)) < 1e-9:  # integer check
                results.add(int(round(val)))
    return results

# Find longest consecutive run starting from 1
def longest_run(digits):
    results = generate_integers(digits)
    n = 1
    while n in results:
        n += 1
    return n - 1

# Search over all sets of 4 distinct digits (1–9)
def find_final_answer():
    best_set, best_run = None, 0
    for digits in combinations(list(range(1, 10)), 4):
        run = longest_run(digits)
        if run > best_run:
            best_run = run
            best_set = digits

    return ''.join(map(str,best_set)), best_run


if __name__ == "__main__":
    final_answers = find_final_answer() # ~Halves computing time by storing best set and best run instead of recalculating
    print(final_answers[0],"\n", final_answers[1])  # Outputs the best set of digits and the length of the longest run