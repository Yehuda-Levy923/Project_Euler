# Function that inputs a number and outputs its factorial using iterative multiplication.  Directly from Problem15.py
def factorial(num):
    factorial_equals = 1
    for i in range(1, num + 1):
        factorial_equals = factorial_equals * i
    return factorial_equals

# Function that gets n and chooses r of them uses the equation: n!/r!(n-r)!
def n_choose_r(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

# Function that finds how many n_choose_r > k for every possible r (n>r)
def find_amount(n,k):
    counter = 0
    for i in range(1, n + 1):
        for r in range(1, i+1):
            if n_choose_r(i, r) > k:
                counter += 1
    return counter

if __name__ == '__main__':
    num1 = int(input("Enter the upper limit for n: ")) # Inputs the number that you want to be the limit
    num2 = int(input("Enter the threshold value k: ")) # Inputs the number that you want to be the threshold
    print(find_amount(num1,num2))