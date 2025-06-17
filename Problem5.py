from functools import reduce
#function to find the greatest common denominator
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#returns the smallest number that is evenly divisible by all numbers from 1 to num
def smallest_evenly_divisible(num):
    return reduce(                          # uses reduce to iteratively apply the LCM function across the range 1 to num
        lambda a, b: a * b // gcd(a, b),    # (Least Common Multiple) LCM(a, b) is calculated using the formula: (a * b) // gcd(a, b)
        range(1, num + 1)                   # generate numbers from 1 to num inclusive
    )

if __name__ == '__main__':
    n = int(input("Enter a number: "))#input the number you want to check 1 through its smallest evenly divisible
    print(smallest_evenly_divisible(n))#printing the smallest number evenly divisible by 1 through n