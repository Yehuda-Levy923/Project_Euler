# function that returns true if a number is a palindrome directly from Problem4.py
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# Checks if a number is a lychrel number by going 100 iterations and seeing if any are palindromes if not it is lychrel
def is_lychrel(num, counter = 0):
    if counter == 100:
        return True
    if is_palindrome(num + int(str(num)[::-1])):
        return False
    else:
        return is_lychrel(num + int(str(num)[::-1]), counter + 1)

# Counts how many lychrel numbers below the inputted num
def how_many_lychrel(num):
    amount_of_lychrel = 0
    for i in range(1, num + 1):
        if is_lychrel(i):
            amount_of_lychrel += 1

    return amount_of_lychrel

if __name__ == "__main__":
    n = int(input("Enter the upper limit for n: ")) # Inputs the number that you want to count the amount of lychrels below it
    print(how_many_lychrel(n)) # prints the amount of lychrels below n