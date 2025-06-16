def square_of_sums(num):
    total = sum(range(1, num + 1))
    return total ** 2

def sum_of_squares(num):
    return sum(i ** 2 for i in range(1, num + 1))

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print(str(square_of_sums(n)) + ' - ' + str(sum_of_squares(n)) + ' = ' + str(square_of_sums(n) - sum_of_squares(n)))
