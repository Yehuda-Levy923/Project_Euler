# Inputs the matrix that is nxn sized (Directly from Problem81.py)
def input_matrix(n):
    data = []
    for _ in range(n):
        line = input()
        numbers = list(map(int, line.strip().split(',')))
        data.append(numbers)
    return data

# Function finds the shortest path from a starting point to all other points in a graph by always expanding the least costly path first.
# It keeps track of the minimum known distance to each node and updates it whenever a shorter path is found through a neighboring node.
def dijkstra(matrix, n):
    visited = [[False] * n for _ in range(n)]
    distances = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        distances[i][0] = matrix[i][0]
    while True:
        min_dist, min_pos = float('inf'), (-1, -1)
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and distances[i][j] < min_dist:
                    min_dist = distances[i][j]
                    min_pos = (i, j)

        if min_pos == (-1, -1):
            break
        i, j = min_pos
        visited[i][j] = True

        for di, dj in [(-1, 0), (1, 0), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                new_dist = distances[i][j] + matrix[ni][nj]
                if new_dist < distances[ni][nj]:
                    distances[ni][nj] = new_dist

    return min(distances[i][n - 1] for i in range(n))

if __name__ == "__main__":
    size = int(input("Enter the size of the matrix: ")) # Inputs the size of the matrix that you will input
    print(f"Enter {size} comma-separated numbers {size} times: ") # Input the numxnum sized matrix which we will find the sortest path for
    print(dijkstra(input_matrix(size), size)) # Prints the weight of the lightest path across the matrix only moving right and down and up