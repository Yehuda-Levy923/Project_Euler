# Creates an n x n spiral matrix starting from the center and expanding outward in a clockwise direction.
# It fills the matrix with consecutive integers from 1 to n^2.
# After constructing the spiral, it reverses the matrix vertically and passes it to the diagonal sum function.
def generate_spiral(n):
    spiral = [[0] * n for _ in range(n)]
    x, y = n // 2, n // 2
    spiral[y][x] = 1
    num = 2
    step = 1

    while num <= n * n:
        for dx, dy in [(1,0),(0,-1),(-1,0),(0,1)]:
            for _ in range(step):
                x += dx
                y += dy
                if 0 <= x < n and 0 <= y < n:
                    spiral[y][x] = num
                    num += 1
            if (dx, dy) in [(0, -1), (0, 1)]: #increase step
                step += 1

    return calculates_diagonals_of_spiral(spiral[::-1], n)

# Calculates the sum of both diagonals in the spiral matrix.
# It subtracts 1 at the end to avoid double-counting the center value.
def calculates_diagonals_of_spiral(spiral, n):
    summation = 0
    for i in range(n):
        summation = spiral[i][i] + spiral[i][n-1-i] + summation
    return summation - 1

if __name__ == '__main__':
    m = int(input("enter a number: ")) # the number which we will find sum of the diagonal of a spiral of its size
    print(generate_spiral(m)) # prints the sum of the diagonal of the spiral

    #Direct equation I later found out
    n=(m-1)/2
    print(8*n*(n+1)*(2*n+1)/3 + 2*n*(8*n+1) + 4*n + 1)