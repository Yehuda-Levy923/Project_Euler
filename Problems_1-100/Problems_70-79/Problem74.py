# Function that inputs a number and outputs its factorial using iterative multiplication (Taken directly from Problem15.py)
def factorial(num):
    factorial_equals = 1
    for i in range(1, num + 1):
        factorial_equals = factorial_equals * i
    return factorial_equals

# Calculates the sum of the digits of num (Taken directly from Problem34.py)
def sum_of_digit_factorials(num):
    total = 0
    for digit in str(num):
        total += factorial(int(digit))
    return total

# Checks the length of the chain of sum of factorials that follows num
def length_of_chain(num):
    chain_length = 0
    chain = [num]
    while True:
        nxt_num = sum_of_digit_factorials(chain[chain_length])
        if nxt_num in chain:
            return chain_length + 1
        chain.append(nxt_num)
        chain_length += 1

# Finds chains longer than num up until limit
def find_chain_longer_than(num, limit):
    all_chain_longer_than_num = []
    for i in range(limit):
        new_len_chain= length_of_chain(i)
        if new_len_chain >= num:
            all_chain_longer_than_num.append((i, new_len_chain))
    return all_chain_longer_than_num


if __name__ == "__main__":
    n = int(input("Enter the length of chain you want: "))         # Input the number for the minimum length of the chain that you want
    lim = int(input("Enter the highest number you want to check:"))# Input the highest number to check its chain length
    chains = find_chain_longer_than(n, lim) # ~Halves the computing time by saving the chains instead of calculating them for the output and length
    print(chains,"\n", len(chains)) # Prints all the chains longer than num that start lower than lim and how many there are