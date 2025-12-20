# Generates generalized pentagonal numbers in the order 1,-1,2,-2,...
def pentagonal_numbers(limit):
    k = 1
    while True:
        g1 = k * (3*k - 1) // 2
        g2 = k * (3*k + 1) // 2
        if g1 > limit:
            break
        yield g1
        if g2 <= limit:
            yield g2
        k += 1

# Calculates p(n) using Euler's recurrence, based on smaller totals we've already figured out
def partition_number(n, p, divisor):
    total = 0
    k = 1
    while True:
        g1 = k * (3*k - 1) // 2
        g2 = k * (3*k + 1) // 2
        if g1 > n:
            break
        sign = -1 if (k % 2 == 0) else 1
        total += sign * p[n - g1]
        if g2 <= n:
            total += sign * p[n - g2]
        k += 1
    return total % divisor

# Finds the first n such that p(n) is divisible by divisor
def first_divisible_by(divisor):
    p, n = [1], 1
    while True:
        val = partition_number(n, p, divisor)
        p.append(val)
        if val == 0:
            return n
        n += 1


if __name__ == '__main__':
    n = int(input("Enter a number: ")) # Inputs n, and it will be the divisor we check against.
    print(first_divisible_by(n))       # Find and print the first integer i such that the number of partitions of
                                       # i using all smaller positive integers is divisible by n.




