# function that calculates 2^n
def calculate_2_pow_num(num):
    return 2**num
#function that calculates the sum of all the digits of a given number
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

if __name__ == '__main__':
    n = int(input("Enter a number: ")) # inputs value of n that we will add the digits of 2^n
    print(sum_of_digits(calculate_2_pow_num(n))) #prints the sum of all the digits of 2^n