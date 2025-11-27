# Count new integer shortest path cuboids added when increasing M by 1
def delta_count(M):
    new_count, a = 0, M
    for k in range(2, 2 * a + 1):
        shortest_path_squared = a * a + k * k
        root = int(shortest_path_squared ** 0.5)
        if root * root == shortest_path_squared:
            upper_c = k // 2
            lower_c = max(1, k - M)

            if upper_c >= lower_c:
                new_count += (upper_c - lower_c + 1)

    return new_count

# Incremental approach to find smallest M exceeding target count of integer shortest path cuboids
def smallest_M_exceeding_target(target):
    M, total_count = 1, 0
    while True:
        total_count += delta_count(M)
        if total_count > target:
            return M
        M += 1

if __name__ == "__main__":
    n = int(input("Enter the maximum number for target: ")) # Input for M threshold
    print(smallest_M_exceeding_target(n)) # Print the minimum M for the given the threshold n