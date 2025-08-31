#function that finds the factors of any given number inspiration taken from Problem12
def regular_factors(n):
    factors = {1}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.add(i)
            if i != n // i:
                factors.add(n // i)
    return factors


#checks if the numbers are amicable numbers (sum of divisors equals other number and vice versa)
def amicable_numbers_checker(num1, num2):
    return sum(regular_factors(num1)) == num2 and sum(regular_factors(num2)) == num1

#sums all the numbers that are amicable numbers between 1 and n (no repeating)
def sum_all_amicable_numbers(n):
    sum_of_all = 0
    for i in range(2, n):
        d = sum(regular_factors(i))
        if i < d < n:
            if sum(regular_factors(d)) == i:
                sum_of_all += i + d
    return sum_of_all

if __name__ == "__main__":
    n = int(input("Enter a number: ")) #input the number you want to sum the amicable numbers between 1 and it
    print(sum_all_amicable_numbers(n)) #prints the sum of the amicable numbers between 1 and n