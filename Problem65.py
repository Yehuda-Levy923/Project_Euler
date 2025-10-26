# Function that calculates the sum of all the digits of a given number (Directly from Problem16.py)
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

# Finds the approximation of e to the requested depth using the equation:  1 + 1 / (1 + 1 / (2*k + 1 / ...))
def approx_e(depth):
    terms = [2]
    k = 1
    while len(terms) < depth:
        terms.extend([1, 2 * k, 1])
        k += 1
    terms = terms[:depth]

    num, den = 1, terms[-1]
    for term in reversed(terms[1:-1]):
        num, den = den, term * den + num

    numerator = terms[0] * den + num
    return sum_of_digits(numerator)


if __name__ == '__main__':
    n = int(input("Enter the depth: "))  # Inputs the depth that you want to check until for e
    print(approx_e(n)) # Prints the sum of the digits of the numerator for the approximation of e to the nth depth