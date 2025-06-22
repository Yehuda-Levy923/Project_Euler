#function that finds the factors of any given number, inspiration taken from Problem12 / function taken from Problem21
def regular_factors(n):
    factors = {1}
    for i in range(2, int(n**0.5) + 1): # only go up to square root to avoid repeats
        if n % i == 0:
            factors.add(i)
            if i != n // i:  # avoid adding the square root twice (in perfect squares)
                factors.add(n // i)
    return factors

# checks if a number is abundant (sum of divisors > number)
def check_if_its_abundant(num):
    return sum(regular_factors(num)) > num

# calculates sum of all numbers <= num that are NOT the sum of two abundant numbers
def all_numbers_not_sum_of_two_abundent_numbers_summer(num):
    abundant_numbers = [i for i in range(1, num + 1) if check_if_its_abundant(i)]# get all abundant numbers up to num
    abundant_sums = set()  # will store all possible sums of two abundant numbers
    # double loop to find all possible sums of two abundant numbers
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            abundant_sum = abundant_numbers[i] + abundant_numbers[j]
            if abundant_sum <= num:
                abundant_sums.add(abundant_sum)

    # sum all numbers from 1 to num that are not in the abundant_sums set
    total_sum = sum(i for i in range(1, num + 1) if i not in abundant_sums)
    return total_sum

if __name__ == '__main__':
    n = int(input("Enter a number: ")) #input a number for calculating the sum of all deficient (numbers that the sum of all its divisors are smaller than it) numbers until it
    print(all_numbers_not_sum_of_two_abundent_numbers_summer(n)) #prints the sum of all the deficient numbers until n