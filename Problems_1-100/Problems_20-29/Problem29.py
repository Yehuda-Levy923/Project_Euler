# This function generates a list of all distinct values of i^j and j^i for every pair of integers i and j in the ranges
# [2, a) and [2, b)
def making_all_distinct_squares(a, b):
    all_distinct_squares = []
    for i in range(2,a):
        for j in range(2,b):
            if i**j not in all_distinct_squares:
                all_distinct_squares.append(i**j)
            if j**i not in all_distinct_squares:
                all_distinct_squares.append(j**i)
    return all_distinct_squares

if __name__ == '__main__':
    n = int(input("enter 2 numbers: ")) # the numbers which we will find amount of distinct a^b and b^a from 2 until a and b
    m = int(input())
    print(len(making_all_distinct_squares(n,m)), making_all_distinct_squares(n,m)) # prints the amount of distinct a^b and b^a and all of them