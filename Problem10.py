#function to check if a number is prime
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

#function that add all primes smaller than num
def add_all_primes(num):
    sum_of_primes = 0
    for i in range(1,num):
        if is_prime(i):
            sum_of_primes = sum_of_primes + i
    return sum_of_primes


if __name__ == '__main__':
    n = int(input("Enter a number: "))  # the number we get to add all primes until it
    print(add_all_primes(n)) #printing the sum of all primes smaller than n
