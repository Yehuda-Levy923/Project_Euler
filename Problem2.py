def generate_fibonacci(number):
    a, b = 1, 2
    while b < number:
        yield b
        a, b = b, a + b

if __name__ == '__main__':
    print(sum([x for x in generate_fibonacci(4000000) if x % 2 == 0]))