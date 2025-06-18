#function that finds the prime factors of any given number
def prime_factors(n):
    i = 2
    factors = {}
    while i * i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = 1
    return factors
# extra note for function above: uses trial division the exponents are stored in a dictionary

#function which uses the exponents of the prime factors to find the amount of factors
def count_divisors_via_factors(n):
    factors = prime_factors(n)
    count = 1
    for exp in factors.values():
        count *= (exp + 1)
    return count
# extra note for function above: it multiplies (exponent + 1) for each prime factor to get total divisors

# function that checks the first triangle number
# (addition of all number until a certain number (10 = 1+2+3+4)) that has a minimum divisors of min_divisors
def first_triangle_with_divisors(min_divisors):
    n = 1
    triangle = 1
    while True:
        triangle_factors = prime_factors(triangle)
        divisors = 1
        for exp in triangle_factors.values():
            divisors *= (exp + 1)
        if divisors >= min_divisors:
            return triangle
        n += 1
        triangle += n
# extra note for function above: builds triangle numbers incrementally stops at first with enough divisors

if __name__ == '__main__':
    num = int(input("Enter a number: "))  # smallest number with the input as the amount of divisors
    print(first_triangle_with_divisors(num)) # checks the smallest number with num divisors and prints it