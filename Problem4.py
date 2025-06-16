def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    max_pal, f = (
        max(((i * j, (i, j)) for i in range(10 ** (n - 1), 10 ** n) for j in range(i, 10 ** n) if is_palindrome(i * j)),
        key=lambda x: x[0]))
    print(f[0], f[1], max_pal)