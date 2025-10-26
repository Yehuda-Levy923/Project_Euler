# Finds all cubes until n the for all with the same length it groups them together
def cubes_with_same_lengths(n):
    groups = {}
    for i in range(1, n+1):
        cube = i**3
        key = ''.join(sorted(str(cube)))
        if key not in groups:
            groups[key] = []
        groups[key].append(cube)
    return groups

# Using the groups found above it iterates through them and finds the permutations in each group and returns the one with the smallest number
def find_permuted_cubes(n, amount):
    all_groups = cubes_with_same_lengths(n)
    for cubes in all_groups.values():
        if len(cubes) >= amount:
            return cubes[:amount]
    return None


if __name__ == '__main__':
    num = int(input("Check cubes up to: ")) # Input the number you want to check the cubes until  (1000000 works until 49 very quickly)
    permuted_cubes = int(input("How many permuted cubes do you want? ")) # The number of cubed permutes you want to find
    print(find_permuted_cubes(num, permuted_cubes)) # Prints the list in ascending order of all cubes that are permutes of each other