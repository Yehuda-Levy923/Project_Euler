# read a lot of numbers from user input this function is almost identical to in Problem11
def alot_of_nums_input(length_of_numbers, amount_of_nums):
    new_bunch_of_nums = []
    print(f"Enter the a bunch of numbers values number by number ({amount_of_nums} values per number):")
    for i in range(length_of_numbers):
        while True:
            num_input = input().split()
            num = [int(value) for value in num_input]
            new_bunch_of_nums.append(num)
            break
    return new_bunch_of_nums
# extra note for function above: reads 'length_of_numbers' lines,
# each with 'amount_of_nums' space-separated integers stores them as a list of lists

#sums all the numbers inputted across all the sublists
def sum_all_nums(nums):
    total = 0
    for number_of_number in nums:
        total += sum(number_of_number)
    return total

if __name__ == '__main__':
    amount_of_number = int(input("Enter the amount numbers: "))  # inputs number of amount of numbers
    length_of_numbers = int(input("Enter the length of the numbers: "))  # inputs all the numbers length
    numbers = alot_of_nums_input(amount_of_number, length_of_numbers)  # input all the numbers
    print(sum_all_nums(numbers)) # reads multiple rows of numbers from the user, then prints their total sum