#function that inputs a number and outputs its factorial using iterative multiplication
#a copy from Problem15.py and Problem20.py
def factorial(num):
    factorial_equals = 1
    for i in range(1, num + 1):
        factorial_equals = factorial_equals * i
    return factorial_equals

#counts how many permutations exist for that length list
def how_many_permutations(list_of_digits):
    return factorial(len(list_of_digits))

# inputs a list of digits (not repeats) and a num it takes every number in the list and
# returns the `num`-th lexicographic permutation of distinct digits using
# the factorial number system: breaks permutation space into blocks
# of (n-1)!, (n-2)!, etc., to directly select digits without generating all permutations
def permutation_num_is(list_of_digits, num):
    result = []
    while list_of_digits:
        n = len(list_of_digits)
        f = factorial(n - 1)
        index = num // f
        num %= f
        result.append(list_of_digits.pop(index))
    return "".join(str(d) for d in result)

if __name__ == '__main__':
    l = list(input("Enter a list: ")) # the list of digits for permutation checking
    n = int(input("Enter a number: ")) # what number permutation you want in the lexicographic order
    print(int(permutation_num_is(l,n))) #prints the n-th permutation in lexicographic order on list l