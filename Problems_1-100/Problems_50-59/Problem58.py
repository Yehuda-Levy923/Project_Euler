# Return a list of all prime numbers up to n (inclusive) using the Sieve of Eratosthenes algorithm (Directly from Problem37.py)
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

# Function that checks if a number is prime (similar to Problem7.py)
def is_prime(n, primes):
    if n < 2:
        return False
    r = int(n**0.5)
    for p in primes:
        if p > r:
            break
        if n % p == 0:
            return False
    return True

# Function that finds the side length of the square spiral for which
# the ratio of primes along both diagonals first falls below a given threshold (ratio)
def spiral_prime_ratio(ratio):
    side_length = 1
    prime_count = 0
    total_diagonals = 1

    primes = sieve_of_eratosthenes(30000)

    while True:
        side_length += 2
        corners = [
            side_length**2,
            side_length**2 - (side_length - 1),
            side_length**2 - 2*(side_length - 1),
            side_length**2 - 3*(side_length - 1),
        ]
        prime_count += sum(1 for c in corners if is_prime(c, primes))
        total_diagonals += 4

        if prime_count / total_diagonals < ratio:
            return side_length

if __name__ == "__main__":
    r = float(input("Enter the percent threshold: ")) # Inputs the precent threshold you want to use
    print(spiral_prime_ratio(r/100)) # Outputs the side length of the square spiral where prime ratio along diagonals first falls below threshold