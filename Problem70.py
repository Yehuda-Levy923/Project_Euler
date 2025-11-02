# Uses a sieve-based approach to compute Euler's Totient function phi(n) for all n up to num
def compute_totients(num):
    phi = list(range(num + 1))
    for i in range(2, num + 1):
        if phi[i] == i:
            for j in range(i, num + 1, i):
                phi[j] -= phi[j] // i
    return phi

# Finds the smallest ratio from a list of (ratio, n) tuples
def find_smallest_ratio(lst):
    smallest_ratio = (float('inf'), 0)
    for i in lst:
        if i[0] < smallest_ratio[0]:
            smallest_ratio = i
    return smallest_ratio

# Finds all n such that phi(n) is a digit permutation of n
def find_permutation_with_phi(num):
    phi = compute_totients(num)
    all_permutation_with_phi = []
    for i in range(2, num + 1):
        if sorted(str(i)) == sorted(str(phi[i])):
            ratio = i / phi[i]
            all_permutation_with_phi.append((ratio, i))
    return all_permutation_with_phi

if __name__ == "__main__":
    max_n = int(input("Enter the max n you want to check for: ")) # Inputs value you want to find the smallest ratio that the number of positive
                                                                  # integers not exceeding n which are relatively prime to n over n is minimal
                                                                  # also makes sure we only check n is contactable to phi(n)
    print(find_smallest_ratio(find_permutation_with_phi(max_n)))  # Outputs the value of the n and the value of the n/phi(n)