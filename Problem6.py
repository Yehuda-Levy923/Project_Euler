#function that calculates the square of the sum of all the numbers smaller and equal to a number
def square_of_sums(num):
    total = sum(range(1, num + 1))
    return total ** 2

#function that calculates the sum of the square of all the numbers smaller and equal to a number
def sum_of_squares(num):
    return sum(i ** 2 for i in range(1, num + 1))

if __name__ == '__main__':
    n = int(input("Enter a number: ")) #input the number you want to find the difference between the squares of sums and the reverse
    print(str(square_of_sums(n)) + ' - ' + str(sum_of_squares(n)) + ' = ' + str(square_of_sums(n) - sum_of_squares(n)))#printing the results
