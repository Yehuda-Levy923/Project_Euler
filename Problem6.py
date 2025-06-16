def square_of_sum(num):
    total = sum(range(1, num + 1))
    return total ** 2

def sum_of_squares(num):
    return sum(i ** 2 for i in range(1, num + 1))

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print(square_of_sum(n) - sum_of_squares(n))
