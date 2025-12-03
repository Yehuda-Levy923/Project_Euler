# Function to find the greatest common denominator (Taken directly from Problem5.py)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Counts all right-angled triangles in an n×n grid by summing those with right angles
# 1. At the origin. 2. On the axes. 3. At interior points using vector steps.
def count_right_angled_triangles(limit):
    count = limit * limit + 2 * limit * limit
    for x in range(1, limit + 1):
        for y in range(1, limit + 1):
            g = gcd(x, y)
            dx = y // g
            dy = -x // g

            steps_pos = min((limit - x) // dx, y // -dy)
            steps_neg = min(x // dx, (limit - y) // -dy)

            count += steps_pos + steps_neg
    return count


if __name__ == "__main__":
    n = int(input("Enter a number: ")) # Inputs the maximum number for x and y to be
    print(count_right_angled_triangles(n)) # Prints how many right-angled triangles can be on integer valued x,y in the grid of nXn