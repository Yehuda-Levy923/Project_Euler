def generate_fibonacci(number):
    a, b = 1, 2
    while b < number:
        yield b
        a, b = b, a + b

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print(sum([x for x in generate_fibonacci(n) if x % 2 == 0]))