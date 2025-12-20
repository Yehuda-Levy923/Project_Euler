#function which makes fibonacci numbers until num.  Taken from Problem2.py with a slight change
def generate_fibonacci():
    a, b = 1, 2
    while True:
        yield b
        a, b = b, a + b

# checks for the smallest fibonacci number that is longer or equal to num digits long
def check_length(num):
    i = 0
    for fib in generate_fibonacci():
        i += 1
        if len(str(fib)) > num:
            return i + 2, fib

if __name__ == '__main__':
    n = int(input("enter a number: ")) #the number which you want to see the fibonacci number
    print(check_length(n - 1)) #prints the number + what index it has that has a length larger or equal to n