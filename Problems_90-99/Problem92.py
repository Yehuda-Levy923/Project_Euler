# ENTIRE SOLUTION IS INSPIRED BY THE SOLUTION FOR Problem.74

# Function that inputs a number and outputs its square
def square(num):
    return num ** 2

# Calculates the sum of the digits^2 of num
def sum_of_digit_squares(num):
    total = 0
    for digit in str(num):
        total += square(int(digit))
    return total

# Checks the last number of the chain of sum of squares that follows num
def end_of_chain(num):
    if num == 0:
        return 0
    while num != 1 and num != 89:
        num = sum_of_digit_squares(num)
    return num

# Finds all chains ending in target_end starting up until limit
def find_chain_ending_in(target_end, limit):
    all_chains = []
    for i in range(limit):
        last = end_of_chain(i)
        if last == target_end:
            all_chains.append((i, last))
    return all_chains


if __name__ == "__main__":
    n = int(input("Enter the last number of chain you want: "))  # Inputs the final number of the chain of squares
    lim = int(input("Enter the highest number you want to check: "))  # Inputs the highest number that we will check its chians
    chains = find_chain_ending_in(n, lim + 1)  # ~Halves the computing time by saving the chains instead of calculating them for the output and length
    print(chains, "\n", len(chains))  # Prints all the chains end in num that start lower than lim and how many there are