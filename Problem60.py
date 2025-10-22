# Return a list of all prime numbers up to n (inclusive) using the Sieve of Eratosthenes algorithm. (Directly from Problem37.py)
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

# Function to check if a number is prime. (Directly from Problem7.py)
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

# Function that checks that a concatenated b and b concatenated a are both prime
def concatenated_prime_check(a, b):
    return is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))

# Uses backtracking to save time by pruning invalid sets
def backtrack(current, start, primes, size):
    if len(current) == size:
        return current
    for i in range(start, len(primes)):
        p = primes[i]

        if all(concatenated_prime_check(p, q) for q in current):
            result = backtrack(current + [p], i + 1, primes, size)
            if result:
                return result
    return None

# Finds the set I want by putting all the above functions together
def find_prime_sets(size):
    limit = 10000
    primes = sieve_of_eratosthenes(limit)
    return backtrack([], 0, primes, size)


if __name__ == '__main__':
    amount = int(input("Enter the amount of primes: ")) # Inputs the amount that you want to be for the primes
    the_list = find_prime_sets(amount) # Halves the computing time by saving the list and not checking it twice
    print(the_list, sum(the_list)) # Prints the list followed by the sum of the amount of number you want