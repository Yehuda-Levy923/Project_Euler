# Finds the last 10 digits of the given prime
def find_last_10_digits():
    return (28433 * 2**7830457 + 1) % 10**10


if __name__ == '__main__':
    print(find_last_10_digits()) # Prints the final 10 digits of the prime that was asked