#function that starts from the second-to-last row of a pyramid and, for each element,
#adds it to the maximum of its two adjacent elements below.
#It repeats this process row by row upwards until only one element remains at the top.
def find_most_expensive_path(triangle):
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])
    return triangle[0][0]

# reads a pyramid of numbers from user input this function is almost identical to in Problem11 and Problem13
def pyramid_of_nums_input(height_of_tree):
    triangle = []
    print("Enter the values row by row, where each row has one more number than the last:")
    for i in range(height_of_tree):
        num_input = input().split()
        row = [int(value) for value in num_input]
        triangle.append(row)
    return triangle

if __name__ == "__main__":
    height = int(input("Enter the height of the triangle: ")) # inputs value of height of the pyramid
    print(find_most_expensive_path(pyramid_of_nums_input(height)))  # inputs the pyramid and searches for shortest path