# Function that builds a string of concatenated numbers starting from 0 until the string length reaches 'num'
def str_of_all_numbers(num):
    i = 0
    string = ''
    while len(string) < num:
        string = string + str(i)
        i += 1
    return string

# Function that finds the product of digits at positions n, n*m, n*m^2, ... in the concatenated number string
# It starts with n = 1 and multiplies the digit at each position until n >= num
def product_finder(num, m):
    n = 1
    product = 1
    string = str_of_all_numbers(num)
    while n < num:
        product *= int(string[n])
        n *= m
    return product

if __name__ == '__main__':
    n = int(input("Enter a number: "))  # Length of the concatenated string
    m = int(input("Enter a number: "))  # Multiplier for index positions
    print(product_finder(n, m))         # Prints the product of selected digits