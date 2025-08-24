#returns the length of a cycle using long division
def long_division(num):
    r, had, i = 1, {}, 0
    while True:
        if r == 0:
            return i
        if r in had:
            return i - had[r]
        had[r] = i
        r = (r % num) * 10
        i += 1

#finds the longest until variable until and returns it and the length
def find_longest(until):
    longest = 0
    number_with_longest = 0
    for i in range(1, until):
        current = long_division(i)
        if current > longest:
            longest = current
            number_with_longest = i
    return number_with_longest, long_division(number_with_longest)

if __name__ == '__main__':
    n = int(input("enter a number: "))  #The limit for which 1 divided by that number (1/n) has the longest repeating decimal cycle
    print(find_longest(n)) #prints the number + what the length of the cycle is