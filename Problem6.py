def square_of_sum(num):
    total = sum(range(1, num + 1))
    return total ** 2

def sum_of_squares(num):
    return sum(i ** 2 for i in range(1, num + 1))

if __name__ == '__main__':
    print(square_of_sum(100) - sum_of_squares(100))
