from functools import reduce
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def smallest_evenly_divisible(num):
    return reduce(lambda a, b: a * b // gcd(a, b), range(1, num + 1))

if __name__ == '__main__':
    print(smallest_evenly_divisible(20))