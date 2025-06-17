#function that calculates the largest prime number that num is divisible by
def largest_prime_factor(num):
        factor = 2
        while factor * factor <= num:
            if num % factor == 0:
                num //= factor
            else:
                factor += 1
        return num
if __name__ == '__main__':
    n = int(input("Enter a number: ")) #input a number for the search of the largest prime factor
    print(largest_prime_factor(n)) #prints the largest prime factor of the inputted number