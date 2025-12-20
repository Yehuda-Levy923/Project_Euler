#function which makes fibonacci numbers until number
def generate_fibonacci(number):
    a, b = 1, 2
    while b < number:
        yield b
        a, b = b, a + b

if __name__ == '__main__':
    n = int(input("Enter a number: ")) #input a number for the threshold number
    print(sum([x for x in generate_fibonacci(n) if x % 2 == 0])) #prints the sum of all the even numbers in the
                                                                 #fibonacci sequence until the number you input