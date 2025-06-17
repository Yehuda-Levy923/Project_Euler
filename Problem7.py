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

#function to find the Nth prime number
def nth_prime(num):
    if n == 1:
        return 2
    how_many = 1
    prime = 3
    while True:
        if is_prime(prime):
            how_many += 1
            if how_many == num:
                return prime
        prime += 2

if __name__ == '__main__':
    n = int(input("Enter a number: "))  #input the number that you want to check the n(your number)th prime
    print(nth_prime(n)) #printing the numbers prime