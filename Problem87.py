# Return a list of all prime numbers up to n (inclusive) using the Sieve of Eratosthenes algorithm (Directly from Problem37.py).
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

# Function that finds all numbers <= n that can be expressed as: prime^2 + prime^3 + prime^4
def nums_that_are_primes_square_plus_cube_plus_fourth_power(n):
    primes_square = sieve_of_eratosthenes(int(n ** 0.5))
    primes_cube =   sieve_of_eratosthenes(int(n ** (1/3)))
    primes_fourth = sieve_of_eratosthenes(int(n ** 0.25))
    results = set()
    for i in primes_square:
        i2 = i * i
        if i2 > n: break
        for j in primes_cube:
            j3 = j * j * j
            if i2 + j3 > n: break
            for k in primes_fourth:
                k4 = k ** 4
                m = i2 + j3 + k4
                if m <= n:
                    results.add(m)
    return results


if __name__ == "__main__":
    num = int(input("Enter a number: "))  # Input the upper bound n that we will find how many nums are the sum: prime^2 + prime^3 + prime^4
    result = nums_that_are_primes_square_plus_cube_plus_fourth_power(num) # ~Halves the computing time by saving the result instead of calculating them for the output and length
    print(result, "\n", len(result))  # Prints all such numbers exist up to n and how many there are
