#function that converts a number (num1) into a list of a shifting window with the size window_size
def convert_num_to_list_of_chunks(num1, window_size):
    num_str = str(num1)
    return [int(num_str[i:i + window_size]) for i in range(len(num_str) - window_size + 1)]

#multiplies all the digits in a window by each other
def multiply_digits_in_chunks(windows):
    products = []
    for window in windows:
        product = 1
        for digit in str(window):
            product *= int(digit)
        products.append(product)
    return products

if __name__ == '__main__':
    n = int(input("Enter a number: "))  #the number we will split
    m = int(input("Enter window size: "))  #size of the window

    print(max(multiply_digits_in_chunks(convert_num_to_list_of_chunks(n, m))))  # printing the highest multiple of the digits of a window