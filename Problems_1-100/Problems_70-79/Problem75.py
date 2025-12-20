# Function to find the greatest common denominator (Taken directly from Problem5.py)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function that finds all pythagorean triplets that all the numbers are below limit
def pythagorean_triplets_euclid_formula(limit):
    triplets = []
    m = 2
    while m * m <= limit:
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:
                a = m*m - n*n
                b = 2*m*n
                c = m*m + n*n
                if c > limit:
                    break
                k = 1
                while k * c <= limit:
                    triplets.append((k*a, k*b, k*c))
                    k += 1
        m += 1
    return triplets

# Finds all the sums of pythagorean triplets that appear once meaning that they are numbers which exactly one integer sided right angle triangle can be formed be formed
def all_sums_of_triplets_that_appear_once(num):
    all_triplets = pythagorean_triplets_euclid_formula(num // 2)
    all_triplets_sums = []
    for triplet in all_triplets:
        s = sum(triplet)
        if s <= num:
            all_triplets_sums.append(s)

    counts = {}
    for s in all_triplets_sums:
        counts[s] = counts.get(s, 0) + 1

    return [s for s in all_triplets_sums if counts[s] == 1]


if __name__ == "__main__":
    n = int(input("Enter the limit sum to check: ")) # Enters the limit for the sum of the 3 numbers (a,b,c pythagorean)
    all_sums = all_sums_of_triplets_that_appear_once(n) # ~Halves the computing time by saving the chains instead of calculating them for the output and length
    print(all_sums,"\n", len(all_sums)) # Prints all the sums that don't repeat and how many there are