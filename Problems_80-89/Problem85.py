# Function that finds the rectangle with the closest amount of sub-rectangles to target and returns the dimensions of the rectangle
# its area and how many sub-rectangles it has.   Uses the equation for a 2D grid: [N*(N+1)//2] * [M*(M+1)//2]
def find_the_best_rect(target):
    min_diff, best_area, best_n, best_m, best_num_rects = target, 0, 0, 0, 0
    for n in range(1, int((2 * target)**0.5) + 1):
        triangle_num_n = n * (n + 1) // 2

        if triangle_num_n * (1 * (1 + 1) // 2) > target + min_diff:
            break

        for m in range(n + 1):
            triangle_num_m = m * (m + 1) // 2
            num_rects = triangle_num_n * triangle_num_m
            diff = abs(num_rects - target)

            if diff < min_diff:
                best_num_rects, min_diff, best_n, best_m, best_area  = num_rects, diff, n, m, n * m

            if num_rects > target + min_diff:
                break

    return  best_n, best_m, best_area, best_num_rects


if __name__ == "__main__":
    num = int(input("Enter a number: ")) # Inputs the number we will find the closest rectangle that has it amount of sub-rectangles
    print(find_the_best_rect(num)) # Prints the dimensions of the rectangle and its area followed by how many sub-rectangles