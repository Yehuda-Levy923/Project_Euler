#function to check if a number is prime, same as in Problem10
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

# Finds coefficients a and b such that the quadratic n^2 + an + b
# produces the longest sequence of consecutive primes starting from n = 0, under the given limits for a and b
def nums_that_satisfy_equation(limit_a, limit_b):
    longest_consecutives = 0
    best_a = 0
    best_b = 0
    if limit_a%2:
        limit_a += 1
    for a in range(-limit_a + 1, limit_a, 2):
        for b in (b for b in range(2, limit_b) if is_prime(b)):
            n = 0
            while is_prime(n**2 + a*n + b):
                n += 1
            if n > longest_consecutives:
                longest_consecutives = n
                best_a = a
                best_b = b

    return best_a, best_b, best_a*best_b

if __name__ == '__main__':
    n = int(input("enter 2 numbers: "))      # the number which we will find the product of the coefficients
    m = int(input())                         # of the 2 numbers under n that satisfy the equation
                                             # n^2 + an + b = the longest consecutive chain of primes
    print(nums_that_satisfy_equation(n, m))  # prints the coefficients product