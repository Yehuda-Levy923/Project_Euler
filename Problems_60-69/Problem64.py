# Calculates the period length by starting with the base (a0), then iteratively updating m, d, and a
# using the continued fraction recurrence until we have a repeated state, which marks the end of the repeating cycle.
def period_length(n):
    a0 = int(n ** 0.5)
    if a0 * a0 == n:
        return 0
    m, d, a, period = 0, 1, a0, 0
    seen = {}

    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        period += 1

        state = (m, d, a)
        if state in seen:
            return period - seen[state]
        seen[state] = period

# Finds all the odd period sqrts below the given n and returns how many there are
def find_all_odd_period_sqrt(n):
    count = 0
    for i in range(2, n + 1):
        if period_length(i) % 2 == 1:
            count += 1
    return count


if __name__ == '__main__':
    num = int(input("Enter the maximum number: "))  # Inputs the max number that you want to check the amount of odd periods
    print(find_all_odd_period_sqrt(num)) # Prints the number of odd period sqrts under num