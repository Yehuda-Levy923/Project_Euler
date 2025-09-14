# Function to find the greatest common denominator (Taken directly from Problem5.py)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find the first digit of a number
def first_num(n):
    return [int(d) for d in str(n)][0]

# Function to find the last digit of a number
def last_num(n):
    return [int(d) for d in str(n)][-1]

# Function that finds all the 2 digit curious fractions and puts them in a list.  It finds them by checking for every j
# larger than i when 11<i<100 if the first digit (of j) equals the second digit (of i) and if so check if
# the first digit (of i) / second digit (of j) is the same as i/j
def find_fractions():
    all_curious_fractions = []
    for i in range(11, 100):
        for j in range(i, 100):
            fi, si = first_num(i), last_num(i)
            fj, sj = first_num(j), last_num(j)
            if sj != 0 and j != 0 and i != j:
                if fj == si and i * sj == fi * j:
                    all_curious_fractions.append((i, j))
    return all_curious_fractions

# Function that multiplies all the fractions in curious_fractions then simplifies and returns the denominator
def multiply_fractions(curious_fractions):
    num, den = 1, 1
    for n, d in curious_fractions:
        num *= n
        den *= d

    common = gcd(num, den)
    return den // common


if __name__ == '__main__':
    print(multiply_fractions(find_fractions())) # prints the denominator of the simplified multiplication of all
                                                # curious fractions when the num/den < 1 and 10<num,den<100