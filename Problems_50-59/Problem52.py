# I learnt in a calculus class that n/7 (n>7) is the same digits repeated so when I saw the question I knew the answer immediately
# The same idea works for: 1/17, 1/19, 1/23, 1/29, 1/47, 1/59, 1/61 ...
# Here is a python solution with a limit that can be changed (now it's 10^6 which will be fast and work for the question)
# Finds a number that 1*num has the same digits as 2*num ... n*num
def find_the_number(n):
    for i in range(1, 10**6):
        digits = set(str(i))
        if all(set(str(i * j)) == digits for j in range(2, n + 1)):
            return i

if __name__ == '__main__':
    num = int(input("Enter a number: "))  # Inputs the number that you want to find the first number that 1*num has the same digits as 2*num ... n*num
    print(find_the_number(num)) # Prints the number that is the smallest of the num in teh sequence