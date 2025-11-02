#The problem is similar to asking: if people are considered connected based on the colours of shirts they wear,
# who is connected to the most others? It would be the person whose shirt shares the most colours in common with everyone else's.
# Meaning here we will start from the lowest prime and build up until we pass 1000000 and take 1 step back.
# 1 * 2 * 3 * 5 * 7 * 11 * 13 * 17 (* 19) = 510510  (9,699,690)
#                                passes limit         with 19


#                                 Here is a coding approach:
# Uses a sieve-based approach to compute Euler's Totient function phi(n) for all n up to num
def compute_totients(num):
    phi = list(range(num + 1))
    for i in range(2, num + 1):
        if phi[i] == i:
            for j in range(i, num + 1, i):
                phi[j] -= phi[j] // i
    return phi

# Finds the largest ratio between n and phi(n) for all n up to num
def find_largest_n_ratio_phi_n(num):
    phi = compute_totients(num)
    max_ratio, best_n = 0, 0
    for n in range(2, num + 1):
        ratio = n / phi[n]
        if ratio > max_ratio:
            max_ratio = ratio
            best_n = n
    return best_n, max_ratio


if __name__ == "__main__":
    n = int(input("Enter the maximum n that can be returned: ")) # Inputs value you want to find the largest n that the number of positive
                                                                 # integers not exceeding n which are relatively prime to n over n is maximal.
    print(find_largest_n_ratio_phi_n(n)) # Outputs the value of the n and the value of the n/phi(n)