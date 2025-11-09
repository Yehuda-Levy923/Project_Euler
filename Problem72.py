# Function to find the greatest common denominator (Taken directly from Problem5.py)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Finds all the fraction that are reduced proper fractions where the denominator is smaller than d.
# Using Euler's totient function: phi(n) = (p1^a1 - p1^(a1-1)) * (p2^a2 - p2^(a2-1)) *...* (pk^ak - pk^(ak-1))
# Then we sum all the phi's from phi(2) ... phi(n)
def reduced_proper_fractions(d):
    phi = list(range(d + 1))
    for i in range(2, d + 1):
        if phi[i] == i:
            for j in range(i, d + 1, i):
                phi[j] -= phi[j] // i

    return sum(phi[2:])

if __name__ == "__main__":
    limit = int(input("Enter the limit of depth: ")) # Choose the deph limit for the numerator and denominator
    print(reduced_proper_fractions(limit))           # Finds the amount of reduced proper fractions when the limit of
                                                     # the denominator and numerator is the input