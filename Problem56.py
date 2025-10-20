# Function that sums all the digits from the number a ^ b
def find_sum_of_a_pow_b(a,b):
    return sum([int(i) for i in list(str(a**b))])

# Function that finds the largest sum of all the digits of a ^ b where a and b are limits (it checks all numbers lower than a, b)
def find_largest_sum_of_a_pow_b(a, b):
    all_a_pow_b = []
    for i in range(a):
        for j in range(b):
            all_a_pow_b.append(find_sum_of_a_pow_b(i, j))

    return max(all_a_pow_b)

if __name__ == '__main__':
    base = int(input("Enter the limit for a: ")) # Inputs the limit that you want to be for the base
    exponent = int(input("Enter the limit for b: ")) # Inputs the limit that you want to be for the exponent
    print(find_largest_sum_of_a_pow_b(base, exponent)) # Prints the largest sum for the number that is base^exponent limited