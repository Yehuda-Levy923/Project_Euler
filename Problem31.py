# Calculates how many ways you can add up to num using the values in sizes,
# by keeping track of smaller totals we've already figured out
def check_all_options(sizes, num):
    dp = [0] * (num + 1)
    dp[0] = 1
    for size in sizes:
        for i in range(size, num + 1):
            dp[i] += dp[i - size]
    return dp[num]

if __name__ == '__main__':
    arr = list(input("Enter a list of all denominations: ")) # Inputs all the denominations for finding the final number
    n = int(input("Enter a number: ")) # Inputs the number we want to find the amount of ways to find it using summation of all denominations
    print(check_all_options([1,2,5,10,20,50,100,200], 200)) # Prints the amount of possible ways to get to num using denominations and sum
