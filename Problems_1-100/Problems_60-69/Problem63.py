# Checks if the length of the first given (n) is the same s the value of the second (e)
def power_len_comp_power(n, e):
    return len(str(n)) == e

# Checks all the plausible options according to notes in the function
def check_all_plausible():
    count = 0
    for i in range(1,10):# If you take 10^n, it always has n+1 digits.
                         # That means only bases 1 through 9 are worth checking, because 10^n and higher bases will always overshoot.
        for j in range(1,22): # 9^22 = 984770902183611232881, has 21 digits meaning anything higher will still fall short.
            if power_len_comp_power(i**j,j):
                count += 1

    return count


if __name__ == '__main__':
    print(check_all_plausible()) # Prints how many n-digit positive integers exist which are also an nth power