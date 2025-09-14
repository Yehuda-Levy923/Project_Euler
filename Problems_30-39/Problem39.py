# Finds all Pythagorean triplets (a, b, c) such that a + b + c = sum_total
# Iterates through possible values of a and b, calculates c as the remainder
# Checks if the triplet satisfies the Pythagorean condition a² + b² = c²
# Returns a list of all valid triplets that meet the condition
def pythagorean_triplets(sum_total):
    triplets = []
    for a in range(1, sum_total // 2):
        for b in range(a, sum_total // 2):
            c = sum_total - a - b
            if a**2 + b**2 == c**2:
                triplets.append([a, b, c])
    return triplets

# Iterates through even values of total from 12 (the minimum triplet) up to max_check (since odd totals can't form valid triplets)
# For each total, finds how many Pythagorean triplets exist using pythagorean_triplets()
# Keeps track of the total that yields the maximum number of solutions
# Returns the total with the most solutions and the count of those solutions
def maximum_solutions_finder(max_check):
    max_count = 0
    best_sum = 0
    for total in range(12, max_check, 2):
        count = len(pythagorean_triplets(total))
        if count > max_count:
            max_count = count
            best_sum = total
    return best_sum, max_count

if __name__ == '__main__':
    n = int(input("Enter a number: ")) # The maximum number which we will find the number with the most pythagorean triplets that sum to it.
    print(maximum_solutions_finder(n)) # Print the value of total ≤ n that produces the most Pythagorean triplet solutions and how many