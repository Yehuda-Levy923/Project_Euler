# Checks if a list is pan-digital to num inspiration from Problem32.py
def is_pandigital(s):
    return sorted(s) == list('123456789')

# Builds a concatenated product of num with (1,2,3...) until the string reaches 9 digits
# Returns the 9-digit string if it's exactly 9 digits long, otherwise returns None
def find_the_concatenated_product(num):
    concatenated_product = ''
    i = 1
    while len(concatenated_product) < 9:
        concatenated_product += str(num * i)
        i += 1
    return concatenated_product if len(concatenated_product) == 9 else None

# Iterates through 4-digit numbers (due to Some simple reasoning tells us that we are looking for 4-digit number times 1 and 2.
# A 3-digit number starting with 9 would produce 7 or 11 digits, and a 2-digit number starting with 9 would produce 8 or 11 digits.
# So a 4-digit number it is, and since we are only concerned with the max.)
# to find all whose concatenated products are 1-9 pandigital, returns a list of all such valid pandigital concatenated products
def find_all_pandigital_concatenated_products():
    all_pandigital_concatenated_products = []
    for i in range(1000, 10000):
        concatenated_product = find_the_concatenated_product(i)
        if concatenated_product and is_pandigital(concatenated_product):
            all_pandigital_concatenated_products.append(concatenated_product)
    return all_pandigital_concatenated_products

# Finds the largest 1-9 pandigital number formed as a concatenated product of an integer, starts from the given pandigital
# number (we get in the question that number meaning the answer must be higher) and updates if a larger one is found.
def find_largest_pandigital_concatenated_product():
    largest = 918272645
    for i in find_all_pandigital_concatenated_products():
        if int(i) > largest:
            largest = int(i)
    return largest

# Prints the largest pandigital concatenated product found
print(find_largest_pandigital_concatenated_product())