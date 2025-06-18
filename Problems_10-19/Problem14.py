#function that applies the Collatz rule until reaching 1, counting however many steps it takes
def Collatz_Problem(num):
    counter = 1
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        counter += 1
    return counter

#function that loops through all numbers from 1 to num - 1, and finds the one with the longest Collatz sequence
def check_longest_chain(num):
    biggest_length = 0
    number_with_longest = 1
    for i in range(1, num):
        length = Collatz_Problem(i)
        if length > biggest_length:
            biggest_length = length
            number_with_longest = i
    return number_with_longest, biggest_length

if __name__ == '__main__':
    num_to_check = int(input("Enter a limit and the program will check all numbers from 1 up to that limit,"
                             " and find which number has the longest Collatz sequence: ")) #inputs the max number used for the check
    print(check_longest_chain(num_to_check)) # output max chain head and length found
