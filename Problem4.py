def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    print(max(i * j for i in range(100, 1000) for j in range(i, 1000) if is_palindrome(i * j)))
