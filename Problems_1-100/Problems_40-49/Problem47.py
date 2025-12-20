# Function that returns a list where each index i contains the number of distinct prime factors of i.
def list_primality(n):
    result = [0] * (n + 1)
    for i in range(2, int(n) + 1):
        if result[i] == 0:
            for j in range(2 * i, len(result), i):
                result[j] += 1
    return result

# Finds the first number in a sequence of n consecutive integers where each integer has exactly n distinct prime factors.
def first_consecutive_same_primality(n):
    if n > 4:
        result = list_primality(1000000000)
    if n < 5:
        result = list_primality(250000)
    for i in range(2, len(result) - n):
        if all(result[i + j] == n for j in range(n)):
            return i

if __name__ == '__main__':
    num = int(input("Enter a number: "))         # Number which we will find a sequence of n consecutive
#>5 since higher will take too long to compute.  # Integers where each integer has exactly n distinct prime factors
    print(first_consecutive_same_primality(num)) # Prints the first number in the sequence found