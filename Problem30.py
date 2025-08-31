# Calculates the sum of the fifth powers of each digit in a number
def splitting_num_and_calc_5th_pow(num):
    return sum(int(digit)**5 for digit in str(num))

# Checks if a number is equal to the sum of the fifth powers of its digits
def comparing_og_to_sum_5th_pow(num):
    if num == splitting_num_and_calc_5th_pow(num):
        print(num)
    return num == splitting_num_and_calc_5th_pow(num)

# Sums all numbers that are equal to the sum of the fifth powers of their digits
def sum_of_all_5th_pow_equal_og():
    return sum(i for i in range(2, 6*9**5) if comparing_og_to_sum_5th_pow(i))

if __name__ == '__main__':
    print("sum: " + str(sum_of_all_5th_pow_equal_og()))