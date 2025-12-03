# Function that finds the sum of the perimeters of all almost equilateral triangles using
# a recurrence relation derived from the properties of Pell's equation.
def sum_almost_equilateral_triangle_perimeters(limit):
    total_sum, a, b, m, perimeter = 0, 1, 1, 1, 0

    while perimeter <= limit:
        a, b, m, perimeter = b, 4 * b - a + 2 * m, -m, 3 * a - m
        if perimeter < 5 : continue # No such triangle with perimeter less than 5 that works
        if perimeter <= limit:
            total_sum += perimeter

    return total_sum


if __name__ == "__main__":
    n = int(input("Enter the maximum perimeter limit: "))  # Inputs the maximum perimeter limit
    print(sum_almost_equilateral_triangle_perimeters(n))  # Prints the total sum of perimeters