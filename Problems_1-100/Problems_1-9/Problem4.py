# function that returns true if a number is a palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]

if __name__ == '__main__':
    n = int(input("Enter a number: ")) #input the length you want
    max_pal, f = max(
        (
            (i * j, (i, j))                         # store product and the pair (i, j)
            for i in range(10 ** (n - 1), 10 ** n)  # i goes from smallest n-digit number to largest
            for j in range(i, 10 ** n)              # j starts from i to avoid duplicates
            if is_palindrome(i * j)                 # only keep products that are palindromes
        ),
        key=lambda x: x[0]                          # choose the pair with the largest product
    )

    print(f[0], f[1], max_pal)  # print the two numbers and their palindrome product