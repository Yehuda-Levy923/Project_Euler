#function to check if a number is prime directly from Problem7.py
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

#function to check if a number is a circular prime meaning that if you rotate it however many times it will stay prime
def is_circular_prime(num):
    s = str(num)
    for _ in range(len(s)):
        if not is_prime(int(s)):
            return False
        s = s[1:] + s[0]
    return True

# Function that checks every number up until num if it is a circular prime
def find_all_circular_primes(num):
    all_circular_primes = []
    for i in range(num):
        if is_circular_prime(i):
            all_circular_primes.append(i)
    return all_circular_primes

if __name__ == '__main__':
    n = int(input("enter a number: ")) # Number we will find all the numbers below it that are circular prime and check how many
    print(len(find_all_circular_primes(n)),find_all_circular_primes(n)) # prints the amount of circular primes below n and a list of them