#function to check if a number is prime, same as in Problem10
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

from functools import reduce
def prime1(n):
    return list(range(2,n))==list((filter(lambda x:n % x!=0,(range(2,n)))))

def prime2(n):
    return reduce(lambda x,y:x if n%y!=0 else x+[y],range(2,n),[])==[]

def prime3(n):
    return not([x for x in range(2,n) if n%2==0])

print(prime1(9),prime2(9),prime3(9))
