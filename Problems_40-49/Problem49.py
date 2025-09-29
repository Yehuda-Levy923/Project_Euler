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

# Checks if the list is 3 numbers that are permutations of each other (same digits different order)
def permutations_checker(lst):
    s = [sorted(str(x)) for x in lst]
    return s[0] == s[1] == s[2]

# Function to find the 3 primes that are permutations of each other nad are 4 digits long and an arithmatic sequence
def find_the_3_primes():
    all_triplets = []
    primes = [p for p in sieve_of_eratosthenes(9999) if p >= 1000]
    prime_set = set(primes)
    for p in primes:
        for q in primes:
            if q > p:
                r = q + (q - p)
                if r in prime_set:
                    triplet = [p, q, r]
                    if permutations_checker(triplet):
                        all_triplets.append(triplet)
    return all_triplets

# Concatenates the 3 terms
def concatenate(lst):
    return int(''.join(map(str, lst)))

if __name__ == '__main__':
    for triplet in find_the_3_primes():
        print(concatenate(triplet)) # Prints all concatenated sequences of 3 permutation primes 4 digits long