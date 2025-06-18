#function that inputs a number and outputs its factorial using iterative multiplication a copy from Problem15.py
def factorial(num):
    factorial_equals = 1
    for i in range(1, num + 1):
        factorial_equals = factorial_equals * i
    return factorial_equals

#function that calculates the sum of all the digits of a given number a copy from Problem16.py
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

if __name__ == "__main__":
    n = int(input("Enter a number: ")) #input the number you want to calculate the sum of it factorial
    print(sum_of_digits(factorial(n))) #prints the sum of the digits of n!