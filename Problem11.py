# read grid rows from user input
def grid_input(r, columns):
    new_grid = []
    print(f"Enter the grid values row by row ({columns} values per row):")
    for i in range(r):
        while True:
            row_input = input().split()
            row = [int(value) for value in row_input]
            new_grid.append(row)
            break
    return new_grid

# calculate and return max product of n adjacent numbers in all directions
def max_adjacent_product(grid, n):
    the_rows, columns = len(grid), len(grid[0])
    directions = [(0,1), (1,0), (1,1), (1,-1)]  # directions: right, down, diagonal right, diagonal left
    return max(
        eval('*'.join(f'grid[i+{k*dx}][j+{k*dy}]' for k in range(n))) # multiply n numbers in direction (dx, dy) starting at (i, j)
        for i in range(the_rows) for j in range(columns)
        for dx, dy in directions
        if all(0 <= i + k*dx < the_rows and 0 <= j + k*dy < columns for k in range(n)) # only consider positions where all n elements fit inside grid otherwise we would multiply an int by None
    )

if __name__ == '__main__':
    rows = int(input("Enter number of rows: ")) # inputs number of grid rows
    cols = int(input("Enter number of columns: ")) # inputs number of grid columns
    grid = grid_input(rows, cols) # input the entire grid itself
    num = int(input("Enter number of adjacent ones you want to calculate: "))  # length of adjacent sequence we will calculate
    print(max_adjacent_product(grid, num)) # output max product found
