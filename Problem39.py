def pythagorean_triplets(sum_total):
    triplets = []
    for a in range(1, sum_total // 2):
        for b in range(a, sum_total // 2):
            c = sum_total - a - b
            if a**2 + b**2 == c**2:
                triplets.append([a, b, c])
    return triplets


def maximum_solutions_finder(max_check):
    max_count = 0
    best_sum = 0
    for total in range(12, max_check,2):
        count = len(pythagorean_triplets(total))
        if count > max_count:
            max_count = count
            best_sum = total
    return best_sum, max_count

print(maximum_solutions_finder(1000))