def largest_prime_factor(num):
        factor = 2
        while factor * factor <= num:
            if num % factor == 0:
                num //= factor
            else:
                factor += 1
        return num
if __name__ == '__main__':
    print(largest_prime_factor(600851475143))