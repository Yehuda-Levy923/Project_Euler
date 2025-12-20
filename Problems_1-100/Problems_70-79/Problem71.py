# Function to find the greatest common denominator (Taken directly from Problem5.py)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Finds the fraction directly to the left of the target_n / target_d with the depth limit of num
def find_directly_to_left(num, target_n, target_d):
    best_n, best_d = 0, 1
    for d in range(1, num + 1):
        n = (target_n * d - 1) // target_d
        if gcd(n, d) == 1:
            if n * best_d > best_n * d:
                best_n, best_d = n, d
    return best_n, best_d

if __name__ == "__main__":
    limit = int(input("Enter the limit of depth: "))               # Choose the deph limit for the numerator and denominator
    numerator = int(input("Enter the numerator target: "))         # Inputs which numerator to check directly to teh left of
    denominator = int(input("Enter the denominator target: "))     # Inputs which denominator to check directly to teh left of
    print(find_directly_to_left(limit + 1, numerator, denominator))# Prints the numerator and denominator of the to the left
                                                                   # of the requested fraction within the asked for depth limit