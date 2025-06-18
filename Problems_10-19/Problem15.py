#function that inputs a number and outputs its factorial using iterative multiplication
def factorial(num):
    factorial_equals = 1
    for i in range(1, num + 1):
        factorial_equals = factorial_equals * i
    return factorial_equals

#uses the equation: (X+Y) nCr X = (X+Y)! / (X!·Y!) to calculate all possible routes
def find_on_grid_options(numX, numY):
    return factorial(numX + numY)//(factorial(numX)*factorial(numY))

if __name__ == '__main__':
    X_on_grid = int(input("Enter the X value: ")) # inputs value of X on the graph
    Y_on_grid = int(input("Enter the Y value: ")) # inputs value of Y on the graph
    print(find_on_grid_options(X_on_grid, Y_on_grid)) # prints amount of all possible routes to (X,Y)

