# ENTIRE CODE TAKEN FROM Problem31.py (took out the denominations and made it all the nums until n)
# Calculates how many ways you can add up to num using the values in sizes,
# by keeping track of smaller totals we've already figured out.
def check_all_options(sizes, num):
    dp = [0] * (num + 1)
    dp[0] = 1
    for size in sizes:
        for i in range(size, num + 1):
            dp[i] += dp[i - size]
    return dp[num]

if __name__ == '__main__':
    n = int(input("Enter a number: ")) # Inputs the number we want to find the amount of ways to find it using summation of all numbers smaller
    print(check_all_options([i for i in range(1, n)], n)) # Prints the amount of possible ways to get to num using all nums smaller and sum
