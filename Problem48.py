# Function that returns a list of all the numbers to the power of themselves until n
def power_finder(n):
    return [i**i for i in range(1,n)]

# Function that returns the sum of the list of all the numbers to the power of themselves until n
def total_sum(n):
    return sum(power_finder(n + 1)) - 1

# Function that cuts the number to the last ten digits and returns it
def cut_and_return_result(n):
    return int(str(total_sum(n))[len(str(total_sum(n)))-10:])

if __name__ == '__main__':
    num = int(input("Enter a number: ")) # Inputs the number that you want to find all the powers num**num under it
    print(cut_and_return_result(num)) # Prints the last 10 digits of the sum of all the 'num**num's