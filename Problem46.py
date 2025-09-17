# Return a list of all prime numbers up to n (inclusive) using the Sieve of Eratosthenes algorithm. Directly from Problem37.py
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

# Checks if a number violates Goldbach's other conjecture
def is_goldbach_other_conjecture_false(n, primes):
    for p in primes:
        if p >= n:
            break
        remainder = n - p
        if remainder % 2 == 0:
            square = remainder // 2
            root = int(square**0.5)
            if root * root == square:
                return False
    return True

# Finds the smallest odd composite number that violates Goldbach's other conjecture
def find_goldbach_counterexample(limit):
    primes = sieve_of_eratosthenes(limit)
    prime_set = set(primes)

    for n in range(3, limit, 2):
        if n in prime_set:
            continue
        if is_goldbach_other_conjecture_false(n, primes):
            return n

if __name__ == '__main__':
    print(find_goldbach_counterexample(6000)) # Finds and prints the Counterexample for Goldbach's other conjecture