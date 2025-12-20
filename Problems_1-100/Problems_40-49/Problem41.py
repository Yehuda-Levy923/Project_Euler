#function to check if a number is prime directly from Problem7.py
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

# Function to generate permutations of a string
def generate_permutations(s):
    if len(s) <= 1:
        yield s
    else:
        for i in range(len(s)):
            for perm in generate_permutations(s[:i] + s[i+1:]):
                yield s[i] + perm

# Function to find the largest pandigital prime
def find_largest_pandigital_prime(number):
    for n in range(number, 0, -1):
        for p in sorted(generate_permutations('123456789'[:n]), reverse=True):
            num = int(''.join(p))
            if is_prime(num):
                return num

if __name__ == '__main__':
    n = int(input("Enter a number: "))     # The number length for finding the highest pandigital prime
    print(find_largest_pandigital_prime(n)) # Print the highest prime pandigital at length of n