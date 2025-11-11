# Return a list of all prime numbers up to n (inclusive) using the Sieve of Eratosthenes algorithm (Taken directly from Problem37.py).
def sieve_of_eratosthenes(n):
    if n < 2:
        return []

    # Step 1: Assume all numbers are prime initially
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False

    # Step 2: Eliminate non-primes
    p = 2
    while p * p <= n:
        if is_prime[p]:
            # Mark all multiples of p as non-prime
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1

    # Step 3: Collect all primes
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

# Calculates how many ways you can add up to num using the values in sizes,
# by keeping track of smaller totals we've already figured out (Taken directly from Problem31.py).
def check_all_options(sizes, n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for size in sizes:
        for i in range(size, n + 1):
            dp[i] += dp[i - size]
    return dp[n]

# Finds the first number that can be written as the sum of primes in over n different ways
def check_first_more_than(n):
    for i in range(int(n)):
        if check_all_options([i for i in sieve_of_eratosthenes(i)], i) > n:
            return i
    return None

if __name__ == '__main__':
    num = int(input("Enter a number: ")) # Inputs the number we want to find the amount of ways to find it using summation of all numbers smaller
    print(check_first_more_than(num)) # Prints the amount of possible ways to get to num using all nums smaller and sum
