from math import log
# Function that will get inputs of numbers separated by commas and return them as a list of lists (Inspired by Problem89.py)
def read_number_input_as_lists():
    print("Enter lines of numbers separated by commas (one per line). Press Enter twice to finish:\n")
    return [list(map(int, line.strip().split(','))) for line in iter(input, '') if line.strip()]

# Function that compares the 2 lines inputted to be exponents and returns the larger onne using the clever trick:
# If exponent1 * ln(base1) > exponent2 * ln(base2) then base1^exponent1 < base2^exponent2 and vise versa
def compare_2_exponents(lst1, lst2):
    if lst1[1] * log(lst1[0]) > lst2[1] * log(lst2[0]):
        return lst1
    return lst2

# Finds the largest of all the exponents by using the compare on all the pairs inputted and counts what line it's on
def find_largest_exponent(lst_of_lsts):
    line_number = 1
    largest_exponent_line_number = 1
    largest_exponent = lst_of_lsts[0]
    for lst in lst_of_lsts:
        if compare_2_exponents(lst, largest_exponent) == lst:
            largest_exponent = lst
            largest_exponent_line_number = line_number
        line_number += 1
    return largest_exponent, largest_exponent_line_number


if __name__ == "__main__":
    all_nums = read_number_input_as_lists() # Inputs all the bases,exponents on different rows
    print(find_largest_exponent(all_nums))  # Prints the highest valued pair + the line number