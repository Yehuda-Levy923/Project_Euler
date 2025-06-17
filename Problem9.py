import math
#function to check if its a pythagorean triplet
def pythagorean_triplet_checker(n, num1, num2):
    # check if sqrt(num1 ** 2 + num2 ** 2) is an integer
    if math.isqrt(num1 ** 2 + num2 ** 2) * math.isqrt(num1 ** 2 + num2 ** 2) == num1 ** 2 + num2 ** 2:
        return sum_is_n(n, num1, num2, math.isqrt(num1 ** 2 + num2 ** 2))
    return None
#checks if the sum of num1,num2,num3 is equal to n
def sum_is_n(num, num1, num2, num3):
    if num1 + num2 + num3 == num:
        return num1 * num2 * math.isqrt(num1 ** 2 + num2 ** 2)
    return None

if __name__ == '__main__':
    n = int(input("Enter a number: "))  #the number to see if its the sum of the triplet
    for a in range(1, n):
        for b in range(a + 1, n):  # ensure b > a to avoid duplicates
            if pythagorean_triplet_checker(n, a, b) is not None:
                print(a)
                print(b)
                print(pythagorean_triplet_checker(n, a, b))