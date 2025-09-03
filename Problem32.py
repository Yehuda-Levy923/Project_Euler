# Turns a number into its digits
def digits_of_number(n):
    return [int(d) for d in str(n)]

# Function that detects if the given number is pan-digital (uses all digits 1 to num exactly once)
def pandigital_digits_detector(digits, num):
    expected = set(range(1, num + 1))
    return 0 not in digits and set(digits) == expected and len(digits) == num

# Finds all the factors of a given number
def all_factor_finder(num):
    pairs = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            j = num // i
            pairs.append((i, j))
    return pairs

# Pairs numbers with their factors and makes sure it's pan-digital
def paired_and_checker(num):
    matches = []
    products_seen = set()
    upper_limit = 10000

    for product in range(1, upper_limit):
        for a, b in all_factor_finder(product):
            digits = digits_of_number(a) + digits_of_number(b) + digits_of_number(product)
            if pandigital_digits_detector(digits, num):
                if product not in products_seen:
                    matches.append([[a, b], product])
                    products_seen.add(product)
    return summer(matches)

# Flattens a nested list
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# Sums only the products from the matches
def summer(all_pan_digital_numbers_including_divs):
    products = [match[1] for match in all_pan_digital_numbers_including_divs]
    return sum(products)

if __name__ == '__main__':
   n = int(input("Enter a number: ")) # Input to the number we will check the sum of all the pan-digital numbers of 1 to the input
   print(paired_and_checker(n))