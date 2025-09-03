# Return a list of all prime numbers up to n (inclusive) using the Sieve of Eratosthenes algorithm.
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

# Function that checks if a prime number is truncatable (both ways) via checking each direction's truncatability
def is_truncatable(prime, prime_set):
    prime_str = str(prime)
    for i in range(1, len(prime_str)):
        if int(prime_str[i:]) not in prime_set:
            return False
    for i in range(len(prime_str) - 1, 0, -1):
        if int(prime_str[:i]) not in prime_set:
            return False

    return True

# Finds all the truncatable primes by making a list of them all using the is_truncatable function
def find_all_truncatable():
    primes = sieve_of_eratosthenes(10**6)
    prime_set = set(primes)
    truncatables = [p for p in primes if p > 7 and is_truncatable(p, prime_set)]
    return truncatables


if __name__ == '__main__':
    print(find_all_truncatable(), "  Sum:", sum(find_all_truncatable())) # Prints all 11 dual-sided truncatable primes and their sum