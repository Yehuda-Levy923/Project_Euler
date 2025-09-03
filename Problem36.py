# Converting base 10 to base 2
def converter(num):
    return bin(num)[2:]

# function that returns true if a number is a palindrome taken from Problem4.py
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# Function that returns true if a number is a palindrome and the base 2 version of the same number is a palindrome
def is_base_10_and_2_palindrome(num):
    return is_palindrome(num) and is_palindrome(converter(num))

# Finds all double palindromes smaller than num and sums them up
def sum_finder_for_double_palindromes(num):
    all_double_palindromes = []
    for i in range(1,num,2):
        if is_base_10_and_2_palindrome(i):
            all_double_palindromes.append(i)
    return sum(all_double_palindromes)


if __name__ == '__main__':
    n = int(input("enter a number: ")) # The number which we will find all the double palindromes lower than it and sum them
    print(sum_finder_for_double_palindromes(n)) # Prints the sum of all double palindromes lower than n