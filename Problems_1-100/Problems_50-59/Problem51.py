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

# Gets a number and the placements in it to swap and swaps them our for the same number repeated
def digit_replacer(num, digit_place_lst):
    num_str = list(str(num))
    new_num_lst = []
    for i in range(10):
        temp = num_str[:]
        for j in digit_place_lst:
            temp[j] = str(i)
        new_num_lst.append(int("".join(temp)))
    return new_num_lst

# Finds the amount of primes there are with digit replacements
def find_primes_with_dig_rep(num):
    if num == 9:
        primes = sieve_of_eratosthenes(10**8)
    else:
        primes = sieve_of_eratosthenes(10**6)
    primes_set = set(primes)
    for prime in primes:
        str_prime = str(prime)
        for digit in set(str_prime):
            positions = [i for i in range(len(str_prime)) if str_prime[i] == digit]
            if len(positions) < 2:
                continue
            candidates = digit_replacer(prime, positions)
            prime_family = [p for p in candidates if p in primes_set and len(str(p)) == len(str_prime)]

            if len(prime_family) >= num:
                return prime_family

if __name__ == '__main__':
    n = int(input("Enter a number: ")) # Inputs the number that you want to find the
                                       # smallest prime that masking it also makes n primes
    print(str(find_primes_with_dig_rep(n)[0]) +
          "\n" + str(find_primes_with_dig_rep(n))) # Prints prime followed by all the primes in the family