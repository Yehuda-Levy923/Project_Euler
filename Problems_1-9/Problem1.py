#main that calculates the sum of all numbers divisible by 3 or 5 until the input
if __name__ == '__main__':
    n = int(input("Enter a number (upper limit): ")) #input a number for the upper limit
    m = int(input("Enter a number (lower limit): ")) #input a number for the lower limit
    print(sum(i for i in range(1, n) if i % 3 == 0 or i % 5 == 0)) #prints the sum of all the numbers in
                                                                   #the range you input that comply with
                                                                   #the if (divisible by 3V5)