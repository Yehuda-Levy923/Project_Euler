# Generate all factor combinations of target starting from 'start' and accumulating in current_factors
def find_factors(target, start, current_factors):
    if target == 1:
        if len(current_factors) > 1:
            yield current_factors
        return
    for i in range(start, target + 1):
        if target % i == 0:
            yield from find_factors(target // i, i, current_factors + [i])

# Finds all the minimal product-sum numbers for 2 ≤ k ≤ limit and returns their unique values as a set.
def minimal_product_sum_numbers(limit):
    minimal = {k: float('inf') for k in range(2, limit + 1)}
    for n in range(2, (limit * 2) + 1):
        for factors in find_factors(n, 2, []):
            sum_factors = sum(factors)
            ones = n - sum_factors
            k = len(factors) + ones
            if 2 <= k <= limit and n < minimal[k]:
                minimal[k] = n
    return set(minimal.values())

if __name__ == '__main__':
    num = int(input("Enter a number: "))  # Inputs the maximum k to find minimal product-sum numbers for
    print((minimal_product_sum_numbers(num)))  # Prints the sum of all the minimal product-sum numbers for 2 ≤ k ≤ 12000