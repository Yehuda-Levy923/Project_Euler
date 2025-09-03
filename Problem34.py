# Calculates factorial using a for loop
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Calculates the sum of the digits of num
def sum_of_digit_factorials(num):
    total = 0
    for digit in str(num):
        total += factorial(int(digit))
    return total

# Checks if it's a curious number by comparing the number to the sum of its digits factorial (each one separately)
def is_curious_number(num):
    return num == sum_of_digit_factorials(num)

# Calculates the sum of all curious numbers (with an upper limit of 100000)
def sum_of_all_curious_numbers():
    summation = 0
    for i in range(10, 100000):
        if is_curious_number(i):
            summation += i
    return summation


if __name__ == '__main__':
    print(sum_of_all_curious_numbers()) # Prints the sum of all numbers which the sum of the numbers digits factorial
                                        # (each one separately) is equal to itself