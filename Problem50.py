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

# Finds longest string of consecutive primes that adds up to a prime below num
def find_longest_sequence(num):
    primes = sieve_of_eratosthenes(num)
    set_primes = set(primes)
    cumulative_sum = [0]
    for p in primes:
        cumulative_sum.append(cumulative_sum[-1] + p)
    max_length, max_prime = 0, 0
    for i in range(len(primes)):
        for j in range(i + max_length, len(primes)):
            total = cumulative_sum[j] - cumulative_sum[i]
            if total > num:
                break
            if total in set_primes:
                max_length = j - i
                max_prime = total
    return max_prime, max_length

if __name__ == '__main__':
    num = int(input("Enter a number: "))  # Inputs the number that you want to find the longest sequence of consecutive
                                          # primes that sum to a prime smaller than num
    print(find_longest_sequence(num)) # Prints prime it sums to and the length of the prime sequence