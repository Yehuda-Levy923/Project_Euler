def convert_num_to_list_of_chunks(num1, chunk_size):
    num_str = str(num1)
    return [int(num_str[i:i + chunk_size]) for i in range(len(num_str) - chunk_size + 1)]

def multiply_digits_in_chunks(portions):
    products = []
    for portion in portions:
        product = 1
        for digit in str(portion):
            product *= int(digit)
        products.append(product)
    return max(products)

if __name__ == '__main__':
    n = int(input("Enter a large number: "))
    m = int(input("Enter chunk size: "))

    print(multiply_digits_in_chunks(convert_num_to_list_of_chunks(n, m)))